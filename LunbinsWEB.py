#!/usr/bin/env python3

from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import subprocess
import datetime
import platform
import random
import psutil
import json
import os


# Fail Var Placeholders
FailSTRING = ""
MoreINFO = ""
# Module List
ModulesReady = ['json', 'random', 'psutil', 'platform', 'datetime', 'flask']
# Importing My Modules Safely
try:
    from src.pyScripts import *
    ModulesReady.append("email")
except Exception as ERROR:
    MoreINFO = "Email Script Raised Error"
    FailSTRING = ERROR

# Flask
app = Flask(__name__, template_folder='pages', static_folder='src', static_url_path='/src') 
# Config
UPLOAD_FOLDER = 'src/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'leelunbinteehee'

# Time
current_time = datetime.datetime.now()
# System Info
os_name = platform.system()
MemoryINFO = psutil.virtual_memory()
CPU_INFO = psutil.cpu_freq()

# Placeholder Vars
ReceiverEmail_Var = ""
FilePathData = {}
click_count = 0
IP = ""
PORT = ""

# Getting Data Files From Main Path JSON
# Getting Data From JSONs
if os_name.lower() == str("linux"):
    with open("LunbinsWEB/src/data/FilePath_Pi.json", "r") as Data:
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
    ReceiverEmail_Var = ServerConfig_Data["ReceiverEmail"]
    # Getting IP And Port
    IP = ServerConfig_Data["IP"]
    PORT = ServerConfig_Data["PORT"]
    # Making Var Checking Pi Server
    global PiServer_Check
    PiServer_Check = ServerConfig_Data["Pi"]["Check"]
    # Making & Setting Vars
    global Debug_EN
    Debug_EN = ServerConfig_Data["Self"]["Terminal"]["Debug"]
    global Clear_EN
    Clear_EN = ServerConfig_Data["Self"]["Terminal"]["Clear"]

# Vars
Click_FILE = FilePathData["Clicks"]
Auth_FILE = FilePathData["Auth"]
Server_FILE = FilePathData["Server"]
PFP_Types = ['.png', '.jpg', '.bmp']
AUDIO_Types = ['.mp3', '.ogg', '.wav']
VIDEO_Types = ['.mp4', '.mov']

#########################
# Setting Up HTML Pages #
#########################

# Index Page
@app.route('/')
def index():
    if FailSTRING != str(""):
        return render_template('ERROR.html', error=FailSTRING, moreinfo=MoreINFO)
    else:
        return render_template('index.html')
# About Page
@app.route('/about')
def about():
    return render_template('about.html')
# Howling Haven Page
@app.route('/howlinghaven')
def howlinghaven():
    return render_template('howlinghaven.html')
# Links Page
@app.route('/links')
def links():
    return render_template('links.html')
# Projects Page
@app.route('/projects')
def projects():
    return render_template('projects.html')
# Admin Page
@app.route('/adminlogin')
def adminlogin():
    return render_template('adminlogin.html')
# Auth Page
@app.route('/authlogin')
def authlogin():
    return render_template('authlogin.html')
# News Letter Page
@app.route('/newsletter')
def newsletter():
    return render_template('newsletter.html')
# User Login Page
@app.route('/login')
def userlogin():
    return render_template("userlogin.html")
# User Profile Page
@app.route('/userprofile')
def userprofile():
    return render_template("userprofile.html")
# Look Up User Profile
@app.route('/lookprofile')
def lookprofile():
    return render_template("lookprofile.html")
##########
# Events #
##########

# Store the initial modification times of your files
last_modified_times = {}
for filename in ['LunbinsWEB.py', 'pages/index.html', 'pages/about.html', 'pages/userprofile.html','pages/adminlogin.html','pages/authlogin.html','pages/ERROR.html','pages/howlinghaven.html','pages/links.html','pages/newsletter.html','pages/projects.html','pages/userlogin.html', 'pages/userprofile.html','src/scripts/adminManager.js','src/scripts/auth.js','src/scripts/email_about.js','src/scripts/Main.js','src/scripts/pinpad.js','src/scripts/script.js', 'src/scripts/userlogin.js','src/scripts/profile.js', 'src/pyScripts/Email.py', 'src/pyScripts/Tokenize.py', 'src/pyScripts/database.py', 'src/pyScripts/Tools.py', 'src/pyScripts/__init__.py']:
  last_modified_times[filename] = os.path.getmtime(filename)

