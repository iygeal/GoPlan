#!/usr/bin/env python3
"""
Test script for saving and retrieving models from the database.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import create_app
from app.db import db
from app.models.user import User
from app.models.location import Location
from app.models.travel_plan import TravelPlan
from app.models.dashboard import Dashboard
from app.models.search_history import SearchHistory

# Initialize the Flask app and DB context
app = create_app()

with app.app_context():
    # Test User creation
    user = User(
        username="testuser",
        email="testuser@example.com",
        password="hashedpassword",
        first_name="Test",
        last_name="User"
    )
    user.save()  # Save the user to the database

    # Test Location creation
    location = Location(
        name="Paris",
        latitude=48.8566,
        longitude=2.3522,
        country="France",
        description="The capital city of France."
    )
    location.save()  # Save the location to the database

    # Test Travel Plan creation
    travel_plan = TravelPlan(
        user_id=user.id,
        location_id=location.id,
        start_date="2024-10-22",
        end_date="2024-10-28",
        activities="Visit Eiffel Tower, Louvre Museum.",
        budget=1500.00
    )
    travel_plan.save()  # Save the travel plan to the database

    # Test Dashboard creation
    dashboard = Dashboard(
        user_id=user.id,
        travel_plan_id=travel_plan.id
    )
    dashboard.save()  # Save the dashboard to the database

    # Test Search History creation
    search_history = SearchHistory(
        user_id=user.id,
        search_query="Best places to visit in Paris"
    )
    search_history.save()  # Save search history to the database

    # Fetch and print data to verify persistence
    saved_user = User.query.filter_by(username="testuser").first()
    print(f"User retrieved: {saved_user}")

    saved_location = Location.query.filter_by(name="Paris").first()
    print(f"Location retrieved: {saved_location}")

    saved_travel_plan = TravelPlan.query.filter_by(user_id=user.id).first()
    print(f"TravelPlan retrieved: {saved_travel_plan}")

    saved_dashboard = Dashboard.query.filter_by(user_id=user.id).first()
    print(f"Dashboard retrieved: {saved_dashboard}")

    saved_search_history = SearchHistory.query.filter_by(
        user_id=user.id).first()
    print(f"SearchHistory retrieved: {saved_search_history}")
