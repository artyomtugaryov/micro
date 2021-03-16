import json

from pika.spec import BasicProperties

from services.common.broker.rabbitmq.manager import RabbitMQBrokerManager
from services.common.constants import SUBMIT_TASK_QUEUE


class RabbitMQBrokerPublisher:
    def __init__(self, task_queue: str = SUBMIT_TASK_QUEUE):
        self._broker_manager = RabbitMQBrokerManager()
        self._task_queue = task_queue

    def publish(self, data: dict):
        self._broker_manager.channel.basic_publish(
            exchange='',
            routing_key=self._task_queue,
            body=json.dumps(data),
            properties=BasicProperties(
                delivery_mode=2,
            ))
