const red_color = document.querySelector('header');

red_color.addEventListener("click", updateColor);

function updateColor() {
    red_color.style.color = '#FF0000';
}
