// controlla il menu a barre
document.addEventListener('DOMContentLoaded', function () {
    const menuToggle = document.querySelector('.menu-toggle');
    const navMenu = document.getElementById('menu');

    menuToggle.addEventListener('click', function (event) {
        navMenu.classList.toggle('hidden');
        event.stopPropagation(); // Impedisce la propagazione del click al documento
    });

    document.addEventListener('click', function (event) {
        if (!navMenu.classList.contains('hidden') && !navMenu.contains(event.target) && !menuToggle.contains(event.target)) {
            navMenu.classList.add('hidden');
        }
    });
});
// ===================================

<!-- si occupa di andare a capo in textarea ingredienti  -->
// document.querySelector("textarea[name='ingredienti']").addEventListener("blur", function () {
//     document.querySelector(".testo-ingredienti").textContent = this.value;
// });
//
//
// document.querySelector("textarea[name='steps']").addEventListener("blur", function () {
//     document.querySelector(".testo-steps").textContent = this.value;
// });

<!-- ====================== -->

// script per inizializzare editor di testo Quill
// document.addEventListener("DOMContentLoaded", function () {
//
//     // Inizializzare Quill per Ingredienti
//     const quillIngredienti = new Quill('#editorIngredienti', {
//         theme: "snow"
//     });
//
//     // Inizializzare Quill per Steps
//     const quillSteps = new Quill('#editorSteps', {
//         theme: "snow"
//     });

// Mandare il contenuto del Quill al backend quando il form viene inviato
//     document.querySelector("form").addEventListener("submit", function (event) {
//         // Impedire che il form venga inviato prima di aggiornare i campi nascosti
//         event.preventDefault();
//
//         // Aggiornare i campi nascosti con il contenuto degli editor Quill
//         // document.querySelector("#hiddenDescrizione").value = quillDescrizione.root.innerHTML;
//         document.querySelector("#hiddenIngredienti").value = quillIngredienti.root.innerHTML;
//         document.querySelector("#hiddenSteps").value = quillSteps.root.innerHTML;
//
//         // Invia il form dopo aver aggiornato i campi nascosti
//         this.submit();
//     });
// });
//=====================================================================================================================

// script per tinyMCE editor video image text

tinymce.init({
    selector: '.editor',
    plugins: 'image media link lists code',
    toolbar: 'bold italic underline | alignleft aligncenter alignright alignjustify | bullist numlist | image media link | code',
    height: 300,
    menubar: false,
    branding: false
});