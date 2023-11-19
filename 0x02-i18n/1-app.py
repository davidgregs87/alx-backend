#!/usr/bin/env python3
"""
A flask module
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Babel's configuration
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route("/", methods=['GET'], strict_slashes=False)
def home():
    """
    New home route
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
