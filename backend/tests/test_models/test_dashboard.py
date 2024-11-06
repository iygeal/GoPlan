#!/usr/bin/env python3
"""
Test cases for the Dashboard model in the GoPlan application.
"""

import unittest
from app import create_app, db
from app.models.user import User
from app.models.travel_plan import TravelPlan
from app.models.dashboard import Dashboard
from datetime import date


class DashboardModelTestCase(unittest.TestCase):
    """Test case for the Dashboard model."""

    @classmethod
    def setUpClass(cls):
        """Set up the test app and database once for all tests."""
        cls.app = create_app(testing=True)
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        """Tear down the database after all tests."""
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def setUp(self):
        """Set up before each test method."""
        self.user = User(
            username="testuser",
            email="testuser@example.com",
            password="testpassword",
            first_name="Test",
            last_name="User"
        )
        self.user.set_password("testpassword123")
        db.session.add(self.user)
        db.session.commit()

        self.travel_plan = TravelPlan(
            user_id=self.user.id,
            title="Test Plan",
            state="Test State",
            city="Test City",
            start_date=date(2023, 1, 1),
            end_date=date(2023, 1, 5)
        )
        db.session.add(self.travel_plan)
        db.session.commit()

        self.dashboard = Dashboard(
            user_id=self.user.id,
            travel_plan_id=self.travel_plan.id
        )
        db.session.add(self.dashboard)
        db.session.commit()

    def tearDown(self):
        """Clean up the database after each test method."""
        db.session.query(Dashboard).delete()
        db.session.query(TravelPlan).delete()
        db.session.query(User).delete()
        db.session.commit()

    def test_dashboard_retrieval(self):
        """Test that a dashboard can be retrieved by user ID."""
        retrieved_dashboard = Dashboard.query.filter_by(
            user_id=self.user.id).first()
        self.assertIsNotNone(retrieved_dashboard)
        self.assertEqual(retrieved_dashboard.user_id, self.user.id)
        self.assertEqual(retrieved_dashboard.travel_plan_id,
                         self.travel_plan.id)

    def test_dashboard_deletion(self):
        """Test that a dashboard can be deleted from the database."""
        dashboard_id = self.dashboard.id
        db.session.delete(self.dashboard)
        db.session.commit()

        with db.session() as session:
            deleted_dashboard = session.get(Dashboard, dashboard_id)
        self.assertIsNone(deleted_dashboard)

    def test_dashboard_associations(self):
        """Test associations between dashboard, user, and travel plan."""
        retrieved_dashboard = Dashboard.query.filter_by(
            user_id=self.user.id).first()
        self.assertIsNotNone(retrieved_dashboard)

        # Check association with user and travel plan
        self.assertEqual(retrieved_dashboard.user.id, self.user.id)
        self.assertEqual(retrieved_dashboard.travel_plan.id,
                         self.travel_plan.id)


if __name__ == '__main__':
    unittest.main()
