
    // document.addEventListener('DOMContentLoaded', function() {
    //     const menuToggle = document.querySelector('.menu-toggle');
    //     const nav = document.querySelector('nav');

    //     menuToggle.addEventListener('click', function() {
    //         nav.classList.toggle('hidden');
    //     });
    // });


document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.querySelector('.menu-toggle');
    const nav = document.querySelector('nav');

    menuToggle.addEventListener('click', function() {
        // gestisce la visibilità del menu trasformando NONE(nascosto) in BLOCK(visibile)
        if (nav.style.display === "none" || nav.style.display === "") {
            nav.style.display = "block";  // Mostra il menu
        } else {
            nav.style.display = "none";  // Nascondi il menu
        }
    });
});

    
function loadSection(section) {
    var content = document.getElementById("content");
    
    switch(section) {
        case "create_recipe":
            content.innerHTML = "<h2>Crea una nuova ricetta</h2><p>Form per inserire una nuova ricetta.</p>";
            break;
        case "read_recipe":
            content.innerHTML = "<h2>Lista Ricette</h2><p>Visualizza tutte le ricette disponibili.</p>";
            break;
        case "update_recipe":
            content.innerHTML = "<h2>Modifica Ricetta</h2><p>Seleziona una ricetta da modificare.</p>";
            break;
        case "delete_recipe":
            content.innerHTML = "<h2>Elimina Ricetta</h2><p>Seleziona una ricetta da eliminare.</p>";
            break;
        default:
            content.innerHTML = "<p>Seleziona un'opzione dal menu.</p>";
    }
}
