FROM python:3.8

ENV http_proxy http://proxy-dmz.intel.com:911
ENV https_proxy http://proxy-dmz.intel.com:912

ENV REQUIREMENTS=/requirements
ENV MICRO_ROOT=/micro
ENV PYTHONPATH=${PYTHONPATH}:${MICRO_ROOT}

USER root

COPY ./requirements.txt ${REQUIREMENTS}/requirements.txt

RUN python3 -m pip install --no-cache-dir -r ${REQUIREMENTS}/requirements.txt

COPY ./services/task/docker/entrypoint.sh /entrypoint.sh

WORKDIR ${MICRO_ROOT}

CMD ["/bin/bash", "/entrypoint.sh"]
