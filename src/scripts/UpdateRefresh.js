function checkForUpdates() {
    fetch('/check_for_updates')
      .then(response => response.json())
      .then(data => {
        if (data.updated) {
          location.reload(); // Reload the page
        }
      })
      .catch(error => {
        console.error('Error checking for updates:', error);
    });
}

// Pi Server Check
function checkPiServer() {
  fetch('/piserver_check', {
    method: 'POST',
    headers: {
        "Content-Type": "application/json"
    },
    body: "picheck=check"
  })
    .then(response => response.json()) 
    .then(data => {
      if (data.status == "offline") {
        console.error("Pi Server is offline!");
      }
      else if (data.status == "off") {
        
      }
      else {
        console.info("Pi Server is online!");
        console.log(data)
      }
    })
    .catch(error => {
      console.error('Error checking for Pi Server:', error);
  });
}

setInterval(checkForUpdates, 5000); // Check every 5 seconds
setInterval(checkPiServer, 5000); // Check Pi Server every