#!/usr/bin/env python3
"""
This module runs the GoPlan Flask app.
"""

from app import create_app
from flask_cors import CORS

# Create an instance of the app
app = create_app()

# Enable CORS
CORS(app)

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True)
