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
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    description = db.Column(db.Text, nullable=True)
    popular_attractions = db.Column(db.Text, nullable=True)
    country = db.Column(db.String(100), nullable=False)
    state_id = db.Column(db.String(60), db.ForeignKey(
        'states.id'), nullable=False)
    city_id = db.Column(db.String(60), db.ForeignKey(
        'cities.id'), nullable=False)

    # Relationships
    travel_plans = db.relationship('TravelPlan', back_populates='location')
    state = db.relationship('State', back_populates='locations')
    city = db.relationship('City', back_populates='locations')

    def __repr__(self):
        return f'<Location {self.name}, {self.country}>'
