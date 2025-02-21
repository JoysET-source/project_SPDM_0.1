from flask import Blueprint, render_template

dashboard_routes = Blueprint("dashboard_routes", __name__)

@dashboard_routes.route("/admin_dashboard", methods=["GET", "POST"])
def admin_dashboard():
    return render_template("dashboard/admin_dashboard.html")

@dashboard_routes.route("/create_recipe", methods=["GET", "POST"])
def create_recipe():
    return render_template("dashboard/create_recipe.html")

@dashboard_routes.route("/read_recipe", methods=["GET"])
def read_recipe():
    return render_template("dashboard/read_recipe.html")

@dashboard_routes.route("/update_recipe", methods=["GET","POST"])
def update_recipe():
    return render_template("dashboard/update_recipe.html")

@dashboard_routes.route("/delete_recipe", methods=["GET", "POST"])
def delete_recipe():
    return render_template("dashboard/delete_recipe.html")