document.addEventListener('DOMContentLoaded', function () {
// Sélectionnez l'élément <div> dans le DOM avec l'ID "hello"
const helloElement = document.getElementById("hello");

// URL de l'API pour obtenir le texte "hello" en français
const apiUrl = "https://hellosalut.stefanbohacek.dev/?lang=fr";

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
    // Affichez le texte "hello" dans l'élément HTML avec l'ID "hello"
    const translation = data.hello;
    helloElement.textContent = translation;
    })
});
