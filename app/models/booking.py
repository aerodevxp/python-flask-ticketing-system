from app import db
from datetime import datetime

class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    statut = db.Column(db.String(20), default='Confirmed')
    date_reservation = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('bookings', lazy='dynamic'))
    event = db.relationship('Event', backref=db.backref('bookings', lazy='dynamic'))
    
    def __repr__(self):
        return f'<Booking {self.id}>'