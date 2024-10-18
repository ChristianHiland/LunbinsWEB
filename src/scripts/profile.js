// Button
const SaveButton = document.getElementById("Submit");

SaveButton.addEventListener('click', () => {
    // Bio
    const Bio = document.getElementById("Bio");
    // Tags
    const FURRY = document.getElementById("FurryID").checked;
    const GAY = document.getElementById("GayID").checked;
    const TECH = document.getElementById("TechID").checked;
    const ART = document.getElementById("ArtID").checked;
    const WRITER = document.getElementById("WriterID").checked;
    const FURSUIT = document.getElementById("FursuitID").checked;
    const WOLF = document.getElementById("WolfID").checked;
    const FOX = document.getElementById("FoxID").checked;
    // USER ID
    const LoginID = localStorage.getItem("loginID");
    // DATA

    const data = {
        id: LoginID,
        furry: FURRY,
        gay: GAY,
        tech: TECH,
        art: ART,
        writer: WRITER,
        fursuit: FURSUIT,
        wolf: WOLF,
        fox: FOX,
        bio: Bio.textContent
    };
    fetch("/userupdate_send", {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })
    .catch((error) => {
        console.error("Error: ", error);
        Body.value = error;
    })
    // Uploading PFP
    const fileInput = document.getElementById('IMG');
    const file = fileInput.files[0];

    if (file) {
      const formData = new FormData();
      formData.append('image', file);
      formData.append('username', LoginID);

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
    location.reload();
})