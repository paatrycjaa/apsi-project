FROM python:3.9.0-slim-buster

RUN mkdir -p /app
COPY requirements.txt /app/
WORKDIR /app
RUN apt-get update && apt-get upgrade
RUN apt-get install -y default-libmysqlclient-dev gcc
RUN pip install -r requirements.txt
EXPOSE 8000
