from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db, login_manager
from app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    #login page
    if current_user.is_authenticated:
        print('already auth')
        return redirect(url_for("event.index"))
    
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        remember = request.form.get("remember")
        
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.mot_de_passe, password):
            login_user(user, remember=bool(remember))
            flash("Connexion réussie !", "success")
            return redirect(url_for("event.index"))
        else:
            flash("Email ou mot de passe incorrect.", "danger")
    
    return render_template("auth/login.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    #sign up
    if current_user.is_authenticated:
        return redirect(url_for("event.index"))
    
    if request.method == "POST":
        nom = request.form.get("nom")
        email = request.form.get("email")
        password = request.form.get("password")
        role = request.form.get("role", "user")
        
        user_exists = User.query.filter_by(email=email).first()
        if user_exists:
            flash("Cet email est déjà utilisé.", "danger")
            return render_template("auth/register.html")
        
        new_user = User(
            nom=nom,
            email=email,
            mot_de_passe=generate_password_hash(password),
            role=role
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        flash("Compte créé ! Connectez-vous.", "success")
        return redirect(url_for("auth.login"))
    
    return render_template("auth/register.html")

@auth_bp.route("/logout")
@login_required
def logout():
    """Déconnexion."""
    logout_user()
    flash("Vous avez été déconnecté.", "info")
    return redirect(url_for("auth.login"))