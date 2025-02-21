from flask import Blueprint, render_template

dashboard_routes = Blueprint("dashboard_routes", __name__)

@dashboard_routes.route("/admin_dashboard")
def admin_dashboard():
    return render_template("dashboard/admin_dashboard.html")

@dashboard_routes.route("/create_recipe", methods=["GET", "POST"])
def create_recipe():
    return render_template("dashboard/ricette/create_recipe.html")

@dashboard_routes.route("/read_recipe", methods=["GET"])
def read_recipe():
    return render_template("dashboard/ricette/read_recipe.html")

@dashboard_routes.route("/update_recipe", methods=["GET","POST"])
def update_recipe():
    return render_template("dashboard/ricette/update_recipe.html")

@dashboard_routes.route("/delete_recipe", methods=["GET", "POST"])
def delete_recipe():
    return render_template("dashboard/ricette/delete_recipe.html")

@dashboard_routes.route("/footer")
def footer():
    return render_template("dashboard/footer.html")

@dashboard_routes.route("/header")
def header():
    return render_template("dashboard/header.html")