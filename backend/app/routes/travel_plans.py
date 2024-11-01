#!/usr/bin/env python3
"""
This module defines the CRUD routes for the TravelPlan model in GoPlan.
It includes routes for creating, retrieving, updating, and deleting travel plans,
as well as dashboard integration.
"""
from flask import jsonify, request, abort
from datetime import datetime
from app.models.travel_plan import TravelPlan
#from app.models.dashboard import Dashboard
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.routes import app_views


#!/usr/bin/env python3
"""
Travel Plan route implementation with full model support and validation
"""
from flask import jsonify, request, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
from app import db
from app.routes import app_views
from app.models.travel_plan import TravelPlan
from app.models.state import State
from app.models.city import City
from app.models.attraction import Attraction
from app.models.attraction_type import AttractionType


@app_views.route('/states/<state_id>', methods=['GET'],
                 strict_slashes=False)
def get_state_details(state_id):
    """
    Get details for a specific state and its cities.

    Args:
        state_id: The ID of the state to retrieve

    Returns:
        JSON response with state details and its cities
    """
    try:
        state = State.query.get(state_id)
        if not state:
            return jsonify({
                'success': False,
                'error': 'State not found'
            }), 404

        cities = City.query.filter_by(state_id=state_id).all()
        city_data = [{
            'id': str(city.id),
            'name': city.name
        } for city in cities]

        return jsonify({
            'success': True,
            'state': {
                'id': str(state.id),
                'name': state.name,
                'cities': city_data
            }
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app_views.route('/cities/<city_id>/attractions', methods=['GET'],
                 strict_slashes=False)
def get_city_attractions(city_id):
    """
    Get attractions in a specific city, optionally filtered by attraction type.

    Args:
        city_id: The ID of the city to retrieve attractions for

    Query Parameters:
        type_id: Optional attraction type ID to filter by

    Returns:
        JSON response with city attractions
    """
    try:
        city = City.query.get(city_id)
        if not city:
            return jsonify({
                'success': False,
                'error': 'City not found'
            }), 404

        # Get optional type_id filter from query parameters
        type_id = request.args.get('type_id')

        # Build query based on filters
        query = Attraction.query.filter_by(city_id=city_id)
        if type_id:
            query = query.filter_by(type_id=type_id)

        attractions = query.all()
        attraction_data = [{
            'id': str(attraction.id),
            'name': attraction.name,
            'type_id': str(attraction.type_id)
        } for attraction in attractions]

        return jsonify({
            'success': True,
            'city': {
                'id': str(city.id),
                'name': city.name,
                'attractions': attraction_data
            }
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app_views.route('/travel_plan',
                 methods=['POST'], strict_slashes=False)
@jwt_required()
def create_travel_plan():
    """
    Create a new travel plan.
    
    Required fields:
    - state_id
    - city_id
    - attraction_id
    - attraction_type_id
    - start_date
    - end_date
    
    Optional fields:
    - activities
    - budget
    - accommodation_details
    
    Returns:
        JSON response with created travel plan data.
    """
    try:
        # Get request data
        data = request.get_json()
        if not data:
            return jsonify({
                'success': False,
                'error': 'No data provided'
            }), 400

        # Get user_id from JWT
        user_id = get_jwt_identity()

        # Validate required fields
        required_fields = [
            'state_id', 'city_id', 'attraction_id', 
            'attraction_type_id', 'start_date', 'end_date'
        ]
        for field in required_fields:
            if field not in data:
                return jsonify({
                    'success': False,
                    'error': f'Missing required field: {field}'
                }), 400

        # Validate and parse dates
        try:
            start_date = datetime.strptime(data['start_date'], '%Y-%m-%d').date()
            end_date = datetime.strptime(data['end_date'], '%Y-%m-%d').date()
            
            if start_date > end_date:
                return jsonify({
                    'success': False,
                    'error': 'Start date cannot be after end date'
                }), 400
            
            if start_date < datetime.now().date():
                return jsonify({
                    'success': False,
                    'error': 'Start date cannot be in the past'
                }), 400
                
        except ValueError:
            return jsonify({
                'success': False,
                'error': 'Invalid date format. Use YYYY-MM-DD'
            }), 400

        # Validate budget if provided
        if 'budget' in data:
            try:
                budget = float(data['budget'])
                if budget < 0:
                    return jsonify({
                        'success': False,
                        'error': 'Budget cannot be negative'
                    }), 400
            except ValueError:
                return jsonify({
                    'success': False,
                    'error': 'Invalid budget value'
                }), 400
        
        # Create new TravelPlan instance
        travel_plan = TravelPlan(
            user_id=user_id,
            state_id=data['state_id'],
            city_id=data['city_id'],
            attraction_id=data['attraction_id'],
            attraction_type_id=data['attraction_type_id'],
            start_date=start_date,
            end_date=end_date,
            activities=data.get('activities'),
            budget=float(data['budget']) if 'budget' in data else None,
            accommodation_details=data.get('accommodation_details')
        )

        # Save to database
        db.session.add(travel_plan)
        db.session.commit()

        # Prepare response
        response_data = {
            'id': str(travel_plan.id),
            'user_id': str(travel_plan.user_id),
            'state_id': str(travel_plan.state_id),
            'city_id': str(travel_plan.city_id),
            'attraction_id': str(travel_plan.attraction_id),
            'attraction_type_id': str(travel_plan.attraction_type_id),
            'start_date': travel_plan.start_date.isoformat(),
            'end_date': travel_plan.end_date.isoformat(),
            'activities': travel_plan.activities,
            'budget': float(travel_plan.budget) if travel_plan.budget else None,
            'accommodation_details': travel_plan.accommodation_details
        }

        return jsonify({
            'success': True,
            'travel_plan': response_data
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
