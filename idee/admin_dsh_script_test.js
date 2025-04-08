// // window.toggleMenu = function() {
// //     // console.log("toggleMenu chiamato!");
// //     var menu = document.getElementById("menu");
// //     menu.classList.toggle("hidden");
// // }
//
// window.toggleMenu = function () {
//     // console.log("toggleMenu chiamato!");
//     var menu = document.getElementById("menu");
//
//     if (menu.classList.contains("hidden")) {
//         menu.classList.remove("hidden");
//         menu.style.display = "block"; // 👈 Forza la visualizzazione
//     } else {
//         menu.classList.add("hidden");
//         menu.style.display = "none"; // 👈 Nasconde di nuovo
//     }
// };
//
//
// function loadSection(section) {
//     var content = document.getElementById("content");
//
//     switch(section) {
//         case "create_recipe":
//             content.innerHTML = "<h2>Crea una nuova ricetta</h2><p>Form per inserire una nuova ricetta.</p>";
//             break;
//         case "read_recipe":
//             content.innerHTML = "<h2>Lista Ricette</h2><p>Visualizza tutte le ricette disponibili.</p>";
//             break;
//         case "update_recipe":
//             content.innerHTML = "<h2>Modifica Ricetta</h2><p>Seleziona una ricetta da modificare.</p>";
//             break;
//         case "delete_recipe":
//             content.innerHTML = "<h2>Elimina Ricetta</h2><p>Seleziona una ricetta da eliminare.</p>";
//             break;
//         default:
//             content.innerHTML = "<p>Seleziona un'opzione dal menu.</p>";
//     }
// }
//
//
// // document.addEventListener("DOMContentLoaded", function () {
// //     console.log("DOM caricato!");
//
// //     var toggleButton = document.querySelector(".menu-toggle");
//
// //     if (toggleButton) {
// //         console.log("Elemento .menu-toggle trovato!");
// //         toggleButton.addEventListener("click", function () {
// //             console.log("Menu cliccato!");
// //             toggleMenu();
// //         });
// //     } else {
// //         console.log("Elemento .menu-toggle NON trovato!");
// //     }
// // });
