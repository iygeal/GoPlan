#!/usr/bin/env python3
"""
This script populates the database with data from locations_data.json.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # noqa
from app.models.location import Location
from app.models.city import City
from app.models.state import State
from app.db import db
from app import create_app
import json


def load_locations():
    # Load data from the JSON file
    with open('backend/data/locations_data.json') as f:
        data = json.load(f)

    for state_data in data["states"]:
        # Get or create the state
        state = State.query.filter_by(name=state_data["name"]).first()
        if not state:
            state = State(name=state_data["name"])
            db.session.add(state)
            db.session.flush()  # Ensure `state.id` is available

        for city_data in state_data["cities"]:
            # Get or create the city
            city = City.query.filter_by(
                name=city_data["name"], state=state).first()
            if not city:
                city = City(name=city_data["name"], state=state)
                db.session.add(city)
                db.session.flush()  # Ensure `city.id` is available

            for loc_data in city_data["locations"]:
                # Add the location
                location = Location(
                    name=loc_data["name"],
                    latitude=loc_data["latitude"],
                    longitude=loc_data["longitude"],
                    description=loc_data["description"],
                    popular_attractions=loc_data["popular_attractions"],
                    country=loc_data["country"],
                    state=state,
                    city=city
                )
                db.session.add(location)

    # Commit all changes
    db.session.commit()
    print("Database has been populated with locations data.")


if __name__ == "__main__":
    # Initialize the Flask app context
    app = create_app()
    with app.app_context():
        load_locations()
