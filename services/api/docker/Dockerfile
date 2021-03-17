FROM python:3.8

ENV REQUIREMENTS=/requirements
ENV MICRO_ROOT=/micro
ENV PYTHONPATH=${PYTHONPATH}:${MICRO_ROOT}

USER root

COPY ./services/api/requirements.txt ${REQUIREMENTS}/requirements.txt

RUN python3 -m pip install --no-cache-dir -r ${REQUIREMENTS}/requirements.txt

WORKDIR ${MICRO_ROOT}/services/api/

CMD ["/bin/bash", "/micro/services/api/docker/entrypoint.sh"]
