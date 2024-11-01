#!/usr/bin/env python3
"""
contains travel plan that inherits from the basemodel
"""

from app.db import db
from app.models.base_model import BaseModel


class TravelPlan(BaseModel):
    """Travel Plan model for the application."""
    __tablename__ = 'travel_plans'

    user_id = db.Column(db.String(60), db.ForeignKey('users.id'),
                        nullable=False)

    state_id = db.Column(db.String(60), db.ForeignKey('states.id'),
                         nullable=False)

    city_id = db.Column(db.String(60), db.ForeignKey('cities.id'),
                         nullable=False)
    dashboard_id = db.Column(db.String(60), db.ForeignKey('dashboards.id'),
                             nullable=False)

    attraction_type_id = db.Column(db.String(60), db.ForeignKey('attraction_types.id'),
                                   nullable=False)

    attraction_id = db.Column(db.String(60), db.ForeignKey('attractions.id'),
                              nullable=False)

    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    activities = db.Column(db.Text, nullable=True)
    budget = db.Column(db.Float, nullable=True)
    accommodation_details = db.Column(db.Text, nullable=True)

    # Relationships
    dashboard = db.relationship('Dashboard', back_populates='travel_plans')
