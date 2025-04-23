"""
Expose all SQLAlchemy models in one place so you can simply do:
    from models import db, User, Machine, Rental
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import order matters only for type checkers, not at runtime
from .user import User          # noqa: E402,F401
from .machine import Machine    # noqa: E402,F401
from .rental import Rental      # noqa: E402,F401

__all__ = ["db", "User", "Machine", "Rental"]
