#!/usr/bin/env python3
"""
contains a history model that inherits from BaseModel
"""

from app.db import db
from app.models.base_model import BaseModel


class SearchHistory(BaseModel):
    """Search History model for the application.
    """

    __tablename__ = 'search_histories'

    user_id = db.Column(db.String(60), db.ForeignKey(
        'users.id'), nullable=False)
    search_query = db.Column(db.String(255), nullable=False)
    searched_at = db.Column(db.DateTime, nullable=False,
                            default=db.func.current_timestamp())

    # Relationship
    user = db.relationship('User', back_populates='search_histories')

    def __repr__(self):
        return f'<SearchHistory {self.id}: {self.user.username} - "{self.search_query}">'
