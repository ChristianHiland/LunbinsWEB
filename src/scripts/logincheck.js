const LoginLink = document.getElementById("LoginID");

function CheckLoginStatus() {
    if (localStorage.getItem("loginID") != "") {
        LoginLink.textContent = "Profile";
        LoginLink.href = "{{url_for('userprofile')}}";
    }
}

CheckLoginStatus()