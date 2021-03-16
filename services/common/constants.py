import os
from inspect import getfile

from services.common.get_env import get_env_var

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(getfile(lambda: 0))))
STATIC_CLIENT_PATH = os.path.join(ROOT_PATH, 'services', 'client')

DEFAULT_HOST = 'localhost'

BROKER_PROTOCOL = get_env_var(name='BROKER_PROTOCOL', default='amqp')
BROKER_HOST = get_env_var(name='BROKER_HOST', default=DEFAULT_HOST)
BROKER_PORT = get_env_var(name='BROKER_PORT', default=5672, cast_function=int)
BROKER_VIRTUAL_HOST = get_env_var(name='BROKER_VHOST', default='micro')
BROKER_USERNAME = get_env_var(name='BROKER_USER', default='micro')
BROKER_PASSWORD = get_env_var(name='BROKER_PASSWORD', default='micro')

BROKER_URL_WITHOUT_VHOST = f'{BROKER_PROTOCOL}://{BROKER_USERNAME}:{BROKER_PASSWORD}@{BROKER_HOST}'
BROKER_URL_WITH_VHOST = f'{BROKER_URL_WITHOUT_VHOST}/{BROKER_VIRTUAL_HOST}'

SUBMIT_TASK_QUEUE = get_env_var(name='BROKER_PASSWORD', default='submit_task_queue')

ASYNC_MODE = get_env_var(name='ASYNC_MODE', default='eventlet')
