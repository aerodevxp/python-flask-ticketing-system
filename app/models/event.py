from app import db
from datetime import datetime

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(150), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text, nullable=True)
    capacite = db.Column(db.Integer, nullable=False)
    categorie = db.Column(db.String(50), nullable=True)
    
    def __repr__(self):
        return f'<Event {self.titre}>'