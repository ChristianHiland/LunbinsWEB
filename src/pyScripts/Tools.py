# Importing Modules
from wtforms.validators import InputRequired
from wtforms import FileField, SubmitField
from flask_wtf import FlaskForm
import mysql.connector
import subprocess
import platform
import json
import os

# Vars (System)
os_name = platform.system()

# Checking System Config
# Getting Data Files From Main Path JSON
# Getting Data From JSONs
if os_name.lower() == str("linux"):
    with open("/home/biqu/Server/Data/FilePath_Pi.json", "r") as Data:
        FileData = json.load(Data)
        # Got File Paths
        FilePathData = FileData
elif os_name.lower() == str("windows"):
    with open("C:\\Users\\hilan\\Documents\\Code\\HTML\\LunbinsWEB\\src\\data\\FilePath_WIN.json", "r") as Data:
        FileData = json.load(Data)
        # Got File Paths
        FilePathData = FileData
# Getting Server Config
with open(FilePathData["ServerConfig"], "r") as Server:
    ServerConfig_Data = json.load(Server)
    # Saving Receiver Email
    MySQL_IP = ServerConfig_Data["MySQL"]["ServerIP"]
    MySQL_Name = ServerConfig_Data["MySQL"]["Username"]
    MySQL_PW = ServerConfig_Data["MySQL"]["Password"]
    MySQL_Base = ServerConfig_Data["MySQL"]["Database"]

# SQL Database
db = mysql.connector.connect(host=MySQL_IP, user=MySQL_Name, passwd=MySQL_PW, database=MySQL_Base)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Uploading File Func
def allowed_file(filename):
    """Checks if the file extension is allowed."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def update_database(user_id, filepath):
    """Updates the database with the image file path."""
    # ... your code to connect to the database and update the row ...
    # Example using mysql.connector:
    try:
        # ... your database connection details ...
        cursor = db.cursor()
        sql = "UPDATE users.normalinfo SET LinuxPFP = %s WHERE id = %s"
        val = (filepath, user_id)
        cursor.execute(sql, val)
        db.commit()
        print("Database updated successfully")
    except Exception as e:
        print(f"Error updating database: {e}")

def generate_filename(filename):
    """Generates a custom filename to avoid conflicts."""
    # Example: Add a timestamp to the filename
    import time
    timestamp = str(int(time.time()))
    return f"{timestamp}_{filename}"

# Other File Uploading Funcs
class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")
# Ping Func
def ping(host:str):
    """Pings a host and checks if it's reachable.

    Args:
        host: The hostname or IP address to ping.

    Raises:
        CalledProcessError: If the ping command fails.
    """
    try:
        # Use the ping command with a count of 4 and a timeout of 2 seconds
        subprocess.run(['ping', '-n', '4', '-w', '2', host], check=True)  
        print(f"{host} is reachable")
    except subprocess.CalledProcessError:
        return str("offline")
    else:
        return str("online")