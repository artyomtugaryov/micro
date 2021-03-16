from mypy_extensions import TypedDict


class TaskData(TypedDict, total=False):
    task_id: int
