#!/usr/bin/env python3
"""
This module defines the user-related routes for the GoPlan application.
It includes routes for registering new users and logging in existing users,
with proper validation and password management.
"""

from flask import jsonify, request, abort
from app.models.user import User
from app import db
from flask_jwt_extended import create_access_token
from app.routes import app_views


@app_views.route('/users', methods=['POST'])
def register_user():
    """Register a new user."""
    if not request.is_json:
        abort(400, description="Request must be JSON")

    data = request.get_json()

    # Required fields for registration
    required_fields = ['username', 'email',
                       'password', 'first_name', 'last_name']

    for field in required_fields:
        if field not in data or not data[field]:
            abort(400, description=f"Missing required field: {field}")

    try:
        new_user = User()
        for key, value in data.items():
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(new_user, key, value)

        new_user.set_password(data['password'])  # Hash password
        new_user.validate_email()  # Validate email format
        new_user.save()  # Save user to database

        access_token = create_access_token(identity=new_user.id)
        return jsonify({"success": True, "access_token": access_token}), 201

    except Exception as e:
        abort(500, description=str(e))


@app_views.route('/login', methods=['POST'])
def login_user():
    """Log in a user using email or username, and password."""
    if not request.is_json:
        abort(400, description="Request must be JSON")

    data = request.get_json()
    user = None

    # Attempt to retrieve user by email or username
    if data.get('email'):
        user = User.query.filter_by(email=data['email']).first()
    elif data.get('username'):
        user = User.query.filter_by(username=data['username']).first()

    # Check credentials if user is found
    if user and user.check_password(data.get('password')):
        access_token = create_access_token(identity=user.id)
        return jsonify({"success": True, "access_token": access_token}), 200

    abort(401, description="Invalid credentials")
