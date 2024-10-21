#!/usr/bin/env python3
"""
Global error handler for the GoPlan API.
"""

from flask import jsonify
from werkzeug.exceptions import HTTPException


def handle_error(e):
    """Global error handler for all exceptions"""
    if isinstance(e, HTTPException):
        code = e.code
        message = e.description
    else:
        code = 500
        message = str(e)

    return jsonify({
        "success": False,
        "error": {
            "code": code,
            "message": message
        }
    }), code
