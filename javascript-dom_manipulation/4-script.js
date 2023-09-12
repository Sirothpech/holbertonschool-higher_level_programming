// Récupère l'élément avec l'ID "add_item" (le bouton "Add item")
const addItemButton = document.getElementById("add_item");

// Récupère l'élément <ul> avec la classe "my_list"
const myList = document.querySelector(".my_list");

// Ajoute un écouteur d'événement pour le clic sur le bouton "Add item"
addItemButton.addEventListener("click", function () {
    // Crée un nouvel élément <li>
    const newItem = document.createElement("li");

    // Définit le texte à afficher dans le nouvel élément <li>
    newItem.textContent = "Item";

    // Ajoute le nouvel élément <li> à la liste <ul>
    myList.appendChild(newItem);
});
