#!/usr/bin/env python3
"""This module provides a template for all models."""


from datetime import datetime
from uuid import uuid4
from app.db import db


class BaseModel(db.Model):
    """Base model for all other models."""
    __abstract__ = True
    id = db.Column(db.String(60), primary_key=True,
                   default=lambda: str(uuid4()))
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Constructor for BaseModel to handle object creation."""
        if kwargs:
            # Remove unnecessary class data
            kwargs.pop('__class__', None)

            # Safeguard created_at and updated_at fields
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.fromisoformat(
                    kwargs['created_at'])
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.fromisoformat(
                    kwargs['updated_at'])

            # Assign attributes based on kwargs
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            # Default values for new instances
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.utcnow()

    def save(self):
        """Save the current instance to the database."""
        self.updated_at = datetime.utcnow()
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Delete the current instance from the database."""
        db.session.delete(self)
        db.session.commit()
