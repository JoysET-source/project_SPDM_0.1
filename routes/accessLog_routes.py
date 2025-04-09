from flask import Blueprint, request, render_template
from datetime import datetime


from models.accessLog_model import AccessLog
from import_bridge import db

accessLog_routes = Blueprint("accessLog_routes", __name__)


def log_access(
        user_id,
        action,
        details=None,
        ricetta_vista=None,
        ricetta_id=None,
):
    # crea un nuovo log di accesso
    new_log = AccessLog(
            user_id=user_id,
            action=action,
            details=details,
            ricetta_vista=ricetta_vista,
            ricetta_id=ricetta_id,
            country=request.headers.get("X-Country"),
            user_agent=request.headers.get("User-Agent"),
            ip_address=request.remote_addr,
            timestamp=datetime.utcnow()
    )

    # aggiungi il log al database
    db.session.add(new_log)
    db.session.commit()


@accessLog_routes.route("/accessLog", methods=["GET"])
def get_access_logs():

    # prendi tutti i log di accesso dal database
    access_logs = AccessLog.query.all()

    return render_template("dashboard/admin_dashboard.html", access_logs=access_logs)
