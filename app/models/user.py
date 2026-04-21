from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mot_de_passe = db.Column(db.String(255), nullable=True)
    role = db.Column(db.String(20), default='user')
    
    def __repr__(self): #what to return if only the user object is asked for / example: print(user) would be <User EMAIL>
        return f'<User {self.email}>'