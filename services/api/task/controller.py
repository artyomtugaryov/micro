from flask_accepts import responds
from flask_restx import Namespace, Resource

from .schema import TaskSchema
from .service import TaskService

api = Namespace('Tasks')


@api.route('/')
class TaskResource(Resource):
    @responds(schema=TaskSchema)
    def get(self) -> dict:
        """
        Run task
        :return:
        """
        task = TaskService.run_task()
        return task
