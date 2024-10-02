const Auth_String = sessionStorage.getItem('AuthAdmin');

function CheckAuthCode() {
    fetch('/AuthCheck', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: "AuthCheck=" + Auth_String
    })
    .then(response => {
        if (!response.ok) {throw new Error('Network response was not ok');}
        return response.text(); // Extract the text content from the response
    })
    .then(result => {
        console.log(result);
        if (result === "True") {
            sessionStorage.setItem("IsAdmin", "Yes");
        }
        else {
            sessionStorage.setItem("IsAdmin", "No");
        }
    })
}

CheckAuthCode();