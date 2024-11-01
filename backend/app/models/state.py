#!/usr/bin/env python3
"""States model
"""

from app.db import db
from app.models.base_model import BaseModel


class State(BaseModel):
    __tablename__ = 'states'

    name = db.Column(db.String(60), nullable=False, unique=True)
    cities = db.relationship('City', back_populates='state',
                             cascade='all, delete-orphan')
