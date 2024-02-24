#!/usr/bin/python3
"""
Starting a Flask app a simple one
"""

from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
    home page return hello HBNB
    """
    return "Hello HBNB!"

