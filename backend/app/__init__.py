#!/usr/bin/env python3
"""
This module initializes the Flask app and sets up the database connection
using SQLAlchemy and Flask-Migrate for handling database migrations.
"""

from flask import Flask
from flasgger import Swagger
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from app.db import db
from config import config, test_config
from flask_migrate import Migrate

# Import all models to help with migrations
from app.models.user import User
from app.models.travel_plan import TravelPlan
from app.models.search_history import SearchHistory
from app.models.dashboard import Dashboard


# Import the route and error handler initializer
from app.routes import init_app


def create_app():
    """Create and configure the Flask app."""
    app = Flask(__name__)

    # Enable CORS for all routes and origins (for development)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Configure the app with settings from the config instance
    app.config.from_object(config or test_config)

    # Initialize the database connection
    db.init_app(app)

    # Set up Flask-Migrate
    migrate = Migrate(app, db)

    # Set up Flask-JWT-Extended
    jwt = JWTManager(app)

    # Initialize routes and error handlers
    init_app(app)

    # Set up Swagger
    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "GoPlan API",
            "description": "API documentation for GoPlan",
            "version": "1.0.0"
        },
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "JWT Authorization header using the Bearer scheme. Example: 'Authorization: Bearer {token}'"
            }
        },
        "security": [
            {"Bearer": []}
        ]
    }

    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec',
                "route": '/apispec.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/"
    }

    swagger = Swagger(app, config=swagger_config, template=swagger_template)

    return app
