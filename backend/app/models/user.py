#!/usr/bin/env python3
"""
This module defines the User model for the GoPlan application.
"""

import bcrypt
import re
from app.db import db
from app.models.base_model import BaseModel


class User(BaseModel):
    """Represents a user in the GoPlan application."""

    __tablename__ = 'users'

    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    profile_picture = db.Column(db.String(255), nullable=True)
    bio = db.Column(db.Text, nullable=True)

    # Relationships
    travel_plans = db.relationship(
        'TravelPlan', back_populates='user', cascade='all, delete-orphan'
    )
    dashboards = db.relationship(
        'Dashboard', back_populates='user', cascade='all, delete-orphan'
    )
    search_histories = db.relationship(
        'SearchHistory', back_populates='user', cascade='all, delete-orphan'
    )

    def validate_email(self):
        """Validates the email format using a regex."""
        email_regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.match(email_regex, self.email):
            raise ValueError(f"Invalid email format: {self.email}")

    def set_password(self, password):
        """Hash and set the user's password."""
        self.password = bcrypt.hashpw(password.encode(
            'utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        """Check if the provided password matches the hashed password."""
        return bcrypt.checkpw(
            password.encode('utf-8'), self.password.encode('utf-8'))

    def to_dict(self):
        """Convert object to dictionary and
        exclude sensitive fields like password.
        """
        user_dict = super().to_dict()
        user_dict.pop('password', None)  # Exclude password
        return user_dict
