from flask import Flask, render_template, request
import random
import json

app = Flask(__name__, template_folder='pages', static_folder='src', static_url_path='/src') 

Click_FILE = str("/home/leelunbin/ServerTesting/LunbinsWEB/src/data/Clicks.json")
Auth_FILE = str("/home/leelunbin/ServerTesting/LunbinsWEB/src/data/Auth.json")
click_count = 0

#########################
# Setting Up HTML Pages #
#########################

# Index Page
@app.route('/')
def index():
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

##########
# Events #
##########

# Click Counter
@app.route("/save_clicks", methods=["POST"])
def save_clicks():
    global click_count
    click_count += int(request.form["clickCount"])

    # Storing The Updated Click Count.
    with open(Click_FILE, "w") as DATA_JSON:
        DIR_DATA = {
            "Clicks": click_count
        }
        json.dump(DIR_DATA, DATA_JSON, indent=4)
    return "Click Count Saved Successfully"

# Admin Login
@app.route('/verify_passcode', methods=['POST'])
def verify_passcode():
    entered_passcode = request.form['passcode']
    correct_passcode = "39775"

    if entered_passcode == correct_passcode:
        return "Success"
    else:
        return "Failure"
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
    ButtonID = request.form['AuthButton']

    if ButtonID == "0":
        with open(Click_FILE, "w") as WriteClicks:
            DATA_DIR = {
                "Clicks": 0
            }
            json.dump(DATA_DIR, WriteClicks, indent=4)
        return "Click Clean Done!"
    else:
        return "Wrong Button ID, or You're Just Shit."
if __name__ == '__main__':
    app.run(debug=True)
