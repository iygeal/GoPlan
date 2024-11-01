#!/usr/bin/env python3
"""load datas into the attraction types in database table"""

from app import db
from app.models.attraction_type import AttractionType
from app import create_app

app = create_app()

attraction_types = [
    "Festival", "Cultural", "Historical Site", "Natural Attraction",
    "Amusement Park", "Museum", "Art Gallery", "Religious Site", "Zoo",
    "Botanical Garden", "Beach", "Monument", "Scenic Viewpoint", "Market",
    "Theater", "Sports Venue", "Aquarium", "Mountain", "Park", "Nightlife"
]

with app.app_context():
    for type_name in attraction_types:
        # Check if the attraction type already exists
        if not AttractionType.query.filter_by(name=type_name).first():
            new_type = AttractionType(name=type_name, description=f"{type_name} attraction")
            db.session.add(new_type)
            print(f"Added attraction type: {type_name}")

    # Commit all changes
    db.session.commit()
    print("All attraction types added successfully.")
