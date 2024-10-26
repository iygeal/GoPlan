from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from app.models.user import User
from flask_jwt_extended import create_access_token, jwt_required
from app.routes import app_views

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# REGISTER USER
@app_views.route('/users', methods=['POST'], strict_slashes=False)
def register_user():
    """Register a new user"""
    if not request.is_json:
        abort(400, description="Request must be JSON")

    data = request.get_json()
    required_fields = ['email', 'password', 'username']
    missing_fields = [field for field in required_fields if not data.get(field)]

    if missing_fields:
        abort(400, description=f"Missing field(s): {', '.join(missing_fields)}")

    try:
        new_user = User()
        for key, value in data.items():
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(new_user, key, value)

        new_user.set_password(data['password'])
        new_user.validate_email()
        new_user.save()

        access_token = create_access_token(identity=new_user.id)
        return jsonify({
            "success": True,
            "access_token": access_token,
            "user": new_user.to_dict()
        }), 201

    except Exception as e:
        abort(500, description=str(e))

# Other routes...

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)