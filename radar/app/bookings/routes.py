#!/usr/bin/env python3
"""
"""

from flask import Blueprint, flash, jsonify, request, render_template, redirect, url_for
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

    # return render_template("search_results.html", flights=flights_data)
    return jsonify({"flights": flights_data})


@bookings.route("/flight-details", methods=["POST"], strict_slashes=False)
@login_required
def flight_details():
    flight_id = request.form.get("flight_id")
    flight = Flight.query.get_or_404(flight_id)
    flight_data = {
        "airline": flight.airline,
        "source": flight.source,
        "destination": flight.destination,
        "departure_date": flight.departure_date,
        "departure_time": flight.departure_time.strftime("%Y-%m-%d %H:%M:%S"),
        "arrival_time": flight.arrival_time.strftime("%Y-%m-%d %H:%M:%S"),
        "available_seats": flight.available_seats,
    }

    return jsonify(flight_data)
    # return render_template("/flight_details", flight_id=flight_id)


@bookings.route("/book-flight", methods=["POST"], strict_slashes=False)
@login_required
def book_flight():
    user_id = current_user.id
    flight_id = request.form.get("flight_id")

    new_booking = Booking(user_id=user_id, flight_id=flight_id)
    db.session.add(new_booking)
    db.session.commit()

    # flash("Flight booked successfully", "success")
    # return redirect(url_for("users.dashboard")), 201
    return (
        jsonify(
            {
                "message": f"Flight booked successfully\n. Your booking id is {new_booking.id}"
            }
        ),
        201,
    )


@bookings.route(
    "/cancel-booking/<int:booking_id>", methods=["POST"], strict_slashes=False
)
@login_required
def cancel_booking(booking_id):
    booking = Booking.query.get(booking_id)

    if booking.user_id == current_user.id:
        if booking.status == "canceled":
            return jsonify({"message": "Booking already cancelled!"}), 301

        booking.status = "canceled"
        db.session.commit()
        return jsonify({"message": "Booking canceled successfully!"}), 201
    else:
        return (
            jsonify({"message": "You don't have permission to cancel this booking."}),
            403,
        )

    # return redirect(url_for("users.dashboard")), 200
