#!/usr/bin/env node

const constants = require('./constants');
const amqp = require('amqplib/callback_api');

const socketio = require('socket.io')

const io = socketio({
        cors: {
            origin: '*',
        }
    }
);

io.on('connection', (socket) => {
    socket.emit(constants.SOCKET_EVENT, {message: 'A new user has joined!'});
});

function sendSocket(message) {
    io.emit(constants.SOCKET_EVENT, message);
}

amqp.connect(constants.BROKER_URL_WITH_VHOST, (error0, connection) => {
    if (error0) {
        throw error0;
    }
    connection.createChannel((error1, channel) => {
        const queue = constants.TASK_LOGS_QUEUE;

        channel.assertQueue(queue, {
            durable: false
        });
        console.log(` [*] Waiting for messages in ${queue}. To exit press CTRL+C`);
        channel.consume(queue, (message) => {
            console.log(` [x] Received ${message.content.toString()}`);
            sendSocket(JSON.parse(message.content));
        }, {
            noAck: true
        });
    });
});

io.listen(constants.SOCKET_SERVICE_PORT);
