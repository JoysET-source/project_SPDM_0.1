
// controlla il menu a barre

// document.addEventListener('DOMContentLoaded', function() {
//     const menuToggle = document.querySelector('.menu-toggle');
//     const nav = document.querySelector('nav');
//
// // gestisce la visibilità del menu trasformando NONE(nascosto) in BLOCK(visibile)
//     menuToggle.addEventListener('click', function() {
//         if (nav.style.display === "none" || nav.style.display === "") {
//             nav.style.display = "block";  // Mostra il menu
//         } else {
//             nav.style.display = "none";  // Nascondi il menu
//         }
//     });
// });


// controlla il menu a barre
document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.querySelector('.menu-toggle');
    const navMenu = document.getElementById('menu');

    menuToggle.addEventListener('click', function(event) {
        navMenu.classList.toggle('hidden');
        event.stopPropagation(); // Impedisce la propagazione del click al documento
    });

    document.addEventListener('click', function(event) {
        if (!navMenu.classList.contains('hidden') && !navMenu.contains(event.target) && !menuToggle.contains(event.target)) {
            navMenu.classList.add('hidden');
        }
    });
});



