FROM python:2.7-alpine

WORKDIR /tmp

ADD https_server.py ./
ADD server.pem ./
