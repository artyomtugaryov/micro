from services.common.broker.rabbitmq import RabbitMQBrokerPublisher


class TaskService:

    @staticmethod
    def run_task(data: dict) -> dict:
        return RabbitMQBrokerPublisher().publish(data=data)
