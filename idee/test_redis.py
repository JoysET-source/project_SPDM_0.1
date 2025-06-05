@ricette_routes.route('/')
def home():
    cache_key = "home_ricette"

    # Prova a leggere dalla cache
    cached_data = redis_client.get(cache_key)
    if cached_data:
        try:
            ricette_categoria_unica = pickle.loads(cached_data)
            print("📦 Ricette caricate da Redis.")
            return render_template("struttura.html", ricette_categoria_unica=ricette_categoria_unica)
        except Exception as e:
            print("⚠️ Errore durante il caricamento dalla cache:", e)

    print("🚧 Nessuna cache trovata o errore. Calcolo delle ricette...")

    percent_items_to_show = 0.5
    total_items = Ricetta.query.count()

    if total_items == 0:
        return render_template("struttura.html", ricette=[])

    items_to_show_count = int(total_items * percent_items_to_show)
    ricette_giornaliere = Ricetta.query.filter_by(visibility=True).order_by(func.rand()).limit(items_to_show_count).all()

    check_categorie = set()
    ricette_categoria_unica = []

    for ricetta in ricette_giornaliere:
        if ricetta.categoria not in check_categorie:
            check_categorie.add(ricetta.categoria)
            ricette_categoria_unica.append(ricetta)

    # Log
    print(f"✅ Ricette calcolate: {len(ricette_categoria_unica)}")

    # Salva in Redis per 24 ore
    try:
        redis_client.setex(cache_key, 86400, pickle.dumps(ricette_categoria_unica))
        print("✅ Ricette salvate nella cache Redis.")
    except Exception as e:
        print("❌ Errore nel salvataggio Redis:", e)

    log_access(
        action="visita_home",
        ricetta_vista=None,
        ricetta_id=None
    )

    return render_template("struttura.html", ricette_categoria_unica=ricette_categoria_unica)
