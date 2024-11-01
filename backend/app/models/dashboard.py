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
                        nullable=False, unique=True)
    user = db.relationship('User', back_populates='dashboards',
                           uselist=False)
    travel_plans = db.relationship('TravelPlan', back_populates='dashboard')
