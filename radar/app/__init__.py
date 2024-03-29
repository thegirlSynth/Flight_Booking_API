#!/usr/bin/env python3
"""
Initialize Flask App
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_user import UserManager
from flask_mail import Mail
from flasgger import Swagger
from swagger import template, swagger_config


# from flask_user import UserManager

app = Flask(__name__)
app.config.from_object("config.ConfigClass")

db = SQLAlchemy(app)

from app.auth.routes import auth
from app.bookings.routes import bookings
from app.users.routes import users

app.register_blueprint(auth)
app.register_blueprint(bookings)
app.register_blueprint(users)

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    from app.models import User

    return User.query.get(int(user_id))


with app.app_context():
    from app.models import User, Role, UserRoles, Booking, Flight

    db.create_all()

# user_manager = UserManager(app, db, User)
mail = Mail(app)
Swagger(app, config=swagger_config, template=template)
