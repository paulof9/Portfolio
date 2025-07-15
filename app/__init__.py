from flask_babel import Babel, _
from flask import Flask, request



def get_locale():
    lang = request.args.get('lang') or request.accept_languages.best_match(['en', 'pt'])
    print(f"[DEBUG] Idioma detectado: {lang}")
    return lang


def create_app():
    app = Flask(__name__)

    app.config['BABEL_DEFAULT_LOCALE'] = 'en'
    app.config['BABEL_TRANSLATION_DIRECTORIES'] = '../translations'

    babel.init_app(app, locale_selector=get_locale)

    app.jinja_env.globals['_'] = _

    from app.blueprints.main import main as main_bp
    app.register_blueprint(main_bp)

    return app

babel = Babel()