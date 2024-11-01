#!/usr/bin/env python3
"""
Load attractions data for Nigerian cities
"""
from app import create_app
from app.db import db
from app.models.city import City
from app.models.attraction_type import AttractionType
from app.models.attraction import Attraction

# Initialize Flask app
app = create_app()

attractions_data = [
    # Museums
    {
        "name": "National War Museum",
        "city_name": "Umuahia",
        "type_name": "Museum"
    },
    {
        "name": "National Museum",
        "city_name": "Lagos",
        "type_name": "Museum"
    },
    {
        "name": "Jos Museum",
        "city_name": "Jos",
        "type_name": "Museum"
    },
    {
        "name": "Benin City National Museum",
        "city_name": "Benin City",
        "type_name": "Museum"
    },
    
    # Parks
    {
        "name": "Yankari Game Reserve",
        "city_name": "Bauchi",
        "type_name": "Park"
    },
    {
        "name": "Obudu Mountain Resort",
        "city_name": "Calabar",
        "type_name": "Park"
    },
    {
        "name": "Lekki Conservation Centre",
        "city_name": "Lagos",
        "type_name": "Park"
    },
    {
        "name": "Gashaka-Gumti National Park",
        "city_name": "Jalingo",
        "type_name": "Park"
    },

    # Historical Sites
    {
        "name": "Sukur Cultural Landscape",
        "city_name": "Madagali",
        "type_name": "Historical Site"
    },
    {
        "name": "Ancient Kano City Walls",
        "city_name": "Kano",
        "type_name": "Historical Site"
    },
    {
        "name": "First Storey Building",
        "city_name": "Badagry",
        "type_name": "Historical Site"
    },
    {
        "name": "Oba Palace",
        "city_name": "Benin City",
        "type_name": "Historical Site"
    },

    # Markets
    {
        "name": "Kurmi Market",
        "city_name": "Kano",
        "type_name": "Market"
    },
    {
        "name": "Lekki Arts & Crafts Market",
        "city_name": "Lagos",
        "type_name": "Market"
    },
    {
        "name": "Oba Market",
        "city_name": "Benin City",
        "type_name": "Market"
    },

    # Religious Sites
    {
        "name": "Central Mosque",
        "city_name": "Kano",
        "type_name": "Religious Site"
    },
    {
        "name": "Cathedral Church of Christ",
        "city_name": "Lagos",
        "type_name": "Religious Site"
    },
    {
        "name": "Great Mosque",
        "city_name": "Ilorin",
        "type_name": "Religious Site"
    }
]

# Use the app context to interact with the database
with app.app_context():
    for attraction_data in attractions_data:
        # Retrieve city and attraction type from the database
        city = City.query.filter_by(name=attraction_data["city_name"]).first()
        attraction_type = AttractionType.query.filter_by(name=attraction_data["type_name"]).first()
        
        if city and attraction_type:
            # Check if attraction already exists
            existing_attraction = Attraction.query.filter_by(
                name=attraction_data["name"],
                city_id=city.id,
                type_id=attraction_type.id
            ).first()
            
            if not existing_attraction:
                # Create new Attraction instance
                attraction = Attraction(
                    name=attraction_data["name"],
                    city_id=city.id,
                    type_id=attraction_type.id
                )
                db.session.add(attraction)
                print(f"Added attraction: {attraction_data['name']} in {attraction_data['city_name']}")
            else:
                print(f"Attraction already exists: {attraction_data['name']}")
        else:
            print(f"Error: City '{attraction_data['city_name']}' or type '{attraction_data['type_name']}' not found")

    # Commit all changes
    try:
        db.session.commit()
        print("All attractions added successfully.")
    except Exception as e:
        db.session.rollback()
        print(f"Error occurred while adding attractions: {str(e)}")
