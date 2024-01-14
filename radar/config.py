#!/usr/bin/env python3
"""
Flask App Config
"""

import os


class ConfigClass(object):
    """Flask application config"""

    # Flask settings
    SECRET_KEY = os.getenv("SECRET_KEY", "my_secret_key_is_my_secret")

    # Flask-SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = "sqlite:///radar.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-Mail SMTP server settings
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = "email@radar.com"
    MAIL_PASSWORD = "password"
    MAIL_DEFAULT_SENDER = '"MyApp" <noreply@radar.com>'

    # Flask-User settings
    # USER_APP_NAME = "Flask-User Basic App"
    # USER_ENABLE_EMAIL = True
    # USER_ENABLE_USERNAME = False
    # USER_EMAIL_SENDER_NAME = USER_APP_NAME
    # USER_EMAIL_SENDER_EMAIL = "noreply@eradar.com"