# Check For Any Updates, if so Reload Page
@app.route('/check_for_updates')
def check_for_updates():
  if Clear_EN:
        os.system("clear")
  updated = False
  for filename, last_mtime in last_modified_times.items():
    current_mtime = os.path.getmtime(filename)
    if current_mtime > last_mtime:
      updated = True
      last_modified_times[filename] = current_mtime  # Update the last modified time
      break

  return jsonify({'updated': updated})
# Click Counter
@app.route("/save_clicks", methods=["POST"])
def save_clicks():
    global click_count
    click_count += int(request.form["clickCount"])

    # Storing The Updated Click Count.
    with open(Click_FILE, "w") as DATA_JSON:
        DIR_DATA = {"Clicks": click_count}
        json.dump(DIR_DATA, DATA_JSON, indent=4)
    return "Click Count Saved Successfully"
# Pi Server Check
@app.route("/piserver_check", methods=['POST'])
def PiServerCheck():
    if Clear_EN:
        os.system("clear")
    if PiServer_Check:
        print("SERVER CHECK")
        return jsonify({"status": Tools.ping("http://192.168.254.121/")})
    else:
        return jsonify({"status": "off"})
# Email Sender
@app.route('/email_send', methods=['POST'])
def EmailSend():
    data = request.get_json()
    email = data.get('email')
    subject = data.get('subject')
    body = data.get('body')
    Outcome = ""
    try:
        ModulesReady.index("email")
    except Exception as e:
        Outcome = e
    else:
        Email.SendEmail(email, ReceiverEmail_Var, subject, body)
        Outcome = "Email Sent!"
    return Outcome
# Admin Login
@app.route('/verify_passcode', methods=['POST'])
def verify_passcode():
    entered_passcode = request.form['passcode']
    correct_passcode = "39775"

    if entered_passcode == correct_passcode:
        return "Success"
    else:
        return "Failure"
# User Login Event
@app.route('/userlogin_send', methods=['POST'])
def UserLogin():
    data = request.get_json()
    Table = str("normalusers")
    Username = data.get("username")
    Password = data.get("password")

    return str(database.Login_User(Username, Password, Table))
# User Signup Event
@app.route("/usersignin_send", methods=['POST'])
def UserSign():
    data = request.get_json()
    Table = str("normalusers")
    Username = data.get("username")
    Password = data.get("password")
    Name = data.get("name")
    Age = data.get("age")
    file = data.get("pfp")
    user_id = database.Get_User(Username)

    try:
        database.Create_User(Username, Password, Name, Age, file, Table)
    except Exception as e:
        return e
# Get User Data Event
@app.route("/userinfo_send", methods=['POST'])
def SendUserInfo():
    data = request.get_json()
    loginID = data.get("id")
    UsernameEN = data.get("usernameen")
    
    Get = database.Get_UserInfo(loginID, UsernameEN)
    return jsonify(Get)
# Updaing User Data
@app.route("/userupdate_send", methods=['POST'])
def UpdateUserInfo():
    data = request.get_json()
    Data = [data.get("id"), data.get("furry"), data.get("gay"), data.get("tech"), data.get("art"), data.get("writer"), data.get("fursuit"), data.get("wolf"), data.get("fox"), data.get("bio")]
    database.Update_Table(Data)
    return jsonify(Data)
