#!/usr/bin/env python3
"""This module provides a template for all models."""


from datetime import datetime
from uuid import uuid4
from app.db import db


class BaseModel(db.Model):
    """Base model that other models will inherit from."""

    __abstract__ = True  # Ensures this model is not created as a table

    id = db.Column(db.String(36), primary_key=True,
                   default=lambda: str(uuid4()), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow,
                           onupdate=datetime.utcnow, nullable=False)

    def save(self):
        """Save the instance to the database."""
        self.updated_at = datetime.utcnow()
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Delete the instance from the database."""
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        """Convert the instance to a dictionary for easy serialization."""
        return {column.name: getattr(
            self, column.name) for column in self.__table__.columns}
