// Buttons
const RestClicksB = document.getElementById('RestClicks');
const CheckClicksB = document.getElementById('CountCheck');
const ServerStatusB = document.getElementById('ServerStatus');
const ErrorCheckB = document.getElementById('ErrorCheck');
const LinuxCMDB = document.getElementById("LinuxCMD");
// Textarea
const LinuxCMD_Display = document.getElementById("LinuxCMD_Textarea");
// Display
const AdminDisplay = document.getElementById('AdminDisplay');

// Tell Backend to Run The Func To Reset Clicks
RestClicksB.addEventListener('click', () => {
    const Data = {
        authbutton: 0,
        CMD: LinuxCMD_Display.value
    }
    fetch('/AuthButton', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(Data)
    })
    .then(response => {
        if (!response.ok) {throw new Error('Network response was not ok');}
        return response.text(); // Extract the text content from the response
    })
    .then(result => {
        console.log(result);
        AdminDisplay.value = result;
    })
});
// Tell Backend to Run The Func To Check Clicks
CheckClicksB.addEventListener('click', () => {
    const Data = {
        authbutton: 1,
        CMD: LinuxCMD_Display.value
    }
    fetch('/AuthButton', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(Data)
    })
    .then(response => {
        if (!response.ok) {throw new Error('Network response was not ok');}
        return response.text(); // Extract the text content from the response
    })
    .then(result => {
        console.log(result);
        AdminDisplay.value = "Click Count: " + result
    })
});
// Tell Backend to Run The Func To Send Server
ServerStatusB.addEventListener('click', () => {
    const Data = {
        authbutton: 2,
        CMD: LinuxCMD_Display.value
    }
    fetch('/AuthButton', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(Data)
    })
    .then(response => {
        if (!response.ok) {throw new Error('Network response was not ok');}
        return response.text(); // Extract the text content from the response
    })
    .then(result => {
        console.log(result);
        AdminDisplay.value = result;
    })
});
// Tell Backend To Run The Func To Check For Errors
ErrorCheckB.addEventListener('click', () => {
    const Data = {
        authbutton: 3,
        CMD: LinuxCMD_Display.value
    }
    fetch('/AuthButton', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(Data)
    })
    .then(response => {
        if (!response.ok) {throw new Error('Network response was not ok');}
        return response.text(); // Extract the text content from the response
    })
    .then(result => {
        console.log(result);
        AdminDisplay.value = result;
    })
});
// Tell Backend To Run A Linux CMD
LinuxCMDB.addEventListener('click', () => {
    const Data = {
        authbutton: 4,
        CMD: LinuxCMD_Display.value
    }
    fetch('/AuthButton', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(Data)
    })
    .then(response => {
        if (!response.ok) {throw new Error('Network response was not ok');}
        return response.text(); // Extract the text content from the response
    })
    .then(result => {
        console.log(result);
        AdminDisplay.value = result;
    })
});
function ToggleContent() {
    const IsAdmin = sessionStorage.getItem("IsAdmin");
    const content = document.getElementById('IsAdmin');
    const content2 = document.getElementById('IsAdmin2');
    if (IsAdmin == "Yes") {
        content.style.display = 'flex';
        content2.style.display = 'flex';
    }
    else {
        content.style.display = 'none';
        content2.style.display = 'none';
    }
}

setTimeout(ToggleContent, 200);