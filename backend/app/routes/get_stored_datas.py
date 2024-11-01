#!/usr/bin/env python3
"""
API routes for states, cities, attractions, and attraction types
with standardized error handling
"""
from flask import jsonify, request, abort
from app import db
from flask_jwt_extended import create_access_token, jwt_required
from app.routes import app_views
from app.models.state import State
from app.models.city import City
from app.models.attraction import Attraction
from app.models.attraction_type import AttractionType


@app_views.route('/states', methods=['GET'],
                 strict_slashes=False)
@jwt_required()
def get_states():
    """
    Retrieve all available states.
    
    Returns:
        JSON response with state data.
    """
    try:
        states = State.query.all()
        state_data = [{
            'id': state.id,
            'name': state.name
        } for state in states]
        return jsonify({
            'success': True,
            'states': state_data
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app_views.route('/cities', methods=['GET'],
                 strict_slashes=False)
@jwt_required()
def get_cities():
    """
    Retrieve all available cities.
    
    Returns:
        JSON response with city data.
    """
    try:
        cities = City.query.all()
        city_data = [{
            'id': city.id,
            'name': city.name,
            'state_id': city.state_id
        } for city in cities]
        return jsonify({
            'success': True,
            'cities': city_data
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app_views.route('/attraction_types', methods=['GET'],
                 strict_slashes=False)
@jwt_required()
def get_attraction_types():
    """
    Retrieve all available attraction types.
    
    Returns:
        JSON response with attraction type data.
    """
    try:
        types = AttractionType.query.all()
        type_data = [{
            'id': str(t.id),
            'name': t.name
        } for t in types]
        return jsonify({
            'success': True,
            'attraction_types': type_data
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app_views.route('/attractions', methods=['GET'],
                 strict_slashes=False)
@jwt_required()
def get_attractions():
    """
    Retrieve all available attractions.
    
    Returns:
        JSON response with attraction data.
    """
    try:
        attractions = Attraction.query.all()
        attraction_data = [{
            'id': attraction.id,
            'name': attraction.name,
            'city_id': attraction.city_id,
            'type_id': attraction.type_id
        } for attraction in attractions]
        return jsonify({
            'success': True,
            'attractions': attraction_data
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# Optional: Add a custom error handler for 404 errors
@app_views.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'success': False,
        'error': 'Not found'
    }), 404

# Optional: Add a custom error handler for 500 errors
@app_views.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500
