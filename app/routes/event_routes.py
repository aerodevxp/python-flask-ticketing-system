
from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, current_user
from app import db
from app.models.event import Event
from app.models.booking import Booking
from datetime import datetime

event_bp = Blueprint("event", __name__, url_prefix="/events")

@event_bp.route("/")
@event_bp.route("/index")
def index():
    #list all events
    events = Event.query.order_by(Event.date.desc()).all()
    return render_template("events/index.html", events=events)

@event_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    #creation of event from admin account
    if current_user.role != "admin":
        flash("Accès refusé.", "danger")
        return redirect(url_for("event.index"))
    
    if request.method == "POST":
        titre = request.form.get("titre")
        date = request.form.get("date")
        description = request.form.get("description")
        capacite = request.form.get("capacite")
        categorie = request.form.get("categorie")
        
        new_event = Event(
            titre=titre,
            date=datetime.strptime(date, "%Y-%m-%dT%H:%M"),
            description=description,
            capacite=int(capacite),
            categorie=categorie
        )
        
        db.session.add(new_event)
        db.session.commit()
        
        flash("Événement créé !", "success")
        return redirect(url_for("event.index"))
    
    return render_template("events/create.html")

@event_bp.route("/view/<int:id>")
def view(id):
    #view details of an event
    event = Event.query.get_or_404(id)
    reservations = Booking.query.filter_by(event_id=id).all()
    places_dispo = event.capacite - len(reservations)
    
    return render_template("events/view.html", event=event, places_dispo=places_dispo)

@event_bp.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit(id):
    #event mod with admin account
    event = Event.query.get_or_404(id)
    
    if current_user.role != "admin":
        abort(403)
    
    if request.method == "POST":
        event.titre = request.form.get("titre")
        event.date = datetime.strptime(request.form.get("date"), "%Y-%m-%d")
        event.description = request.form.get("description")
        event.capacite = int(request.form.get("capacite"))
        event.categorie = request.form.get("categorie")
        
        db.session.commit()
        
        flash("Événement modifié !", "success")
        return redirect(url_for("event.view", id=id))
    
    return render_template("events/edit.html", event=event)

@event_bp.route("/delete/<int:id>", methods=["POST"])
@login_required
def delete(id):
    #event del with admin account
    event = Event.query.get_or_404(id)
    
    if current_user.role != "admin":
        flash("Accès refusé.", "danger")
        return redirect(url_for("event.index"))
    
    db.session.delete(event)
    db.session.commit()
    
    flash("Événement supprimé !", "success")
    return redirect(url_for("event.index"))