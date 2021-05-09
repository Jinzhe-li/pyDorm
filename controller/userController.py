import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('userController', __name__, url_prefix='/user')


@bp.route('/viewMain', methods=['POST', 'GET'])
def viewMain():
    return render_template("main.html")


@bp.route('/login', methods=['POST', 'GET'])
def login():
    return redirect(url_for("userController.viewMain"))


@bp.route('/viewRegister', methods=['POST', 'GET'])
def viewRegister():
    return render_template("register.html")


@bp.route('/register', methods=['POST', 'GET'])
def register():
    return redirect(url_for("userController.viewMain"))


@bp.route('/updateUserMessage', methods=['POST', 'GET'])
def updateUserMessage():
    return render_template("updateUserMessage.html")


@bp.route('/pushmydata', methods=['POST', 'GET'])
def pushmydata():
    return render_template("pushMyData.html")


