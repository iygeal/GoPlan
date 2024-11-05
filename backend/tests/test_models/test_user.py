#!/usr/bin/env python3
"""
Unit tests for the User model in the GoPlan application.
"""

import unittest
from app import create_app, db
from app.models.user import User


class UserModelTestCase(unittest.TestCase):
    """
    Test case for the User model, including setup, teardown, and test methods
    for creating and validating User instances.
    """

    def setUp(self):
        """
        Sets up a new app instance with testing configuration and an
        in-memory SQLite database for each test case.
        """
        self.app = create_app(testing=True)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        # Sample user data for testing
        self.test_user_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpassword123",
            "first_name": "Test",
            "last_name": "User",
            "profile_picture": None,
            "bio": "This is a test user."
        }

    def tearDown(self):
        """
        Tears down the test database and application context after each test.
        """
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_user(self):
        """
        Tests the creation of a new User instance with all required attributes,
        saving it to the database, and retrieving it to check if attributes
        match and password is hashed correctly.
        """
        # Create a new user with all required attributes
        user = User(
            username=self.test_user_data["username"],
            email=self.test_user_data["email"],
            first_name=self.test_user_data["first_name"],
            last_name=self.test_user_data["last_name"],
            profile_picture=self.test_user_data["profile_picture"],
            bio=self.test_user_data["bio"]
        )
        user.set_password(self.test_user_data["password"])
        db.session.add(user)
        db.session.commit()

        # Retrieve the user from the database and check attributes
        retrieved_user = User.query.filter_by(username="testuser").first()
        self.assertIsNotNone(
            retrieved_user, "User should exist in the database."
        )
        self.assertEqual(
            retrieved_user.username, "testuser", "Username should match."
        )
        self.assertEqual(
            retrieved_user.email, "testuser@example.com", "Email should match."
        )
        self.assertTrue(
            retrieved_user.check_password("testpassword123"),
            "Password should match."
        )


if __name__ == "__main__":
    unittest.main()
