// Get the element with id "red_header"
const redHeader = document.getElementById('red_header');

// Add a click event listener to the "red_header" element
redHeader.addEventListener('click', function () {
  // Get the header element
    const header = document.querySelector('header');

  // Add the class "red" to the header element
    header.classList.add('red');
});
