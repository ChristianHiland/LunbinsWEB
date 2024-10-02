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

// Initial check on page load
checkWindowSize();

// Check again when the window is resized
window.addEventListener('resize', checkWindowSize);