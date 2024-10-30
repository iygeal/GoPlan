#!/usr/bin/env python3
"""
This module defines the API endpoints for retrieving and filtering locations.
"""

from flask import jsonify, request
from app.models.location import Location
from app.models.state import State
from app.models.city import City
from app.routes import app_views
from app.db import db


@app_views.route('/locations', methods=['GET'])
def get_locations():
    """
    Retrieve locations with optional filters for state, city,
    and popular attractions.
    Filters can be applied via query parameters:
    - state: Filter by state name
    - city: Filter by city name
    - popular_attraction: Filter by popular attraction substring
    """
    state_name = request.args.get('state')
    city_name = request.args.get('city')
    popular_attraction = request.args.get('popular_attraction')

    # Start with a base query
    query = db.session.query(Location)

    # Filter by state
    if state_name:
        query = query.join(State).filter(State.name.ilike(f"%{state_name}%"))

    # Filter by city
    if city_name:
        query = query.join(City).filter(City.name.ilike(f"%{city_name}%"))

    # Filter by popular attraction
    if popular_attraction:
        query = query.filter(
            Location.popular_attractions.ilike(f"%{popular_attraction}%"))

    # Execute the query
    locations = query.all()
    locations_list = [location.to_dict() for location in locations]

    return jsonify({"success": True, "locations": locations_list}), 200
