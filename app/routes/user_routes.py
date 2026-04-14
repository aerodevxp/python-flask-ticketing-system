#!/usr/bin/env python3
from flask import Blueprint, render_template, redirect, url_for, flash, abort, request
from flask_login import login_required, current_user
from app import db, login_manager
from app.models.booking import Booking
from app.models.event import Event

user_bp = Blueprint("user", __name__, url_prefix="/user")

@user_bp.route("/dashboard")
@login_required
def dashboard():
    #role dependent dashboard
    if current_user.role == "admin":
        return render_admin_dashboard()
    return render_user_dashboard()

def render_user_dashboard():
    #user
    bookings = Booking.query.filter_by(user_id=current_user.id, statut="confirmé").all()
    return render_template("user/dashboard_user.html", bookings=bookings)

def render_admin_dashboard():
    #admin
    events = Event.query.all()
    all_bookings = Booking.query.all()
    return render_template("user/dashboard_admin.html", events=events, all_bookings=all_bookings)

@user_bp.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    #change name
    if request.method == "POST":
        nom = request.form.get("nom")
        current_user.nom = nom
        db.session.commit()
        flash("Profil modifié !", "success")
        return redirect(url_for("user.profile"))
    
    return render_template("user/profile.html", user=current_user)