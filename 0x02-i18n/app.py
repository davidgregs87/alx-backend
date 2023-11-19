#!/usr/bin/env python3
"""
A flask module
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone, UnknownTimeZoneError
from datetime import datetime
from babel.dates import format_datetime


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "es", "timezone": "Europe/Madrid"},
    4: {"name": "Teletubby", "locale": 'de', "timezone": "Europe/Amsterdam"},
    5: {"name": "Dgregs", "locale": 'zh', "timezone": "Europe/Beijing"},
    6: {"name": "NSK", "locale": 'en', "timezone": "Africa/Lagos"},
}


class Config:
    """
    Babel's configuration
    """
    LANGUAGES = ["en", "fr", "es", "de", "zh"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    find client default locale
    """
    locale = request.args.get('locale', '')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # Change the locale based on the information stored on the db
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    header_req = request.headers.get('locale', '')
    if header_req and header_req in app.config['LANGUAGES']:
        return header_req

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """
    find client timezone
    """
    tz = request.args.get('timezone', '').strip()
    if not tz and g.user:
        tz = g.user['timezone']
    try:
        return timezone(tz).zone
    except UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route("/", methods=['GET'], strict_slashes=False)
def home():
    """
    New home route
    """
    current_time = datetime.now(timezone(get_timezone()))
    formatted_time = format_datetime(current_time, 'medium', locale=get_locale())
    return render_template('index.html', new_time=formatted_time)


def get_user() -> dict | None:
    """
    Validate a request argument login_as
    """
    user_id = request.args.get('login_as', '')
    if not user_id:
        return None
    return users.get(int(user_id))


@app.before_request
def before_request():
    """
    Executed this before any other function
    """
    g.user = get_user()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
