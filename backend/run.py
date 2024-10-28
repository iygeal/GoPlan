from flask import Flask
from flask_cors import CORS
from app.routes import app_views
from app.db import db  # Ensure this is the correct import path for your db instance
import os

app = Flask(__name__)
# Configure CORS to allow requests from http://localhost:3000
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}}, 
     supports_credentials=True, 
     expose_headers=["Content-Type", "Authorization"],
     allow_headers=["Content-Type", "Authorization"])

# Set the SQLAlchemy Database URI from environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+mysqlconnector://{os.getenv('GO_PLAN_USER')}:" 
    f"{os.getenv('GO_PLAN_MYSQL_PWD')}@{os.getenv('GO_PLAN_MYSQL_HOST')}/"
    f"{os.getenv('GO_PLAN_MYSQL_DB')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the app with the SQLAlchemy instance
db.init_app(app)

# Register the app_views blueprint
app.register_blueprint(app_views, url_prefix="/api")

if __name__ == "__main__":
    # Initialize the database tables
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
