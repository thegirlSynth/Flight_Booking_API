#!/usr/bin/env python3
"""
"""

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Booking, Flight
from app import db

bookings = Blueprint("bookings", __name__)


@bookings.route("/search-flights", methods=["POST"], strict_slashes=False)
def search_flights():
    source = request.form.get("source")
    destination = request.form.get("destination")
    departure_date = request.form.get("departure_date")

    query = Flight.query

    if source:
        query = query.filter_by(source=source)
    if destination:
        query = query.filter_by(destination=destination)
    if departure_date:
        query = query.filter_by(departure_date=departure_date)

    flights = query.all()
    flights_data = [
        {
            "id": flight.id,
            "source": flight.source,
            "destination": flight.destination,
            "departure_date": flight.departure_date,
        }
        for flight in flights
    ]

    return jsonify({"flights": flights_data})


@bookings.route("/book-flight", methods=["POST"], strict_slashes=False)
@login_required
def book_flight():
    user_id = current_user.id
    flight_id = request.form.get("flight_id")

    new_booking = Booking(user_id=user_id, flight_id=flight_id)
    db.session.add(new_booking)
    db.session.commit()

    return (
        jsonify(
            {
                "message": f"Flight booked successfully\n This is your booking ID: {new_booking.id}"
            }
        ),
        201,
    )


@bookings.route(
    "/cancel-booking/<int:booking_id>", methods=["DELETE"], strict_slashes=False
)
@login_required
def cancel_booking(booking_id):
    booking = Booking.query.get(booking_id)
    if not booking:
        return jsonify({"message": "Booking not found"}), 404

    db.session.delete(booking)
    db.session.commit()

    return jsonify({"message": "Booking cancelled"}), 200
