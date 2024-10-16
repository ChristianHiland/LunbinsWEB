# Importing Moduels
import mysql.connector
import platform
import bcrypt
import json

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

db = mysql.connector.connect(host=MySQL_IP, user=MySQL_Name, passwd=MySQL_PW, database=MySQL_Base)

DB_Cursor = db.cursor()

# Adds New Users To Database (users)
def Create_User(username, password, name, age, LinuxPFP, table="normalusers", table2="NormalInfo"):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()) 

    sql = "INSERT INTO users.normalusers (username, password) VALUES (%s, %s)"
    val = (username, hashed_password)
    DB_Cursor.execute(sql, val)
    db.commit()
    print(DB_Cursor.rowcount, "record inserted.")
    # Recording Onto The Other Database
    sql = "INSERT INTO users.normalinfo (username, name, age, LinuxPFP) VALUES (%s, %s, %s, %s)"
    val = (username, name, age, LinuxPFP)
    DB_Cursor.execute(sql, val)
    db.commit()
    print(DB_Cursor.rowcount, "record inserted.")
    # Recording Onto The Tags Database
    sql = "INSERT INTO users.tags (furry, gay, tech, art, writer, fursuit, wolf, fox) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (0, 0, 0, 0, 0, 0, 0, 0)
    DB_Cursor.execute(sql, val)
    db.commit()
    print(DB_Cursor.rowcount, "record inserted.")
    # Recording Onto The Bio Database
    sql = "INSERT INTO users.bio (biocol) VALUES (%s)"
    val = ("Bio Not Set")
    DB_Cursor.execute(sql, val)
    db.commit()
    print(DB_Cursor.rowcount, "record inserted.")

# Checks for right login from user in database (users)
def Login_User(username, password, table="normalusers"):

    PyBytes_Password = password.encode('utf-8')
    # Getting Table
    DB_Cursor.execute(f"""
    SELECT * FROM {table}
    """)
    myresult = DB_Cursor.fetchall()
    # Checking Each User, then returning User ID if Found:
    for row in myresult:
        PyBytes_ROW = row[2].encode('utf-8')
        if row[1] == username:
            if bcrypt.checkpw(PyBytes_Password, PyBytes_ROW):
                return row[0]
            elif bcrypt.checkpw(PyBytes_Password, PyBytes_ROW) != True:
                return "Wrong Password"
        elif row[1] != username:
            pass
# Updates Table
def Update_Table(Data):
    UserID = Data[0]
    furry = Data[1]
    gay = Data[2]
    tech = Data[3]
    art = Data[4]
    writer = Data[5]
    fursuit = Data[6]
    wolf = Data[7]
    fox = Data[8]
    bio = Data[9]
    # Updating Tags Table
    sql = "UPDATE users.tags SET furry = %s, gay = %s, tech = %s, art = %s, writer = %s, fursuit = %s, wolf = %s, fox = %s WHERE id = %s"
    val = (furry, gay, tech, art, writer, fursuit, wolf, fox, UserID)
    # Updating Database
    DB_Cursor.execute(sql, val)
    db.commit()
    print(DB_Cursor.rowcount, "record inserted.")
    
    # Updating Bio Table
    sql = "UPDATE bio SET biocol = %s WHERE id = %s"
    val = (bio, UserID)
    # Updating Database
    DB_Cursor.execute(sql, val)
    db.commit()
    print(DB_Cursor.rowcount, "record inserted.")
# Gets All Users from Database (users)
def Get_User(Username):
    # Getting All The Rows From The Table
    DB_Cursor.execute("""
    SELECT * FROM users.normalusers
    """)
    # Putting In A Var
    myresult = DB_Cursor.fetchall()
    # Printing each one
    for row in myresult:
        if row[1] == str(Username):
            return row[0]
    return "failed"
# Get User Data
def Get_UserInfo(UserID, UsernameEN):
    bio = ""

    if UsernameEN == 1:
        UserID = Get_User(UserID)

    if UserID == str("failed"):
        Data = {
            "username": "Wrong Username",
            "name": "Wrong Username",
            "age": 0,
            "pfp": 0,
            "furry": 0,
            "gay": 0,
            "tech": 0,
            "art": 0,
            "writer": 0,
            "fursuit": 0,
            "wolf": 0,
            "fox": 0,
            "bio": "You have entered a username that seems to not be on records!"
        }
        return Data
    # Normal Info Table
    query = "SELECT * FROM users.NormalInfo WHERE id = %s"
    DB_Cursor.execute(query, (UserID,))
    # Fetch and process the results
    for row in DB_Cursor:
        global NormalINFO_ROW
        NormalINFO_ROW = row
            
    # Tags Table
    query = "SELECT * FROM users.tags WHERE id = %s"
    DB_Cursor.execute(query, (UserID,))
    # Fetch and process the results
    Tags_ROW = DB_Cursor.fetchone()
    # Fetch bio data
    DB_Cursor.execute("SELECT biocol FROM bio WHERE id = %s", (UserID,))  # Assuming 'id' is the user ID column in the 'bios' table
    bio_result = DB_Cursor.fetchone()
    bio = bio_result[0] if bio_result else None  # Assign the bio data or None if not found

    ReturnData = {
        "username": NormalINFO_ROW[1],
        "name": NormalINFO_ROW[2],
        "age": NormalINFO_ROW[3],
        "pfp": NormalINFO_ROW[4],
        "furry": Tags_ROW[1],
        "gay": Tags_ROW[2],
        "tech": Tags_ROW[3],
        "art": Tags_ROW[4],
        "writer": Tags_ROW[5],
        "fursuit": Tags_ROW[6],
        "wolf": Tags_ROW[7],
        "fox": Tags_ROW[8],
        "bio": bio
    }

    print(f"!!!!!!!!!!!!!!!!!!!!!!!!\n\n{UserID}\n\nData:\n\n{ReturnData}\n\n!!!!!!!!!!!!!!!!!!")

    return ReturnData
# Gets All Users from Database (users)
def Get_Users(table):
    # Getting All The Rows From The Table
    DB_Cursor.execute("""
    SELECT * FROM users.normalusers
    """)
    # Putting In A Var
    myresult = DB_Cursor.fetchall()
    # Printing each one
    for row in myresult:
        print(f"Username: {row[1]}\nPassword: {row[2]}\nIndex ID: {row[0]}")