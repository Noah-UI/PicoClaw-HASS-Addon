ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:3.19
FROM ${BUILD_FROM}

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apk add --no-cache \
    bash \
    python3 \
    ttyd

WORKDIR /app
COPY run.sh /run.sh
COPY app /app
RUN chmod a+x /run.sh /app/main.py

CMD [ "/run.sh" ]
