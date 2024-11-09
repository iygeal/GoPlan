#!/usr/bin/env python3
"""
This module defines the dashboard routes for the GoPlan application.
"""

from flask import jsonify
from flasgger.utils import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.dashboard import Dashboard
from app.models.travel_plan import TravelPlan
from app.routes import app_views


@app_views.route("/dashboard", methods=["GET"], strict_slashes=False)
@jwt_required()
@swag_from("../../docs/dashboards/get_dashboard.yaml")
def get_dashboard():
    """
    Retrieve all travel plans for the logged-in user's dashboard.
    """
    user_id = get_jwt_identity()
    dashboard_entries = Dashboard.query.filter_by(user_id=user_id).all()
    travel_plans = [entry.travel_plan.to_dict() for entry in dashboard_entries]
    return jsonify(travel_plans), 200


@app_views.route("/dashboard/<string:plan_id>", methods=[
    "DELETE"], strict_slashes=False)
@jwt_required()
@swag_from("../../docs/dashboards/delete_dashboard_entry.yaml")
def delete_dashboard_entry(plan_id):
    """
    Delete a specific travel plan from the user's dashboard.
    """
    user_id = get_jwt_identity()
    dashboard_entry = Dashboard.query.filter_by(
        travel_plan_id=plan_id, user_id=user_id
    ).first()

    if not dashboard_entry:
        return jsonify({"error": "Dashboard entry not found"}), 404

    # Retrieve the associated travel plan separately
    travel_plan = TravelPlan.query.get(plan_id)

    # Delete the dashboard entry first
    dashboard_entry.delete()

    # Then delete the associated travel plan
    if travel_plan:
        travel_plan.delete()

    return jsonify({"message": "Travel plan deleted from dashboard"}), 200
