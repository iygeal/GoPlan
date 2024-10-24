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

    def to_dict(self):
        """Make a dictionary representation of GoPlan model object"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = dictionary['created_at'].isoformat()
        dictionary['updated_at'] = dictionary['updated_at'].isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def __str__(self):
        """Make a string representation of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save the current instance to the database."""
        self.updated_at = datetime.utcnow()
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Delete the current instance from the database."""
        db.session.delete(self)
        db.session.commit()
