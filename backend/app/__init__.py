#!/usr/bin/env python3
"""
This module initializes the Flask app and sets up the database connection
using SQLAlchemy and Flask-Migrate for handling database migrations.
"""

from flask import Flask
from app.db import db
from config import config
from flask_migrate import Migrate

from app.models.user import User
from app.models.travel_plan import TravelPlan
from app.models.search_history import SearchHistory
from app.models.dashboard import Dashboard
from app.models.location import Location


def create_app():
    """Create and configure the Flask app."""
    app = Flask(__name__)

    # Configure the app with settings from the config instance
    app.config.from_object(config)

    # Initialize the database connection
    db.init_app(app)

    # Set up Flask-Migrate
    migrate = Migrate(app, db)

    return app
