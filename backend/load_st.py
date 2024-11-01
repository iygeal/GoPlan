#!/usr/bin/env python3
"""Insert Nigerian states into the database."""
from app import create_app
from app.db import db
from app.models.state import State

def insert_states():
    # List of Nigerian states
    states = [
        "Abia", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi",
        "Bayelsa", "Benue", "Borno", "Cross River", "Delta",
        "Ebonyi", "Edo", "Ekiti", "Enugu", "Gombe",
        "Imo", "Jigawa", "Kaduna", "Kano", "Kogi",
        "Kwara", "Lagos", "Nasarawa", "Niger", "Ogun",
        "Ondo", "Osun", "Oyo", "Plateau", "Rivers",
        "Sokoto", "Taraba", "Yobe", "Zamfara", "FCT"
    ]
    
    try:
        # Create a session within the application context
        app = create_app()
        with app.app_context():
            # Check for existing states to avoid duplicates
            existing_states = {state.name for state in State.query.all()}
            
            for state_name in states:
                if state_name not in existing_states:
                    state = State(name=state_name)
                    db.session.add(state)
            
            # Commit the session
            db.session.commit()
            print("States have been inserted successfully!")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    insert_states()
