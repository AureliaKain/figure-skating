from flask import Blueprint, session
from flask import render_template
from flask import request
from flask import url_for
import os

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    if not session.get('logged_in'):
        return render_template('main/index.html')
    else:
        return "Hello Boss! <a href=/logout>Logout</a>"


@bp.route("/figures-list")
def figures_list():
        return render_template('main/figures_list.html')


@bp.route("/figures-list")
def add_figures():
    if not session.get('logged_in'):
        return render_template('main/login.html')
    else:
        pass

@bp.route("/profile")
@login_required
def profile():
    return render_template('main/profile.html')


#if __name__ == "__main__":
    #bp.secret_key = os.urandom(12)
    #bp.run(debug=True, host='0.0.0.0', port=4000)
