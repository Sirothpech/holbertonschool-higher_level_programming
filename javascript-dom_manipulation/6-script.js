// Sélectionnez l'élément avec l'ID "character" dans le DOM
const characterElement = document.getElementById("character");

// URL de l'API Star Wars pour récupérer les données du personnage n° 5
const apiUrl = "https://swapi-api.hbtn.io/api/people/5/?format=json";

// Utilisez la Fetch API pour faire la requête
fetch(apiUrl)
    .then((response) => {
    // Vérifiez si la réponse est OK (statut HTTP 200)
    if (!response.ok) {
        throw new Error("Network response was not ok");
    }
    // Analysez la réponse JSON
    return response.json();
    })
    .then((data) => {
    // Récupérez le nom du personnage à partir des données JSON
    const characterName = data.name;

    // Mettez à jour le contenu de l'élément avec l'ID "character" avec le nom du personnage
    characterElement.textContent = characterName;
    })
