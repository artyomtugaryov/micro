FROM node:14

ENV MICRO_ROOT=/micro

# Create app directory
WORKDIR ${MICRO_ROOT}

COPY services/sockets/package*.json ./

RUN npm install

CMD ["/bin/bash", "/micro/services/sockets/docker/entrypoint.sh"]