# Giving it a code
@app.route('/AuthReady', methods=['POST'])
def AuthReadySend():
    Status = request.form['AuthReady']

    if Status.lower() == str("ready"):
        random_string = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(10))
        with open(Auth_FILE, "w") as AuthSave:
            AUTH_DATA = {
                "AuthCode": random_string
            }
            json.dump(AUTH_DATA, AuthSave, indent=4)
        with open(Auth_FILE, "r") as GetAuth:
            Data = json.load(GetAuth)
            return str(Data["AuthCode"])
# Checking The Auth Code
@app.route('/AuthCheck', methods=['POST'])
def AuthCheckCode():
    UserCode = request.form['AuthCheck']

    with open(Auth_FILE, "r") as ServerAuth:
        ServerAuthD = json.load(ServerAuth)
        if ServerAuthD['AuthCode'] == UserCode:
            return "True"
        else:
            return "Something Went Wrong! WTF?! " + UserCode
    return "ERROR"
# Getting Buttons from Admin
@app.route('/AuthButton', methods=['POST'])
def ButtonsAdmin():
    data = request.get_json()
    ButtonID = data.get("authbutton")
    LinuxCMD = data.get("CMD")

    # Reset Clicks Button
    if ButtonID == 0:
        with open(Click_FILE, "w") as WriteClicks:
            DATA_DIR = {"Clicks": 0}
            json.dump(DATA_DIR, WriteClicks, indent=4)
        return "Click Clean Done!"
    # Check Clicks Button
    elif ButtonID == 1:
        with open(Click_FILE, "r") as CheckClicks:
            Data = json.load(CheckClicks)
            return str(Data['Clicks'])
    elif ButtonID == 2:
        with open(Server_FILE, "r") as ServerCheck:
            ServerInfo = json.load(ServerCheck)
        return ServerInfo
    elif ButtonID == 3:
        if FailSTRING != str(""):
            return FailSTRING
        else:
            return "No Errors Shown"
    elif ButtonID == 4:
        tokens = Tokenize.Tokenize_Input(LinuxCMD)

        if tokens:
            print(tokens)

            # Now I can use SubProcess
            process = subprocess.run(tokens, capture_output=True, text=True, check=True)
            print(process.stdout)
        return str(f"Command: {LinuxCMD}\n\nReturned:\n{process.stdout}")
    else:
        return "Wrong Button ID, or You're Just Shit."
# Uploading
@app.route('/upload_PFP', methods=['POST'])
def Upload():
    file = request.files['image']
    Username = request.form['username']
    NewName = Tools.generate_filename(file.filename)
    extension = os.path.splitext(filename)[1]
    # Checking File Types (Profile Picture)
    for EXT in PFP_Types:
        PFP_File = False
        if EXT == extension:
            PFP_File = True
    # Checking File Types (Audio File)
    for EXT in AUDIO_Types:
        AUDIO = False
        if EXT == extension:
            AUDIO = True   
    
    # If the file uploaded is a PFP Base File Then Update As.
    if PFP_File:
        FilePath = str(f"src/images/PFP/{NewName}")
        file.save(FilePath)
        try:
            ID = int(Username)
        except ValueError:
            ID = database.Get_User(Username)
        Tools.update_database(ID, FilePath)
    if AUDIO:
        FilePath = str(f"src/audio/Users/{NewName}")
        file.save(FilePath)
    return "uploaded"
if __name__ == '__main__':
    # Saving First Server Based Data
    with open(Server_FILE, "w") as ServerFile:
        Time_Start = current_time.strftime("%H:%M:%S")
        Day_Start = current_time.day

        Server_DATA = {
            "DayStarted": Day_Start,
            "TimeStarted": Time_Start,
            "CPU": {
                "Cores": psutil.cpu_count(logical=False),
                "Threads": psutil.cpu_count(logical=True),
                "Frequency": str(f"{CPU_INFO.current:.2f} MHz")
            },
            "Memory": {
                "Total": str(f"{MemoryINFO.total / (1024 ** 3):.2f} GB")
            }
        }

        json.dump(Server_DATA, ServerFile, indent=4)
    app.run(host=IP, port=PORT, debug=Debug_EN)
