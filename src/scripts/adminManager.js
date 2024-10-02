// Buttons
const RestClicksB = document.getElementById('RestClicks');
const CheckClicksB = document.getElementById('CountCheck');
const ServerStatusB = document.getElementById('ServerStatus');
// Display
const AdminDisplay = document.getElementById('AdminDisplay');

// Tell Backend to Run The Func To Reset Clicks
RestClicksB.addEventListener('click', () => {
    fetch('/AuthButton', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: "AuthButton=0"
    })
    .then(response => {
        if (!response.ok) {throw new Error('Network response was not ok');}
        return response.text(); // Extract the text content from the response
    })
    .then(result => {
        console.log(result);
    })
});
// Tell Backend to Run The Func To Check Clicks
CheckClicksB.addEventListener('click', () => {
    fetch('/AuthButton', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: "AuthButton=1"
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
    fetch('/AuthButton', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: "AuthButton=2"
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

ToggleContent();