#!/usr/bin/env python3
"""
The Flask App
"""

from flask import Flask

app = Flask(__name__)


@app.route()
def route():
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
