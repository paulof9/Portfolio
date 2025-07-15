from flask_babel import Babel, _
from flask import Flask, request, session, g
import os

babel = Babel()

def get_locale():
    lang = request.args.get('lang')
    if lang in ['en', 'pt']:
        session['lang'] = lang
        g.current_lang = lang
        return lang

    if 'lang' in session:
        g.current_lang = session['lang']
        return session['lang']

    g.current_lang = 'en'
    return 'en'

def create_app():
    app = Flask(__name__)

    app.config['BABEL_DEFAULT_LOCALE'] = 'en'
    translations_path = os.path.abspath(os.path.join(app.root_path, '..', 'translations'))
    app.config['BABEL_TRANSLATION_DIRECTORIES'] = translations_path

    app.secret_key = 'in9A#juaC4Kmf$m1$qAbJ!Y9YDvHRR9^RmHeFzRenTqc9qKLkmFE#E#20cLaja5W'

    babel.init_app(app, locale_selector=get_locale)

    app.jinja_env.globals['_'] = _
    app.jinja_env.globals['g'] = g 

    from app.blueprints.main import main as main_bp
    app.register_blueprint(main_bp)

    return app