from marshmallow import fields, Schema


class TaskSchema(Schema):
    """Task Schema"""

    taskId = fields.Integer(attribute='task_id')
