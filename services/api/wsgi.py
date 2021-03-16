from services.api import create_app
from services.common.socket_io.socket_io import get_socket_io_server

app = create_app()

if __name__ == '__main__':
    # Flask does not support sockets and we have to run the server using wsgi server - SocketIO
    socket_io_server = get_socket_io_server()
    socket_io_server.run(app, debug=True, host='0.0.0.0', port=5000)
