#!/usr/bin/env python3
'''
Infer appropriate time zone
'''
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone, UnknownTimeZoneError


class Config:
    ''' Babel configuration '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    ''' Get locale from request '''
    locale = request.args.get('locale', '')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    header_locale = request.headers.get('locale', '')
    if header_locale in app.config['LANGUAGES']:
        return header_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    ''' gets user by id '''
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    ''' execute before other functions '''
    g.user = get_user()


@babel.timezoneselector
def get_timezone():
    ''' get user timezone '''
    u_tz = request.args.get('timezone', '').strip()
    if not u_tz and g.user:
        u_tz = g.user['timezone']
    try:
        return timezone(u_tz).zone
    except UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index():
    ''' welcome page '''
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(debug=True)
