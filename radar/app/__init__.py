#!/usr/bin/env python3
"""
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object("config.ConfigClass")

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)

from app.auth.routes import auth
from app.bookings.routes import bookings
from app.users.routes import users

app.register_blueprint(auth)
app.register_blueprint(bookings)
app.register_blueprint(users)
