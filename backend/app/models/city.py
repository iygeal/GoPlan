#!/usr/bin/env python3
"""
This module defines the City model, which represents a city in the GoPlan
application. It inherits from BaseModel and includes relationships to the
State and Location models.
"""

from app.db import db
from app.models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city with a name and an associated state. Each city can
    have multiple locations.

    __tablename__ = 'cities'
        name (str): The name of the city.
        state_id (str): The ID of the associated state.
    """
    name = db.Column(db.String(100), nullable=False)
    state_id = db.Column(db.String(60), db.ForeignKey(
        'states.id'), nullable=False)

    # Relationships
    state = db.relationship('State', back_populates='cities')
    locations = db.relationship('Location', back_populates='city')

    def __repr__(self):
        """
        Returns a string representation of the city instance.
        """
        return f'<City {self.name}, {self.state.name}>'
