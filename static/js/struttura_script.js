        document.getElementById("runButton0").onclick = function() {
            fetch("/run_script")
            .then(response => response.text())
            .then(data => {alert("si giusto")
            });
        };

        // gestisce tasto elenco ricette su HomePage
        document.getElementById("runButton1").onclick = function(){
            fetch("/elenco_ricette") // Effettua la richiesta GET all'endpoint
                .then(response => response.json())  // Parsifica la risposta JSON
                .then(data => {
            // Creiamo una nuova finestra per visualizzare i dati delle ricette
                    const newWindow = window.open();
                    data.forEach(ricetta => { // Loop su ogni ricetta
                    newWindow.document.write(`
                    <h1>${ricetta.nome_ricetta}</h1>
                `);
            });
            newWindow.document.close();
            })
                .catch(error => console.error('Errore:', error)); // Gestione degli errori
        };

        // gestisce barra di ricerca e  tasto search su homePage
        document.getElementById("search-button").onclick = function(){ //quando premi il pulsante fai function
            const cercaRicetta = document.getElementById("search-input").value; //prendi il valore dell`input
            if (!cercaRicetta){
                alert("inserisci una ricetta")
            }
            else{
            fetch("/trova_ricetta?nome_ricetta=" + cercaRicetta) // passa il valore come parametro nella richiesta a python
                .then(response => response.json())
                .then(data => {
                    if (data.detail){
                        alert(`${data.detail}`)
                    }else{
                        const newWindow = window.open();
                        newWindow.document.write(`
                        <h1>${data.nome_ricetta}</h1>
                        <p>${data.ingredienti}</p>
                        <p>${data.kcal}</p>
                        `)};
                        newWindow.document.close();
                    })
                .catch(error => console.error("Errore:", error))};
                document.getElementById("search-input").value = ""; //refresh alla barra di ricerca
        };

// ===========================================================================================================================
// questa parte non viene usata

        // gestisce aggiungi categoria su lista ricette per admin
        document.getElementById("creaCategoria").onclick = function(){ //quando premi il pulsante fai function
            const categoria = document.getElementById("inputCategoria").value; //prendi il valore dell`input
            if (!categoria){
                alert("inserisci una categoria")
            }
            else{
            fetch("/aggiungi_categoria?nome_categoria=" + categoria) // passa il valore come parametro nella richiesta a python
                .then(response => response.json())
                .then(data => {
                    if (data.alert){alert(`${data.alert}`)}
                    else { alert(`${data.errore}`)}
                    })
                .catch(error => console.error("Errore:", error))};
                document.getElementById("inputCategoria").value = ""; //refresh alla barra di ricerca
        };


        // gestisce i tasti elimina per ogni ricetta sulla tabella
        document.addEventListener("DOMContentLoaded", function () {
            document.querySelectorAll(".elimina-ricetta").forEach(button => {
                button.addEventListener("click", function () {
                    const idRicetta = this.getAttribute("data-id");  
                    
                    if (!confirm("Sei sicuro di voler eliminare questa ricetta?")) return;
        
                    fetch("/delete_recipe", {
                        method: "DELETE",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({ id: idRicetta })  // ✅ Mandiamo i dati nel body (JSON)
                    })
                    .then(response => {
                        if (response.ok) {
                            alert("Ricetta eliminata con successo!");
                            location.reload();  
                        } else {
                            alert("Errore nell'eliminazione della ricetta.");
                        }
                    })
                    .catch(error => console.error("Errore nella richiesta:", error));
                });
            });
        });
        
       
        
        
