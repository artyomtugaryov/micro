from flask_socketio import SocketIO

from services.common.constants import BROKER_URL_WITH_VHOST


def get_socket_io_server() -> SocketIO:
    if not get_socket_io_server.SOCKET_IO:
        get_socket_io_server.SOCKET_IO = _create_socket_io_server()
    return get_socket_io_server.SOCKET_IO


get_socket_io_server.SOCKET_IO = None


def _create_socket_io_server() -> SocketIO:
    return SocketIO(cors_allowed_origins='*')


def get_socket_io() -> SocketIO:
    print(BROKER_URL_WITH_VHOST)
    return SocketIO(message_queue=BROKER_URL_WITH_VHOST,
                    logger=True, engineio_logger=True)
