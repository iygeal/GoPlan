#!/usr/bin/env python3
"""
This module contains the TravelPlan model that inherits from BaseModel.
The TravelPlan model represents a user's plan to travel to a specific location
with a given budget and activities.
"""

from app.db import db
from app.models.base_model import BaseModel


class TravelPlan(BaseModel):
    """
    Represents a travel plan for a user, including destination,
    budget, and activities.
    """

    __tablename__ = 'travel_plans'

    user_id = db.Column(db.String(60), db.ForeignKey(
        'users.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(60), nullable=False)
    city = db.Column(db.String(60), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    activities = db.Column(db.Text, nullable=True)
    budget = db.Column(db.Float, nullable=True)
    accommodation_details = db.Column(db.Text, nullable=True)

    # Relationships
    user = db.relationship('User', back_populates='travel_plans')

    # Relationship with Dashboard
    dashboards = db.relationship('Dashboard', back_populates='travel_plan')

    def __repr__(self):
        """
        Returns a string representation of the travel plan instance.
        """
        return (f'<TravelPlan {self.id}: User {self.user_id} - '
                f'Title {self.title}, Destination {self.city}, {self.state}>')
