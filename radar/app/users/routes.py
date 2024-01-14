#!/usr/bin/env python3
"""
"""

from flask import Blueprint, jsonify
from flask_login import current_user, login_required
from app.models import User
from app import db

users = Blueprint("users", __name__)


@users.route("/profile", methods=["GET"], strict_slashes=False)
@login_required
def profile():
    # Endpoint to retrieve user profile
    print("hello")
    user = User.query.get(current_user.id)
    return jsonify(
        {
            "email": user.email,
            "name": user.name,
            # "roles": [role.name for role in user.roles],
        }
    )
