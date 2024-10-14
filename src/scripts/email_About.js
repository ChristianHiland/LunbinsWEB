const SubmitButton = document.getElementById("EmailSend");
const SenderEmail = document.getElementById("Email");
const Subject = document.getElementById("Subject");
const Body = document.getElementById("Body");

SubmitButton.addEventListener('click', () => {
    const data = {
        email: SenderEmail.value,
        subject: Subject.value,
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
        Body.value = data;
    })
    .catch((error) => {
        console.error("Error: ", error);
        Body.value = error;
    })
})