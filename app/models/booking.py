from app import db
from datetime import datetime

class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id', ondelete='CASCADE'), nullable=True)  # ← AJOUTE ondelete='CASCADE'
    statut = db.Column(db.String(20), default='confirmé')
    date_reservation = db.Column(db.DateTime, default=datetime.utcnow)
    

    user = db.relationship('User', backref=db.backref('bookings', lazy='dynamic'))
    event = db.relationship('Event', backref=db.backref('bookings', lazy='dynamic'))
    
    def __repr__(self):
        return f'<Booking {self.id}>'