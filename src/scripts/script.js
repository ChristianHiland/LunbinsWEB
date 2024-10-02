function checkWindowSize() {
  const elementToHide = document.querySelector('.element-to-hide');
  const elementToShow = document.querySelector('.element-to-show');
  if (window.innerWidth <= 720) { // Adjust the breakpoint as needed
    elementToHide.style.display = 'none';
    elementToShow.style.display = 'block';
  } else {
    elementToHide.style.display = 'block'; // Or any other appropriate display value
    elementToShow.style.display = 'none';  
  }
}

document.addEventListener('DOMContentLoaded', (event) => {
  // Your code to select elements and add event listeners goes here
  let clickCount = 1;
  const image = document.getElementById('LUNBIN_IMG'); 

  image.addEventListener('click', function() {
      console.log("Lunbin Clicked!"); 
      fetch('/save_clicks', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'clickCount=' + clickCount
      })
  });
});

// Initial check on page load
checkWindowSize();

// Check again when the window is resized
window.addEventListener('resize', checkWindowSize);