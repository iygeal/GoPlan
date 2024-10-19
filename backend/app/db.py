#!/usr/bin/env python3
"""
This module provides database operations for GoPlan using Flask-SQLAlchemy.
It handles database connections and common operations like saving, deleting,
and retrieving objects.
"""

from flask_sqlalchemy import SQLAlchemy

# Initialize Flask-SQLAlchemy instance
db = SQLAlchemy()


class DBManager:
    """
    A class to manage database operations using Flask-SQLAlchemy.
    It provides methods to save, delete, get, and count objects in the database.
    """

    @staticmethod
    def save(obj):
        """
        Save an object to the database.

        Args:
            obj: The object to save (an instance of a model class).
        """
        db.session.add(obj)
        db.session.commit()

    @staticmethod
    def delete(obj):
        """
        Delete an object from the database.

        Args:
            obj: The object to delete (an instance of a model class).
        """
        if obj is not None:
            db.session.delete(obj)
            db.session.commit()

    @staticmethod
    def get(cls, obj_id):
        """
        Retrieve an object by its class and ID.

        Args:
            cls: The class (model) of the object.
            obj_id: The ID of the object to retrieve.

        Returns:
            An instance of the class or None if not found.
        """
        return db.session.query(cls).filter_by(id=obj_id).first()

    @staticmethod
    def count(cls=None):
        """
        Count the number of objects in the database for a given class.

        Args:
            cls: The class (model) to count objects for. If None, count all objects.

        Returns:
            The number of objects in the database.
        """
        if cls:
            return db.session.query(cls).count()
        else:
            total_count = 0
            for model_class in db.Model._decl_class_registry.values():
                if isinstance(model_class, type):
                    total_count += db.session.query(model_class).count()
            return total_count

    @staticmethod
    def reload():
        """
        Reloads the database by creating all tables.
        This should be called at the app's start to ensure tables exist.
        """
        db.create_all()

    @staticmethod
    def close():
        """
        Close the current database session.
        This should be called when the application is shutting down.
        """
        db.session.close()
