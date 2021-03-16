from pika import PlainCredentials, BlockingConnection, ConnectionParameters

from services.common.constants import BROKER_USERNAME, BROKER_PASSWORD, SUBMIT_TASK_QUEUE, BROKER_HOST, BROKER_PORT, \
    BROKER_VIRTUAL_HOST


class RabbitMQBrokerManagerMeta(type):
    instance = None

    def __call__(cls, *args, **kwargs) -> 'RabbitMQBrokerManager':
        if not RabbitMQBrokerManagerMeta.instance:
            RabbitMQBrokerManagerMeta.instance = RabbitMQBrokerManager()
        return RabbitMQBrokerManagerMeta.instance


class RabbitMQBrokerManager:
    def __init__(self):
        credentials = PlainCredentials(username=BROKER_USERNAME, password=BROKER_PASSWORD)

        self._connection = BlockingConnection(ConnectionParameters(host=BROKER_HOST,
                                                                   port=BROKER_PORT,
                                                                   virtual_host=BROKER_VIRTUAL_HOST,
                                                                   credentials=credentials))
        self.channel = self._connection.channel()
        self.channel.queue_declare(queue=SUBMIT_TASK_QUEUE, durable=True)
