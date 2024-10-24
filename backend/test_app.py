#!/usr/bin/env python3
"""
Test script to validate database connection and BaseModel functionality.
"""

from app import create_app, db
from app.models.base_model import BaseModel

# Create the Flask app instance
app = create_app()

# Define a test model inheriting from BaseModel


class TestModel(BaseModel):
    """A simple test model to verify BaseModel functionality."""
    name = db.Column(db.String(128), nullable=False)


# Create the tables for the models
with app.app_context():
    db.create_all()  # Create all tables

    # Test creating and saving a new TestModel instance
    test_instance = TestModel(name="Sample Test")
    test_instance.save()

    # Query the database to verify
    instance_from_db = TestModel.query.first()
    if instance_from_db:
        print(
            f"Test instance retrieved from database: {instance_from_db.name}")
    else:
        print("No instance found in the database.")

    # Cleanup: Remove the test instance
    test_instance.delete()
