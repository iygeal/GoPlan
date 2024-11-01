#!/usr/bin/env python3
"""Insert Nigerian states into the database."""

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

    # Create a session
    with db.session.begin():
        for state_name in states:
            state = State(name=state_name)
            db.session.add(state)
    
    # Commit the session
    db.session.commit()
    print("States have been inserted successfully!")

if __name__ == "__main__":
    insert_states()
