# Flight Booking API

Welcome to the Flight Booking API documentation. This API provides a platform for users to book flights, search for available flights, and manage their bookings. It is designed to be a user-friendly and efficient solution for flight-related activities.

## Base URL
The base URL for accessing the API is [http://synth.pythonanywhere.com/](http://synth.pythonanywhere.com/).

## API Version
The current version of the API is 1.0.

## Description
The Flight Booking API allows users to perform the following actions:

### Bookings
#### `POST /book-flight`
Book a flight using this endpoint.

#### `POST /search-flights`
Search for available flights based on specified criteria.

### Users
#### `GET /dashboard`
Retrieve the user dashboard, providing information about upcoming flights and booking history.

### Authentication
#### `GET /login`
Retrieve the login page.

#### `POST /login`
Log in a user.

#### `GET /logout`
Logout the user.

#### `POST /signup`
Register a new user.


