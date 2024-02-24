#!/usr/bin/python3
"""
Starting a Flask app
"""

from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
    home page returns hello HBNB
    """
    return "Hello HBNB!"
