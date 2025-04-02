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


<!-- si occupa di  andare a capo in textarea ingredienti  -->
document.querySelector("textarea[name='ingredienti']").addEventListener("blur", function () {
    document.querySelector(".testo-ingredienti").textContent = this.value;
});


document.querySelector("textarea[name='steps']").addEventListener("blur", function () {
    document.querySelector(".testo-steps").textContent = this.value;
});

<!-- ====================== -->

