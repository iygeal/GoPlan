#!/usr/bin/env python3
"""Dashboard routes to get a user's travel plans"""
from flask import jsonify, abort, request
from app.models.user import User
from app.models.dashboard import Dashboard
from app.models.travel_plan import TravelPlan
from app.routes import app_views
from flask_jwt_extended import jwt_required

# GET DASHBOARD (Retrieve user's travel plans)


@app_views.route(
    '/dashboard/<user_id>', methods=['GET'], strict_slashes=False)
@jwt_required()
def get_dashboard(user_id):
    """Fetch all travel plans for a given user"""
    # Get user by ID
    user = User.query.get(user_id)
    if not user:
        abort(404, description="User not found")

    try:
        # Fetch all dashboard entries (travel plans linked to the user)
        dashboard_entries = Dashboard.query.filter_by(user_id=user_id).all()

        if not dashboard_entries:
            return jsonify(
                {"message": "No travel plans found for this user"}), 200

        # Collect travel plan details
        travel_plans_list = []
        for entry in dashboard_entries:
            travel_plan = entry.travel_plan
            travel_plans_list.append(travel_plan.to_dict())

        # Return JSON response
        return jsonify({
            "user_id": user_id,
            "travel_plans": travel_plans_list
        }), 200

    except Exception as e:
        abort(500, description=str(e))
