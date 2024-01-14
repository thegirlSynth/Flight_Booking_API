#!/usr/bin/env python3
"""
"""

from app import db
from datetime import datetime
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250), nullable=False)
    roles = db.relationship(
        "Role", secondary="user_roles", backref=db.backref("users", lazy="dynamic")
    )
    bookings = db.relationship("Booking", back_populates="user", lazy=True)


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)


class UserRoles(db.Model):
    __tablename__ = "user_roles"
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey("users.id", ondelete="CASCADE"))
    role_id = db.Column(db.Integer(), db.ForeignKey("roles.id", ondelete="CASCADE"))


class Booking(db.Model):
    __tablename__ = "bookings"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)
    date_booked = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(20), nullable=False, default="pending")

    # Relationships
    user = db.relationship("User", back_populates="bookings")
    flight = db.relationship("Flight", back_populates="bookings")

    def __repr__(self):
        return f"<Booking {self.id}, User {self.user_id}, Flight {self.flight_id}, Status {self.status}>"


class Flight(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(250), nullable=False)
    destination = db.Column(db.String(250), nullable=False)
    departure_date = db.Column(db.Date, nullable=False)
    airline = db.Column(db.String(100), nullable=False)
    departure_time = db.Column(db.DateTime, nullable=False)
    arrival_time = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Interval, nullable=False)  # Duration in hours and minutes
    price = db.Column(db.Float, nullable=False)
    available_seats = db.Column(db.Integer, nullable=False)

    bookings = db.relationship("Booking", back_populates="flight", lazy=True)
