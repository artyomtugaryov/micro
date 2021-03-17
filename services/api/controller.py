from flask import request
from flask_accepts import responds, accepts
from flask_restx import Namespace, Resource

from services.api.service import TaskService

api = Namespace('Tasks')


@api.route('/')
class TaskResource(Resource):

    @accepts(dict(name='numberOfRepetitions', type=int), api=api)
    @responds(dict(name='taskId', type=int))
    def post(self) -> dict:
        data = request.json
        print(data)
        return TaskService.run_task(data)

