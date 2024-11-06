#!/usr/bin/env python3
"""
Unit tests for the TravelPlan model in the GoPlan application.
"""

import unittest
from app import create_app, db
from app.models.user import User
from app.models.travel_plan import TravelPlan
from datetime import datetime


class TravelPlanModelTestCase(unittest.TestCase):
    """Test cases for the TravelPlan model."""

    @classmethod
    def setUpClass(cls):
        """Set up test database and app context for all test methods."""
        cls.app = create_app(testing=True)
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        db.create_all()

        # Create a test user with all required fields
        cls.user = User(
            username="traveluser",
            email="traveluser@example.com",
            first_name="Test",
            last_name="User",
            profile_picture=None,
            bio="A sample bio for testing."
        )
        cls.user.set_password("travelpassword")
        db.session.add(cls.user)
        db.session.commit()

    @classmethod
    def tearDownClass(cls):
        """Clean up test database after all tests."""
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def setUp(self):
        """Start a new database session for each test."""
        self.user_id = self.user.id

    def tearDown(self):
        """Rollback session for a clean state after each test."""
        db.session.rollback()

    def test_create_travel_plan(self):
        """Test that a travel plan can be created and saved to the database."""
        travel_plan = TravelPlan(
            user_id=self.user_id,
            title="Test Travel Plan",
            state="California",
            city="Los Angeles",
            start_date=datetime(2024, 12, 25),
            end_date=datetime(2024, 12, 30),
            activities="Sightseeing, dining",
            budget=1500.00,
            accommodation_details="Hotel stay at downtown"
        )
        db.session.add(travel_plan)
        db.session.commit()

        retrieved_plan = db.session.get(TravelPlan, travel_plan.id)
        self.assertIsNotNone(retrieved_plan)
        self.assertEqual(retrieved_plan.city, "Los Angeles")
        self.assertEqual(retrieved_plan.budget, 1500.00)

    def test_update_travel_plan(self):
        """Test that a travel plan's details can be updated."""
        travel_plan = TravelPlan(
            user_id=self.user_id,
            title="Update Test Plan",
            state="New York",
            city="New York City",
            start_date=datetime(2024, 1, 10),
            end_date=datetime(2024, 1, 20),
            activities="Museums, Broadway shows",
            budget=2000.00
        )
        db.session.add(travel_plan)
        db.session.commit()

        # Update fields
        travel_plan.activities = "Museums, concerts"
        travel_plan.budget = 1800.00
        travel_plan.accommodation_details = "Stay at Midtown hotel"
        db.session.commit()

        updated_plan = db.session.get(TravelPlan, travel_plan.id)
        self.assertEqual(updated_plan.activities, "Museums, concerts")
        self.assertEqual(updated_plan.budget, 1800.00)
        self.assertEqual(updated_plan.accommodation_details,
                         "Stay at Midtown hotel")

    def test_delete_travel_plan(self):
        """Test that a travel plan can be deleted from the database."""
        travel_plan = TravelPlan(
            user_id=self.user_id,
            title="Delete Test Plan",
            state="Nevada",
            city="Las Vegas",
            start_date=datetime(2024, 3, 15),
            end_date=datetime(2024, 3, 20),
            activities="Casino, shows",
            budget=1200.00
        )
        db.session.add(travel_plan)
        db.session.commit()

        travel_plan_id = travel_plan.id
        db.session.delete(travel_plan)
        db.session.commit()

        deleted_plan = db.session.get(TravelPlan, travel_plan_id)
        self.assertIsNone(deleted_plan)


if __name__ == "__main__":
    unittest.main()
