#!/usr/bin/env python3
"""
This module defines the configuration settings for the GoPlan application,
including database configurations and other global settings.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Configuration class for the GoPlan app."""

    # Database configurations from .env
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+mysqlconnector://{os.getenv('GO_PLAN_USER')}:"
        f"{os.getenv('GO_PLAN_MYSQL_PWD')}@{os.getenv('GO_PLAN_MYSQL_HOST')}/"
        f"{os.getenv('GO_PLAN_MYSQL_DB')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable event system

    # JWT Secret Key from .env
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

    # JWT Access Token Expiration from .env
    JWT_ACCESS_TOKEN_EXPIRES = int(
        os.getenv('JWT_ACCESS_TOKEN_EXPIRES', 86400))


class TestConfig(Config):
    """Configuration class specifically for testing."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"  # In-memory database for testing
    JWT_SECRET_KEY = "test_secret"
    JWT_ACCESS_TOKEN_EXPIRES = 300


# Export the desired configuration based on environment
config = Config()
test_config = TestConfig()
