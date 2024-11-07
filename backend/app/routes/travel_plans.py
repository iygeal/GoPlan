#!/usr/bin/env python3
"""
This module defines the travel plan routes for the GoPlan application.
"""

from flask import request, jsonify
from flasgger.utils import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.travel_plan import TravelPlan
from app.models.dashboard import Dashboard
from app.routes import app_views

# Allowed keys for travel plan attributes
ALLOWED_KEYS = {"title", "state", "city", "start_date", "end_date",
                "activities", "budget", "accommodation_details"}
REQUIRED_FIELDS = {"title", "state", "city", "start_date", "end_date"}


@app_views.route("/travel-plans", methods=["POST"], strict_slashes=False)
@jwt_required()
@swag_from("../../docs/travel_plans/create_travel_plan.yaml")
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

    # Check for any unexpected keys
    unexpected_keys = set(data) - ALLOWED_KEYS
    if unexpected_keys:
        return jsonify({
            "error": f"Unexpected field(s): {', '.join(unexpected_keys)}"
        }), 400

    # Initialize and save the new travel plan
    travel_plan = TravelPlan(user_id=user_id)
    try:
        for key, value in data.items():
            if key in ALLOWED_KEYS:
                setattr(travel_plan, key, value)
        travel_plan.save()

        # Link to Dashboard
        dashboard_entry = Dashboard(
            user_id=user_id, travel_plan_id=travel_plan.id)
        dashboard_entry.save()
    except Exception:
        return jsonify(
            {"error": "An error occurred while saving the travel plan"}), 400

    return jsonify(travel_plan.to_dict()), 201


@app_views.route("/travel-plans", methods=["GET"], strict_slashes=False)
@jwt_required()
@swag_from("../../docs/travel_plans/get_travel_plans.yaml")
def get_travel_plans():
    """Retrieve all travel plans for the logged-in user."""
    user_id = get_jwt_identity()
    travel_plans = TravelPlan.query.filter_by(user_id=user_id).all()
    return jsonify([plan.to_dict() for plan in travel_plans]), 200


@app_views.route("/travel-plans/<string:plan_id>", methods=[
    "GET"], strict_slashes=False)
@jwt_required()
@swag_from("../../docs/travel_plans/get_travel_plan.yaml")
def get_travel_plan(plan_id):
    """Retrieve a specific travel plan by ID."""
    user_id = get_jwt_identity()
    travel_plan = TravelPlan.query.filter_by(
        id=plan_id, user_id=user_id).first()

    if not travel_plan:
        return jsonify({"error": "Travel plan not found"}), 404

    return jsonify(travel_plan.to_dict()), 200


@app_views.route("/travel-plans/<string:plan_id>", methods=[
    "PUT"], strict_slashes=False)
@jwt_required()
@swag_from("../../docs/travel_plans/update_travel_plan.yaml")
def update_travel_plan(plan_id):
    """
    Update an existing travel plan's details for the logged-in user.
    """
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    user_id = get_jwt_identity()
    travel_plan = TravelPlan.query.filter_by(
        id=plan_id, user_id=user_id).first()

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
@swag_from("../../docs/travel_plans/delete_travel_plan.yaml")
def delete_travel_plan(plan_id):
    """
    Delete a specific travel plan for the logged-in user.
    """
    user_id = get_jwt_identity()
    travel_plan = TravelPlan.query.filter_by(
        id=plan_id, user_id=user_id).first()

    if not travel_plan:
        return jsonify({"error": "Travel plan not found"}), 404

    # First, remove the corresponding entry from the dashboard
    dashboard_entry = Dashboard.query.filter_by(
        user_id=user_id, travel_plan_id=plan_id).first()
    if dashboard_entry:
        dashboard_entry.delete()

    # Now, delete the travel plan
    travel_plan.delete()

    return jsonify({"message": "Travel plan deleted successfully"}), 200
