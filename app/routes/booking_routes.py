#!/usr/bin/env python3
"""Routes de réservation de billets."""

from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, current_user
from app import db
from app.models.booking import Booking
from app.models.event import Event
from datetime import datetime

booking_bp = Blueprint("booking", __name__, url_prefix="/bookings")

@booking_bp.route("/create/<int:event_id>", methods=["GET", "POST"])
@login_required
def create(event_id):
    #booking creation for event id
    event = Event.query.get_or_404(event_id)
    
    # Vérifier places disponibles
    reservations = Booking.query.filter_by(event_id=event_id).all()
    places_utilisees = len(reservations)
    
    if places_utilisees >= event.capacite:
        flash("Plus de places disponibles !", "danger")
        return redirect(url_for("event.view", id=event_id))
    
    # Vérifier si déjà réservé
    existing_booking = Booking.query.filter_by(
        user_id=current_user.id,
        event_id=event_id
    ).first()
    
    if existing_booking:
        flash("Vous avez déjà réservé cet événement !", "warning")
        return redirect(url_for("user.dashboard"))
    
    if request.method == "POST":
        new_booking = Booking(
            user_id=current_user.id,
            event_id=event_id,
            statut="confirmé",
            date_reservation=datetime.utcnow()
        )
        
        db.session.add(new_booking)
        db.session.commit()
        
        flash("Réservation confirmée !", "success")
        return redirect(url_for("user.dashboard"))
    
    return render_template("bookings/create.html", event=event)

@booking_bp.route("/cancel/<int:id>", methods=["POST"])
@login_required
def cancel(id):
    #cancel booking on event id
    booking = Booking.query.get_or_404(id)
    
    if booking.user_id != current_user.id:
        abort(403)
    
    # Libérer la place
    booking.statut = "annulé"
    db.session.commit()
    
    flash("Réservation annulée !", "success")
    return redirect(url_for("user.dashboard"))

@booking_bp.route("/status")
@login_required
def status():
    #see booking status
    bookings = Booking.query.filter_by(user_id=current_user.id).all()
    return render_template("bookings/status.html", bookings=bookings)