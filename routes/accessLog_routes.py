from flask import Blueprint, request, render_template
from datetime import datetime
from flask_login import current_user

from models.accessLog_model import AccessLog
from import_bridge import db
from test.geo_location import get_geo_location




accessLog_routes = Blueprint("accessLog_routes", __name__)


def log_access(
        action,
        details=None,
        ricetta_vista=None,
        ricetta_id=None,
):

    if not current_user.is_authenticated:
        user_id = None
    else:
        user_id = current_user.id

    ip_address = request.remote_addr

    country = get_geo_location(ip_address)

    # crea un nuovo log di accesso
    new_log = AccessLog(
            user_id=user_id,
            action=action,
            details=details,
            ricetta_vista=ricetta_vista,
            ricetta_id=ricetta_id,
            country=country,
            user_agent=request.headers.get("User-Agent"),
            ip_address=ip_address,
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
