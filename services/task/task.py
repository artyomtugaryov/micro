import time

from services.common.broker.rabbitmq import RabbitMQBrokerConsumer
from services.common.socket_io import get_socket_io

print(' [*] Waiting for messages. To exit press CTRL+C')


def task_callback(body: dict):
    n = 10
    interval = 1

    print(f' [x] Received {body} and I will reprint this body {n} times with interval {interval}')
    for i in range(n):
        print(f' [x] -> Again: {body}')
        socket_io = get_socket_io()
        socket_io.emit('index', body)
        socket_io.sleep(0)
        time.sleep(interval)
    print(' [x] Done')


if __name__ == '__main__':
    consumer = RabbitMQBrokerConsumer()
    consumer.start_consume(task_callback)
