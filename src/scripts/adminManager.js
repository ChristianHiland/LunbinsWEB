const RestClicksB = document.getElementById('RestClicks');

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