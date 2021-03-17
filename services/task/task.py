import time

from services.common.broker.rabbitmq import RabbitMQBrokerConsumer, RabbitMQBrokerPublisher
from services.common.constants import TASK_LOGS_QUEUE

print(' [*] Waiting for messages. To exit press CTRL+C')


def task_callback(body: dict):
    n = int(body['numberOfRepetitions'])
    interval = 1

    message_publisher = RabbitMQBrokerPublisher(task_queue=TASK_LOGS_QUEUE)

    print(f' [x] Received {body} and I will reprint this body {n} times with interval {interval}')
    for i in range(n):
        body['countDown'] = n - i
        print(f' [x] -> Again: {body}')
        message_publisher.publish(body)
        time.sleep(interval)
    print(' [x] Done')


if __name__ == '__main__':
    consumer = RabbitMQBrokerConsumer()
    consumer.start_consume(task_callback)
