from .auth_routes import auth_bp
from .event_routes import event_bp
from .booking_routes import booking_bp
from .root_routes import root_bp

__all__ = ["auth_bp", "event_bp", "booking_bp", "root_bp"]