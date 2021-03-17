function getEnvironmentVariable(variable, defaultValue) {
    return variable in process.env ? process.env[variable] :defaultValue
}

const BROKER_PROTOCOL = getEnvironmentVariable('BROKER_PROTOCOL', 'amqp');
const BROKER_HOST = getEnvironmentVariable('BROKER_HOST', 'localhost');
const BROKER_PORT = getEnvironmentVariable('BROKER_PORT', 5672);
const BROKER_VIRTUAL_HOST = getEnvironmentVariable('BROKER_VIRTUAL_HOST', 'micro');
const BROKER_USERNAME = getEnvironmentVariable('BROKER_USER', 'micro');
const BROKER_PASSWORD = getEnvironmentVariable('BROKER_PASSWORD', 'micro');
const SOCKET_SERVICE_PORT = getEnvironmentVariable('SOCKET_SERVICE_PORT', 5001);

const BROKER_URL_WITHOUT_VHOST = `${BROKER_PROTOCOL}://${BROKER_USERNAME}:${BROKER_PASSWORD}@${BROKER_HOST}:${BROKER_PORT}`;

module.exports = {
    BROKER_URL_WITH_VHOST: `${BROKER_URL_WITHOUT_VHOST}/${BROKER_VIRTUAL_HOST}`,
    TASK_LOGS_QUEUE: getEnvironmentVariable('TASK_LOGS_QUEUE','task_logs'),
    SOCKET_EVENT: getEnvironmentVariable('SOCKET_EVENT', 'task'),
    SOCKET_SERVICE_PORT: SOCKET_SERVICE_PORT,
};