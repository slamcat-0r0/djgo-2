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


COPY ./app /app
COPY ./entrypoints/python-entrypoint.py /
COPY ./wait-for-it.sh /

RUN useradd -ms /bin/bash user
RUN chown user -R /app/

RUN chmod u=rwx,g=rwx,o=rwx ../wait-for-it.sh
RUN chmod u=rwx,g=rwx,o=rwx ../python-entrypoint.py

RUN pip3 install --upgrade pip
RUN pip3 install -r ./app/requirements.txt

WORKDIR /app
