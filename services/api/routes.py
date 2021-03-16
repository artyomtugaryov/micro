from flask import Flask, Blueprint
from flask_restx import Api


def register_routes(api: Api, app: Flask):
    from services.api.controller import api as task_api

    api.add_namespace(task_api, path=f'/task')

    task_blueprint = Blueprint('Task API', __name__)
    app.register_blueprint(task_blueprint, url_prefix=f'/task')
