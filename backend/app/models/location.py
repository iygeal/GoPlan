#!/usr/bin/env python3
"""
Contains the Location model that inherits from BaseModel.
"""

from app.db import db
from app.models.base_model import BaseModel


class Location(BaseModel):
    """
    Represents a location for travel plans, including geographic coordinates
    and details such as country and attractions.
    """

    __tablename__ = 'locations'

    name = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
    country = db.Column(db.String(100), nullable=False)
    popular_attractions = db.Column(db.Text, nullable=True)

    # Relationships
    travel_plans = db.relationship('TravelPlan', back_populates='location')

    def __repr__(self):
        """
        Returns a string representation of the location instance.
        """
        return f'<Location {self.name}, {self.country}>'
