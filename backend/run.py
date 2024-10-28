#!/usr/bin/env python3
"""
This module runs the GoPlan Flask app.
"""

from app import create_app
from flasgger import Swagger

# Create an instance of the app
app = create_app()

# Initialize Swagger with the app
swagger = Swagger(app)

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True)
