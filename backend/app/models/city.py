#!/usr/bin/env python3
"""
Contains a city module
"""
from app.db import db
from app.models.base_model import BaseModel


class City(BaseModel):
    __tablename__ = 'cities'

    name = db.Column(db.String(60), nullable=False)
    state_id = db.Column(db.String(60), db.ForeignKey('states.id'),
                         nullable=False)

    state = db.relationship('State', back_populates='cities')
    attractions = db.relationship('Attraction', back_populates='city')

    def __repr__(self):
        return f'<City {self.name}, State {self.state.name}>'
