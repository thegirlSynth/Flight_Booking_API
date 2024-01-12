#!/usr/bin/env python3
"""
"""

import bcrypt
from flask import Blueprint, jsonify, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from flask_user import current_user
from app.models import User, Role
from app import db

auth = Blueprint("auth", __name__)


@auth.route("/")
def index() -> str:
    return jsonify({"message": "Welcome to the Flight Booking API"})


@auth.route("/home")
def home():
    if current_user.is_authenticated:
        return jsonify({"message": f"Welcome to the Home Page, {current_user.name}"})
    else:
        return redirect(url_for("auth.login")), 401


@auth.route("/signup", methods=["POST"], strict_slashes=False)
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
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()
    if not user or not bcrypt.checkpw(password.encode("utf-8"), user.password):
        return jsonify({"message": "Invalid credentials"}), 401

    login_user(user)
    # return redirect(url_for("auth.home")), 200
    return jsonify({"message": "Logged in successfully"}), 200


@auth.route("/logout", strict_slashes=False)
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"}), 200
