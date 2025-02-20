document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("register-form").addEventListener("submit", function (event) {
        event.preventDefault();
        
        let formData = new FormData(this);

        fetch("{{ url_for('auth_routes.register') }}", {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("username-error").innerHTML = "";
            document.getElementById("password-error").innerHTML = "";

            if (data.success) {
                alert(data.success);
                window.location.href = "/login";
            } else if (data.errors) {
                if (data.errors.username) {
                    document.getElementById("username-error").innerHTML = data.errors.username.join("<br>");
                }
                if (data.errors.password) {
                    document.getElementById("password-error").innerHTML = data.errors.password.join("<br>");
                }
            }
        })
        .catch(error => console.error("Errore:", error));
    });
});