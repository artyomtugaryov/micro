from flask import Flask
from flask_restx import Api


def register_routes(api: Api, app: Flask, root='api'):
    from services.api.task import register_routes as attach_task

    # Add routes
    attach_task(api, app, root=root)
