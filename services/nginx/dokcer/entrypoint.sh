#!/bin/sh

set -eu

# shellcheck disable=SC2016
envsubst '${$API_SERVICE_ADDR} ${SOCKET_SERVICE_ADDR}' </etc/nginx/conf.d/default.conf.template >/etc/nginx/conf.d/default.conf

exec "$@"