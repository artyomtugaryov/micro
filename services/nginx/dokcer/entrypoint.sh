#!/bin/sh

set -eu

# shellcheck disable=SC2016
envsubst '${$API_SERVICE_ADDR} ${API_SERVICE_PORT} ${SOCKET_SERVICE_ADDR} ${SOCKET_SERVICE_PORT}' </etc/nginx/conf.d/default.conf.template >/etc/nginx/conf.d/default.conf

exec "$@"