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

  setInterval(checkForUpdates, 2000); // Check every 5 seconds