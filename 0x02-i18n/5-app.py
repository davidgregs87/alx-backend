#!/usr/bin/env python3
'''
Mock logging in
'''
from flask import Flask, render_template, request, g
from flask_babel import Babel


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


@app.route('/')
def index():
    ''' welcome page '''
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
