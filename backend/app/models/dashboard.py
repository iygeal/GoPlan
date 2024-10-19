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

    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    travel_plan_id = db.Column(db.String(60), db.ForeignKey('travel_plans.id'), nullable=False)

    # Relationships
    user = db.relationship('User', back_populates='dashboards')
    travel_plan = db.relationship('TravelPlan', back_populates='dashboards')

    def __repr__(self):
        return f'<Dashboard {self.id}: User {self.user.username}, Plan {self.travel_plan.id}>'
