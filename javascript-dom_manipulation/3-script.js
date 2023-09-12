// Get the element with id "red_header"
const togHeader = document.getElementById('toggle_header');

// Add a click event listener to the "red_header" element
togHeader.addEventListener('click', function () {
  // Get the header element
    const header = document.querySelector('header');

  // Add the class "red" or "green" to the header element
    header.classList.toggle('red');
    header.classList.toggle('green');
});
