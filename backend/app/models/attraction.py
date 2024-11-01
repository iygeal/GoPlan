#!/usr/bin/env python3
"""
Model representing tourist attractions, landmarks, and points of interest
"""
from app.db import db
from app.models.base_model import BaseModel


class Attraction(BaseModel):
    __tablename__ = 'attractions'
    name = db.Column(db.String(100), nullable=False)

    # Foreign keys
    city_id = db.Column(db.String(60), db.ForeignKey('cities.id'),
                        nullable=False)

    type_id = db.Column(db.String(50), db.ForeignKey('attraction_types.id'),
                        nullable=False)
    # Relationships
    city = db.relationship('City', back_populates='attractions')
    attr_type = db.relationship('AttractionType', back_populates='attractions')

    def __repr__(self):
        """String representation of Attraction."""
        name = self.name
        attraction_type = self.attraction_type.name
        city = self.city.name
        return f"<Attraction {name}, Type: {attraction_type}, City: {city}>"
