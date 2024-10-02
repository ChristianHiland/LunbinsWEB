const display = document.getElementById('display');
const buttons = document.querySelectorAll('.keypad button');
const MAX_LENGTH = 5; // Set the maximum allowed length of the passcode
var AUTH_CODE = 0;

buttons.forEach(button => {
  button.addEventListener('click', () => {
    const buttonText = button.textContent;

    if (buttonText === 'C') {
      display.value = ''; // Clear the display
    } else if (display.value.length < MAX_LENGTH) { 
      display.value += buttonText; // Append the button text to the display

      // If the passcode is complete (reached MAX_LENGTH)
      if (display.value.length === MAX_LENGTH) {
        // Send the passcode to the Python backend for verification
        const passcode = display.value;
        fetch('/verify_passcode', {  
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: 'passcode=' + passcode
        })
        .then(response => response.text())
        .then(result => {
            if (result === 'Success') {
                PinSuccessFunction();
            } else {
                console.log('Incorrect passcode');
            }
            display.value = result; // Clear the display after verification
        })
        .catch(error => {
            console.error('Error verifying passcode:', error);
            display.value = ''; // Clear the display on error
        });
      }
    }
  });
});

function PinSuccessFunction() {
    // Sending To Backend
    fetch('/AuthReady', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: "AuthReady=Ready"
    })
    .then(response => {
        if (!response.ok) {throw new Error('Network response was not ok');}
        return response.text(); // Extract the text content from the response
    })
    .then(result => {
        console.log(result);
        sessionStorage.setItem('AuthAdmin', result);
        location.replace("/authlogin");
    })
}