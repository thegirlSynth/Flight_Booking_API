#!/usr/bin/env python3
"""
User related endpoints
"""

from flask import Blueprint, jsonify, render_template
from flask_login import current_user, login_required
from app.models import User, Booking
from app import db

users = Blueprint("users", __name__)


@users.route("/profile", strict_slashes=False)
@login_required
def profile():
    """
    Endpoint to retrieve user profile
    """
    user = User.query.get(current_user.id)
    return jsonify(
        {
            "email": user.email,
            "name": user.name,
            # "roles": [role.name for role in user.roles],
        }
    )


@users.route("/dashboard", strict_slashes=False)
@login_required
def dashboard():
    upcoming_flights = (
        Booking.query.filter_by(user_id=current_user.id)
        .filter(Booking.status.in_(["pending", "confirmed"]))
        .all()
    )
    booking_history = (
        Booking.query.filter_by(user_id=current_user.id)
        .filter(Booking.status.in_(["completed", "canceled"]))
        .all()
    )

    upcoming_flights_data = []
    for flight in upcoming_flights:
        flight_data = {
            "source": flight.flight.source,
            "destination": flight.flight.destination,
            "departure_date": flight.flight.departure_date.strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "status": flight.status,
        }
        upcoming_flights_data.append(flight_data)

    booking_history_data = []
    for booking in booking_history:
        booking_data = {
            "source": booking.flight.source,
            "destination": booking.flight.destination,
            "departure_date": booking.flight.departure_date.strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "status": booking.status,
        }
        booking_history_data.append(booking_data)

    return jsonify(
        {
            "upcoming_flights": upcoming_flights_data or "No upcoming flights",
            "booking_history": booking_history_data or "No booking history",
            "user": current_user.name,
        }
    )
