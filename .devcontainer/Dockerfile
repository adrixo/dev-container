FROM mcr.microsoft.com/devcontainers/python:3.9

RUN apt update && DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get install --no-install-recommends -y git curl \
    gzip git strace libpq-dev gcc g++ && \
    pip install poetry && \
    apt install direnv

    execution,
    testing,
    documentation,
    integration,
    deploying
    PR review