FROM nginx:1.21-alpine

RUN apk update && apk add bash

RUN rm /etc/nginx/conf.d/default.conf
COPY ./dockerfiles/nginx/nginx.conf /etc/nginx/conf.d
COPY ./dockerfiles/nginx/certs/ /etc/nginx/conf.d/certs/
COPY ./wait-for-it.sh /
RUN chmod u=rwx,g=rwx,o=rwx ./wait-for-it.sh