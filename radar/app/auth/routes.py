#!/usr/bin/env python3
"""
"""

import bcrypt
from flask import Blueprint, jsonify, flash, request, render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, Role
from app import db
from flasgger import swag_from

auth = Blueprint("auth", __name__)


@auth.route("/login", strict_slashes=False)
def index() -> str:
    """
    Retrieve the login page.
    ---
    tags:
      - Authentication
    parameters:
      - in: path
        name: email
        required: true
    responses:
      403:
        description: You need to log in to access this page

      200:
        description: Login page retrieved successfully
    """
    return jsonify({"message": "You need to log in to access this page"}), 403


@auth.route("/signup", methods=["POST"], strict_slashes=False)
@swag_from("../docs/auth/signup.yaml")
def signup():
    email = request.form.get("email")
    password = request.form.get("password")
    name = request.form.get("name")

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"message": "Email already registered"}), 400

    password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    new_user = User(email=email, name=name, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201


@auth.route("/login", methods=["POST"], strict_slashes=False)
@swag_from("../docs/auth/login.yaml")
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()
    if not user or not bcrypt.checkpw(password.encode("utf-8"), user.password):
        return jsonify({"message": "Invalid credentials"}), 401

    login_user(user)
    # return redirect("/home"), 200
    return jsonify({"message": "Logged in successfully"}), 200


@auth.route("/logout", strict_slashes=False)
@login_required
def logout():
    """
    Logout user
    ---
    tags:
      - Authentication
    parameters:
      - in: path
        name: email
        required: true
    responses:
      403:
        description: Already logged out!

      200:
        description: Logged out successfully
    """
    logout_user()
    return jsonify({"message": "Logged out successfully"}), 200
