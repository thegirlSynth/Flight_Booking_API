#!/usr/bin/env python3
"""
"""

from flask import Blueprint, jsonify, request
from flask_user import login_required
from app.models import Booking, Flight
from app import db

bookings = Blueprint("bookings", __name__)


@bookings.route("/book-flight", methods=["POST"])
@login_required
def book_flight():
    user_id = current_user.id
    flight_id = request.json.get("flight_id")

    new_booking = Booking(user_id=user_id, flight_id=flight_id)
    db.session.add(new_booking)
    db.session.commit()

    return jsonify({"message": "Flight booked successfully"}), 201


@bookings.route("/cancel-booking/<int:booking_id>", methods=["DELETE"])
@login_required
def cancel_booking(booking_id):
    booking = Booking.query.get(booking_id)
    if not booking:
        return jsonify({"message": "Booking not found"}), 404

    db.session.delete(booking)
    db.session.commit()

    return jsonify({"message": "Booking cancelled"}), 200
