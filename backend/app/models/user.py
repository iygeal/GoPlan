#!/usr/bin/env python3
"""
contains user model that inherits from BaseModel
"""

from app.db import db
from app.models.base_model import BaseModel
from sqlalchemy.orm import validates
import re


class User(BaseModel):
    """User model for the application."""

    __tablename__ = 'users'

    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    profile_picture = db.Column(db.String(255), nullable=True)
    bio = db.Column(db.Text, nullable=True)

    # Relationships
    travel_plans = db.relationship('TravelPlan', back_populates='user', cascade='all, delete-orphan')
    dashboards = db.relationship('Dashboard', back_populates='user', cascade='all, delete-orphan')
    search_histories = db.relationship('SearchHistory', back_populates='user', cascade='all, delete-orphan')

    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise ValueError('Email is required')
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError('Invalid email format')
        return email

    @validates('username')
    def validate_username(self, key, username):
        if not username:
            raise ValueError('Username is required')
        if len(username) < 3:
            raise ValueError('Username must be at least 3 characters long')
        return username

    def __repr__(self):
        return f'<User {self.username}>'
