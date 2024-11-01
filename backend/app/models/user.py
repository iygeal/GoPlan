#!/usr/bin/env python3
"""
contains user model that inherits from BaseModel
"""

from app.db import db
from app.models.base_model import BaseModel
import re


class User(BaseModel):
    """User model for the application."""

    __tablename__ = 'users'

    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    profile_picture = db.Column(db.String(255), nullable=True)
    bio = db.Column(db.Text, nullable=True)

    # Relationships
    dashboards = db.relationship('Dashboard', back_populates='user',
                                 cascade='all, delete-orphan')
