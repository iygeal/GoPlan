#!/usr/bin/env python3
"""
This module contains the State model, which represents a state for GoPlan.
"""


from app.db import db
from app.models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a state for GoPlan.

    Attributes:
        name (str): The name of the state.
        cities (list[City]): The cities in the state.
    """

    __tablename__ = 'states'
    name = db.Column(db.String(100), nullable=False, unique=True)

    # Relationships
    cities = db.relationship('City', back_populates='state')

    def __repr__(self):
        return f'<State {self.name}>'
