import ast
from typing import Callable

from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic

from services.common.broker.rabbitmq.manager import RabbitMQBrokerManager
from services.common.constants import SUBMIT_TASK_QUEUE


class RabbitMQBrokerConsumer:
    def __init__(self, task_queue: str = SUBMIT_TASK_QUEUE):
        self._broker_manager = RabbitMQBrokerManager()
        self._task_queue = task_queue
        self._callback: Callable = None

    @staticmethod
    def _decode_body(body: bytes) -> dict:
        dict_str = body.decode('UTF-8')
        return ast.literal_eval(dict_str)

    def _message_callback(self, ch: BlockingChannel, method: Basic.Deliver, _, body: bytes):
        body_as_dict = RabbitMQBrokerConsumer._decode_body(body)
        self._callback(body_as_dict)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def start_consume(self, callback: Callable):
        self._callback = callback

        channel = self._broker_manager.channel
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=self._task_queue, on_message_callback=self._message_callback)

        channel.start_consuming()
