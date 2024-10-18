// Getting Button
const LoginB = document.getElementById("loginbutton");
const signinB = document.getElementById("signinbutton");
const uploadB = document.getElementById("uploadButton")
// Getting Values
const UsernameVAL = document.getElementById("Username");
const PasswordVAL = document.getElementById("password");
const UsernameVAL2 = document.getElementById("Username2");
const PasswordVAL2 = document.getElementById("password2");
const NameVAL = document.getElementById("name");
const AgeVAL = document.getElementById("age");
const PFPVAL = document.getElementById("PFP");
// Status Vars
const LoginStatusVAL = document.getElementById('LoginStatus');
// Divs
const SignInDIV = document.getElementById("SignIN");
const LoginDIV = document.getElementById("LoginIN")
;

// Logining in If it is true, then send the user with a agree.
LoginB.addEventListener('click', () => {
    const data = {
        username: UsernameVAL.value,
        password: PasswordVAL.value
    };
    fetch("/userlogin_send", {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.text())
    .then(data => {
        if (data == "") {
            localStorage.setItem("loginID", "failed")
        }
        else if (data != "") {
            localStorage.setItem("loginID", data)
            LoginStatusVAL.textContent = "Logged in as User ID: " + data
        }
        else {
            console.log(data)
        }
    })
    .catch((error) => {
        console.error("Error: ", error);
        Body.value = error;
    })
})

function uploadFile() {
    const UsernameVAL2 = document.getElementById("Username2");
    const fileInput = document.getElementById('PFP');
    const file = fileInput.files[0];

    if (file) {
      const formData = new FormData();
      formData.append('image', file);
      formData.append('username', UsernameVAL2.value);

      fetch('/upload_PFP', { 
        method: 'POST',
        body: formData
      })
      .then(response => response.json())
      .then(data => {
        console.log('Success:', data);
      })
      .catch(error => {
        console.error('Error:', error);
        });
    }
}
// Logining in If it is true, then send the user with a agree.
signinB.addEventListener('click', () => {
    const data = {
        username: UsernameVAL2.value,
        password: PasswordVAL2.value,
        name: NameVAL.value,
        age: AgeVAL.value,
        pfp: PFPVAL.value
    };
    fetch("/usersignin_send", {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.text())
    .then(data => {
        if (data == "") {
            localStorage.setItem("loginID", "created")
        }
        else if (data != "") {
            LoginStatusVAL.textContent = "Error: Username Taken!"
            LoginStatusVAL.style = "color: red;"
        }
        else {
            console.log(data)
        }
    })
    .catch((error) => {
        console.error("Error: ", error);
        Body.value = error;
    })
})

if (localStorage.getItem("loginID") != null) {
    LoginStatusVAL.textContent = "Logged in as User ID: " + localStorage.getItem("loginID")
    LoginStatusVAL.style = "color: #57ff62;"
    LoginB.disabled = true;
    signinB.disabled = true;
    LoginDIV.style.display = "none";
    SignInDIV.style.display = "none";
}