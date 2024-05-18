FROM python:3.11-alpine3.18
LABEL authors="V. Petrenko"
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . /app

EXPOSE 8000

RUN apk update && apk add musl-dev postgresql-dev

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry lock --no-update
RUN poetry install
