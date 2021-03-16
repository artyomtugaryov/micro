from services.api.task.data import TaskData
from services.common.broker.rabbitmq import RabbitMQBrokerPublisher


class TaskService:
    task_id = 0

    @staticmethod
    def run_task() -> TaskData:
        task_data = TaskData(task_id=TaskService.task_id)
        TaskService.task_id += 1

        RabbitMQBrokerPublisher().publish(data=task_data)
        return task_data
