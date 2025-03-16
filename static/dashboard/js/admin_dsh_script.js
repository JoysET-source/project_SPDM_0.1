
// crea il menu a barre
document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.querySelector('.menu-toggle');
    const nav = document.querySelector('nav');

// gestisce la visibilità del menu trasformando NONE(nascosto) in BLOCK(visibile)
    menuToggle.addEventListener('click', function() {        
        if (nav.style.display === "none" || nav.style.display === "") {
            nav.style.display = "block";  // Mostra il menu
        } else {
            nav.style.display = "none";  // Nascondi il menu
        }
    });
});

// script per inizializzare editor di testo Quill
document.addEventListener("DOMContentLoaded", function () {
    // // Inizializzare Quill per Descrizione
    // const quillDescrizione = new Quill('#editorDescrizione', {
    //     theme: "snow"
    // });

    // Inizializzare Quill per Ingredienti
    const quillIngredienti = new Quill('#editorIngredienti', {
        theme: "snow"
    });

    // Inizializzare Quill per Steps
    const quillSteps = new Quill('#editorSteps', {
        theme: "snow"
    });

    // Mandare il contenuto del Quill al backend quando il form viene inviato
    document.querySelector("form").addEventListener("submit", function (event) {
        // Impedire che il form venga inviato prima di aggiornare i campi nascosti
        event.preventDefault();

        // Aggiornare i campi nascosti con il contenuto degli editor Quill
        // document.querySelector("#hiddenDescrizione").value = quillDescrizione.root.innerHTML;
        document.querySelector("#hiddenIngredienti").value = quillIngredienti.root.innerHTML;
        document.querySelector("#hiddenSteps").value = quillSteps.root.innerHTML;

        // Invia il form dopo aver aggiornato i campi nascosti
        this.submit();
    });
});



