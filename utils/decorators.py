from functools import wraps
from flask import url_for
from werkzeug.utils import redirect

from flask import session


def login_required(f):
    @wraps(f)
    def login(*args, **kwargs):
        if session.get("admin", "None") is None:
            return redirect(url_for("admin_login"))
        return f(*args, **kwargs)
    return login


def is_user_already_logged_in(f):
    @wraps(f)
    def is_user_logged_in(*args, **kwargs):
        if session.get("admin"):
            return redirect(url_for("home"))
        return f(*args, **kwargs)
    return is_user_logged_in


def is_admin(f):
    @wraps(f)
    def admin(*args, **kwargs):
        if not session.get("admin"):
            return redirect(url_for("home"))
        return f(*args, **kwargs)
    return admin