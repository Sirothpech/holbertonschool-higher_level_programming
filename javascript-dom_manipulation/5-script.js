// Get the element with id "update_header"
const updateHeader = document.getElementById('update_header');

updateHeader.addEventListener('click', function () {

    const header = document.querySelector('header');

    header.innerText = 'New Header!!!';
});
