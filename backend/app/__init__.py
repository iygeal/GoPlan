#!/usr/bin/env python3
"""
This module initializes the Flask app and sets up the database connection
using SQLAlchemy.
"""

from flask import Flask
from app.db import db
from config import config


def create_app():
    """Create and configure the Flask app."""
    app = Flask(__name__)

    # Configure the app with settings from the config instance
    app.config.from_object(config)

    # Initialize the database connection
    db.init_app(app)

    return app
