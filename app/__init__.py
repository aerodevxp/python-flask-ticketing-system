from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app(config_class="app.config.DevelopmentConfig"):
    #Creation de linstance de Flask
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"  # Route de connexion

    @login_manager.user_loader #how is the manager going to load users from db
    def load_user(user_id):
        from app.models.user import User
        return User.query.get(int(user_id))

    #Importing our routes
    from app.routes.auth_routes import auth_bp
    from app.routes.event_routes import event_bp
    from app.routes.booking_routes import booking_bp
    from app.routes.user_routes import user_bp
    from app.routes.root_routes import root_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(event_bp, url_prefix="/events")
    app.register_blueprint(booking_bp, url_prefix="/bookings")
    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(root_bp, url_prefix="/")

    return app