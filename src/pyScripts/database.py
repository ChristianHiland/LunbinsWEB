# Importing Moduels
import mysql.connector
import bcrypt

db = mysql.connector.connect(host="localhost", user="leelunbin", passwd="hiland39775", database="users")

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
    sql = "INSERT INTO users.NormalInfo (username, name, age, LinuxPFP) VALUES (%s, %s, %s, %s)"
    val = (username, name, age, LinuxPFP)
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
# Get User Data
def Get_UserInfo(UserID, table, table2):
    Username = ""
    Name = ""
    Age = 0
    PFP_Path = ""
        
    # Other Table
    DB_Cursor.execute(f"""
    SELECT * FROM {table2}
    """)
    # Putting In A Var
    myresult = DB_Cursor.fetchall()
    # Getting Username
    for row in myresult:
        if str(row[0]) == UserID:
            Username = str(row[1])
            Name = str(row[2])
            Age = str(row[3])
            PFP_Path = str(row[4])
    
    ReturnData = {
        "username": Username,
        "name": Name,
        "age": Age,
        "pfp": PFP_Path
    }

    return ReturnData
# Gets All Users from Database (users)
def Get_Users(table):
    # Getting All The Rows From The Table
    DB_Cursor.execute(f"""
    SELECT * FROM {table}
    """)
    # Putting In A Var
    myresult = DB_Cursor.fetchall()
    # Printing each one
    for row in myresult:
        print(f"Username: {row[1]}\nPassword: {row[2]}\nIndex ID: {row[0]}")
