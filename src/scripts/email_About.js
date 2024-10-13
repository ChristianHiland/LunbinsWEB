const SubmitButton = document.getElementById("EmailSend");
const SenderEmail = document.getElementById("Email").value;
const Subject = document.getElementById("Subject").value;
const Body = document.getElementById("Body");

SubmitButton.addEventListener('click', () => {
    const data = {
        email: SenderEmail,
        subject: Subject,
        body: Body.value
    };
    console.log(data)

    fetch("/email_send", {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.text())
    .then(data => {
        console.log(data);
    })
    .catch((error) => {
        console.error("Error: ", error);
    })
})