// Sélectionnez l'élément <ul> dans le DOM avec l'ID "list_movies"
const movieList = document.getElementById("list_movies");

// URL de l'API Star Wars pour récupérer la liste des films
const apiUrl = "https://swapi-api.hbtn.io/api/films/?format=json";

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
    // Récupérez la liste des films à partir des données JSON
    const films = data.results;

    // Parcourez la liste des films et ajoutez chaque titre à la liste HTML
    films.forEach((film) => {
        const listItem = document.createElement("li");
        listItem.textContent = film.title;
        movieList.appendChild(listItem);
    });
    })
