from flask import Flask
from flask_restx import Api

BASE_ROUTE = 'task_api'


def register_routes(api: Api, app: Flask, root: str):
    from flask import Blueprint

    bp = Blueprint(BASE_ROUTE, __name__)

    from services.api.task.controller import api as task_api

    api.add_namespace(task_api, path='/run-task')
    app.register_blueprint(bp, url_prefix=f'/{root}/{BASE_ROUTE}')
