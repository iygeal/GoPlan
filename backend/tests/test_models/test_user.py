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
            "username": "iygeal",
            "email": "innocent@example.com",
            "password": "password77",
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
        retrieved_user = User.query.filter_by(username="iygeal").first()
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.username, "iygeal")
        self.assertEqual(retrieved_user.email, "innocent@example.com")
        self.assertTrue(retrieved_user.check_password("password77"))

    def test_invalid_email(self):
        """Test invalid email format raises ValueError."""
        invalid_email_user = User(
            username="invaliduser",
            email="invalidemail",
            password="password123",
            first_name="Iygeal",
            last_name="Anozie"
        )
        with self.assertRaises(ValueError):
            invalid_email_user.validate_email()

    def test_check_password(self):
        """Test password checking with correct and incorrect passwords."""
        user = User(
            username="passworduser",
            email="password@example.com",
            password="password123",
            first_name="Innocent",
            last_name="Anozie"
        )
        user.set_password("password123")
        self.assertTrue(user.check_password("password123"))
        self.assertFalse(user.check_password("wrongpassword"))

    def test_to_dict(self):
        """Test to_dict excludes the password field in the User model."""
        user = User(
            username="iygeal",
            email="innocent@example.com",
            password="password123",
            first_name="Onyekachi",
            last_name="Anozie"
        )
        user_dict = user.to_dict()
        self.assertNotIn("password", user_dict)


if __name__ == "__main__":
    unittest.main()
