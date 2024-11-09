#!/usr/bin/env python3
"""
This module defines the SearchHistory model, which inherits from BaseModel.
It represents the search history of a user, storing search queries along
with their timestamps.
"""

from app.db import db
from app.models.base_model import BaseModel


class SearchHistory(BaseModel):
    """
    Represents the search history of a user, storing queries and timestamps.
    """

    __tablename__ = 'search_histories'

    user_id = db.Column(db.String(60), db.ForeignKey(
        'users.id'), nullable=False)
    search_query = db.Column(db.String(255), nullable=False)
    searched_at = db.Column(db.DateTime, nullable=False,
                            default=db.func.current_timestamp())

    # Relationships
    user = db.relationship('User', back_populates='search_histories')

    def __repr__(self):
        """
        Returns a string representation of the search history entry.
        """
        return f'<SearchHistory {self.id}: {self.user.username} - "{self.search_query}">'
