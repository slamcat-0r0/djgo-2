FROM alpine:3.15

ENV PYTHONUNBUFFERED 1

RUN apk update && apk add \
    py3-pip \
    gcc \
    python3-dev

COPY ./app /app
RUN pip3 install -r ./app/requirements.txt

COPY ./entrypoints/python-entrypoint.py /python-entrypoint.py

RUN chmod -x ../python-entrypoint.py

WORKDIR /app