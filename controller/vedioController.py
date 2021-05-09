import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('vedioController', __name__, url_prefix='/vedio')


@bp.route("/viewvedio", methods=['GET', 'POST'])
def viewVedio():
    return render_template("vedio.html")
