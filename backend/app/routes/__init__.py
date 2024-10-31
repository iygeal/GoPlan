#!/usr/bin/env python3
"""
Blueprint registration for the GoPlan API routes.
"""

from flask import Blueprint
from app.error_handlers import handle_error

# Create the blueprint for the API routes
app_views = Blueprint("app_views", __name__, url_prefix="/api")

from app.routes.users import *  # noqa
from app.routes.travel_plans import *  # noqa
from app.routes.dashboards import *  # noqa


def init_app(app):
    """Attach error handlers and blueprints to the Flask app."""
    app.register_error_handler(
        Exception, handle_error)  # Register the global error handler
    # Register the app_views blueprint
    app.register_blueprint(app_views)
