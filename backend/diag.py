#!/usr/bin/env python3
"""
Diagnostic script to check database content and identify missing entries
"""
from app import db, create_app
from app.models.city import City
from app.models.attraction_type import AttractionType

app = create_app()

def check_database():
    with app.app_context():
        # Check cities
        print("\n=== Checking Cities ===")
        lagos = City.query.filter(City.name.ilike('Lagos')).first()
        if lagos:
            print(f"Found Lagos: {lagos}")
        else:
            print("Lagos not found in database")
            print("\nAvailable cities:")
            cities = City.query.all()
            for city in cities:
                print(f"- {city.name}")

        # Check attraction types
        print("\n=== Checking Attraction Types ===")
        required_types = ['Museum', 'Park', 'Market', 'Religious Site']
        
        print("\nRequired types status:")
        for type_name in required_types:
            # Try exact match first
            attr_type = AttractionType.query.filter_by(name=type_name).first()
            if not attr_type:
                # Try case-insensitive match
                attr_type = AttractionType.query.filter(
                    AttractionType.name.ilike(type_name)
                ).first()
            
            if attr_type:
                print(f"Found: {attr_type.name}")
            else:
                print(f"Missing: {type_name}")

        print("\nAll available attraction types:")
        all_types = AttractionType.query.all()
        for attr_type in all_types:
            print(f"- {attr_type.name}")

if __name__ == "__main__":
    check_database()
