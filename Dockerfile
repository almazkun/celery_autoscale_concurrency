FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/code

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv==2022.5.2 

RUN pipenv install --system --ignore-pipfile

COPY . .