import sqlite3

from flask import Blueprint, session
from flask import render_template
from flask import url_for
import os

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint("main", __name__)


@bp.route("/")
#fix the case logged/not logged
def index():
    if not session.get('logged_in'):
        return render_template('main/index.html')
    else:
        return "Hello Boss! <a href=/logout>Logout</a>"


@bp.route("/figures_list/")
def figures_list_auto():
    figures = get_db().cursor().execute("SELECT * FROM figure").fetchall()
    return render_template("main/figures_list.html", figures=figures)


@bp.route("/profile")
@login_required
def profile():
    return render_template('main/profile.html')

#if __name__ == "__main__":
    #bp.secret_key = os.urandom(12)


