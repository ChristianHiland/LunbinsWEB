# Importing Modules
import platform
import smtplib
import json

# Vars
os_name = platform.system()
# Placeholder Vars
FilePathData = {}
EmailPassword = ""

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
# Getting Email Password from the Password JSON
with open(FilePathData["Passwords"], "r") as Data:
    FileData = json.load(Data)
    EmailPassword = FileData["Email"]
    
# Starting / Setting Up SMTP Server
EmailSERVER = smtplib.SMTP("smtp.gmail.com", 587)
EmailSERVER.starttls()


# Logining Into The Server
EmailSERVER.login("hilandchristian112@gmail.com", EmailPassword)

        
def SendEmail(SenderEmail, ReceiverEmail, subject, body):
    text = str(f"Subject: {subject}\n\n{body}")

    EmailSERVER.sendmail(SenderEmail, ReceiverEmail, text)