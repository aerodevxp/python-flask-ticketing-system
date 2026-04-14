from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db, login_manager
from app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

root_bp = Blueprint("root", __name__, url_prefix="")

@root_bp.route("/")
def gotoevents():
    print("bigpoe")
    return redirect(url_for("event.index"))