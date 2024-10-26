#!/usr/bin/env python3
"""
This module defines the travel plan routes for the GoPlan application.
"""

from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.travel_plan import TravelPlan
from app.models.location import Location
from app.routes import app_views

# Allowed keys for travel plan attributes
ALLOWED_KEYS = {"location_id", "start_date", "end_date",
                "activities", "budget", "accommodation_details"}
REQUIRED_FIELDS = {"location_id", "start_date", "end_date"}


@app_views.route("/travel-plans", methods=["POST"], strict_slashes=False)
@jwt_required()
def create_travel_plan():
    """
    Create a new travel plan for the logged-in user.
    """
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    user_id = get_jwt_identity()
    data = request.get_json()

    # Validate required fields
    if not REQUIRED_FIELDS.issubset(data):
        return jsonify({"error": "Missing required field(s)"}), 400

    location = Location.query.get(data["location_id"])
    if not location:
        return jsonify({"error": "Location not found"}), 404

    # Initialize and save the new travel plan
    travel_plan = TravelPlan(user_id=user_id)
    try:
        for key, value in data.items():
            if key in ALLOWED_KEYS:
                setattr(travel_plan, key, value)
        travel_plan.save()
    except AttributeError:
        return jsonify({"error": "Invalid attribute(s) provided"}), 400

    return jsonify(travel_plan.to_dict()), 201


@app_views.route("/travel-plans", methods=["GET"], strict_slashes=False)
@jwt_required()
def get_travel_plans():
    """Retrieve all travel plans for the logged-in user."""
    user_id = get_jwt_identity()
    travel_plans = TravelPlan.query.filter_by(user_id=user_id).all()
    return jsonify([plan.to_dict() for plan in travel_plans]), 200


@app_views.route(
    "/travel-plans/<string:plan_id>", methods=["GET"], strict_slashes=False)
@jwt_required()
def get_travel_plan(plan_id):
    """Retrieve a specific travel plan by ID."""
    user_id = get_jwt_identity()
    travel_plan = TravelPlan.query.filter_by(
        id=plan_id, user_id=user_id
    ).first()

    if not travel_plan:
        return jsonify({"error": "Travel plan not found"}), 404

    return jsonify(travel_plan.to_dict()), 200


@app_views.route(
    "/travel-plans/<string:plan_id>", methods=["PUT"], strict_slashes=False)
@jwt_required()
def update_travel_plan(plan_id):
    """
    Update an existing travel plan's details for the logged-in user.
    """
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    user_id = get_jwt_identity()
    travel_plan = TravelPlan.query.filter_by(
        id=plan_id, user_id=user_id
    ).first()

    if not travel_plan:
        return jsonify({"error": "Travel plan not found"}), 404

    data = request.get_json()
    try:
        for key, value in data.items():
            if key in ALLOWED_KEYS:
                setattr(travel_plan, key, value)
        travel_plan.save()
    except AttributeError:
        return jsonify({"error": "Invalid attribute(s) provided"}), 400

    return jsonify(travel_plan.to_dict()), 200


@app_views.route("/travel-plans/<string:plan_id>", methods=[
    "DELETE"], strict_slashes=False)
@jwt_required()
def delete_travel_plan(plan_id):
    """
    Delete a specific travel plan for the logged-in user.
    """
    user_id = get_jwt_identity()
    travel_plan = TravelPlan.query.filter_by(
        id=plan_id, user_id=user_id
    ).first()

    if not travel_plan:
        return jsonify({"error": "Travel plan not found"}), 404

    travel_plan.delete()

    return jsonify({"message": "Travel plan deleted successfully"}), 200
