# FROM alpine:3.15
FROM python:3.9.9-slim-buster
LABEL maintainer = "mign.pl"


ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
	gcc \
	curl \
	gettext \
	mariadb-client \
	default-mysql-client default-libmysqlclient-dev \
	libpq-dev \
	sqlite3 \
	nano \
	iputils-ping \
	--no-install-recommends apt-utils && rm -rf /var/lib/apt/lists/*

# RUN apk update && apk add \
#     bash \
#     py3-pip \
#     gcc \
#     python3-dev \
#     postgresql-dev \
#     musl-dev

RUN pip3 install --upgrade pip

COPY ./app /app
RUN pip3 install -r ./app/requirements.txt
COPY ./entrypoints/python-entrypoint.py /python-entrypoint.py
RUN chmod 755 ../python-entrypoint.py

RUN useradd -ms /bin/bash user
RUN chown user -R /app/

WORKDIR /app
