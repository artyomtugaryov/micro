import eventlet
from flask import Flask, render_template
from flask_restx import Api

from services.common.constants import STATIC_CLIENT_PATH


def create_app() -> Flask:
    from services.api.config import get_config
    from services.api.routes import register_routes
    eventlet.monkey_patch()

    app = Flask(__name__, template_folder=STATIC_CLIENT_PATH)
    config_class = get_config()
    app.config.from_object(config_class)

    api = Api(app, title='Micro API', version='0.1.0', prefix='/api')
    register_routes(api, app)

    @app.route('/index')
    def index():
        return render_template('index.html')

    return app
