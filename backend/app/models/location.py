#!/usr/bin/env python3
"""
contains location module that inherits from BaseModel
"""

from app.db import db
from app.models.base_model import BaseModel


class Location(BaseModel):
    """Location model for the application.
    """

    __tablename__ = 'locations'

    name = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
    country = db.Column(db.String(100), nullable=False)
    popular_attractions = db.Column(db.Text, nullable=True)

    # Relationship
    travel_plans = db.relationship('TravelPlan', back_populates='location')

    def __repr__(self):
        return f'<Location {self.name}, {self.country}>'
