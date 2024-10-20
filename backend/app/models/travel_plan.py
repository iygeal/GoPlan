#!/usr/bin/env python3
"""
contains travel plan that inherits from the basemodel
"""

from app.db import db
from app.models.base_model import BaseModel


class TravelPlan(BaseModel):
    """Travel Plan model for the application.
    """

    __tablename__ = 'travel_plans'

    user_id = db.Column(db.String(60), db.ForeignKey(
        'users.id'), nullable=False)
    location_id = db.Column(db.String(60), db.ForeignKey(
        'locations.id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    activities = db.Column(db.Text, nullable=True)
    budget = db.Column(db.Float, nullable=True)
    accommodation_details = db.Column(db.Text, nullable=True)

    # Relationships
    user = db.relationship('User', back_populates='travel_plans')
    location = db.relationship('Location', back_populates='travel_plans')

    def __repr__(self):
        return f'<TravelPlan {self.id}: {self.user.username} to {self.location.name}>'
