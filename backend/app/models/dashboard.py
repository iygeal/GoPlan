#!/usr/bin/env python3
"""
contains a dashboard module that inherits from BaseModel
"""

from app.db import db
from app.models.base_model import BaseModel


class Dashboard(BaseModel):
    """Dashboard model for the application.
    """

    __tablename__ = 'dashboards'

    user_id = db.Column(db.String(60), db.ForeignKey('users.id'),
                        nullable=False)
    travel_id = db.Column(db.String(60), db.ForeignKey('travel_plans.id'),
                          nullable=False)
    user = db.relationship('User', back_populates='dashboards')
    travel_plans = db.relationship('TravelPlan', back_populates='dashboard')

    def __repr__(self):
        _id = self.id
        username = self.user.username
        travelPlan_ids = [tp.id for tp in self.travel_plans]
        return f'<Dashboard {_id}: User {username}, Plan {travelPlan_ids}>'
