"""
Create Mock Flights
"""

import random
from datetime import datetime, timedelta
from app import app, db
from app.models import Flight


def generate_random_date():
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    random_days = random.randint(1, (end_date - start_date).days)
    return start_date + timedelta(days=random_days)


def generate_random_duration():
    hours = random.randint(1, 5)  # Assuming flights are between 1 to 5 hours
    minutes = random.randint(0, 59)
    return timedelta(hours=hours, minutes=minutes)


def create_mock_flights():
    with app.app_context():
        # Mock flight data with states in Nigeria
        states = [
            "Lagos",
            "Abuja",
            "Kano",
            "Rivers",
            "Oyo",
            "Delta",
            "Kaduna",
            "Ogun",
            "Enugu",
            "Edo",
            "Katsina",
            "Borno",
            "Ondo",
            "Akwa Ibom",
            "Osun",
            "Imo",
            "Plateau",
            "Kogi",
            "Nasarawa",
            "Benue",
        ]

        mock_flights_data = []

        for _ in range(15):
            source = random.choice(states)
            destination = random.choice(states)
            while destination == source:  # Ensure different source and destination
                destination = random.choice(states)

            departure_date = generate_random_date()
            departure_time = datetime.combine(departure_date, datetime.min.time())
            duration = generate_random_duration()
            arrival_time = departure_time + duration
            price = round(
                random.uniform(100.0, 500.0), 2
            )  # Random price between 100 and 500

            flight_data = {
                "source": source,
                "destination": destination,
                "departure_date": departure_date,
                "airline": "Mock Airline",
                "departure_time": departure_time,
                "arrival_time": arrival_time,
                "duration": duration,
                "price": price,
                "available_seats": random.randint(
                    50, 200
                ),  # Assuming available seats between 50 and 200
            }
            mock_flights_data.append(flight_data)

        # Add mock flights to the database
        for flight_data in mock_flights_data:
            new_flight = Flight(**flight_data)
            db.session.add(new_flight)

        db.session.commit()


if __name__ == "__main__":
    create_mock_flights()
