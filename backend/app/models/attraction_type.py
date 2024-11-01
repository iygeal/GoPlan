#!/usr/bin/env python3
"""
Model representing types of attractions (e.g., museum, park, monument)
"""
from app.db import db
from app.models.base_model import BaseModel


class AttractionType(BaseModel):
    __tablename__ = 'attraction_types'
    name = db.Column(db.String(60), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)

    # Relationship: One AttractionType can have many Attractions
    attractions = db.relationship(
        'Attraction',
        back_populates='attr_type',
        lazy='dynamic'
    )

    def __repr__(self):
        """String representation of AttractionType"""
        return f'<AttractionType {self.name}>'
