# imagem base
FROM python:3.8

COPY ./backend-django-desafio-dev/requirements.txt .

RUN pip install -r requirements.txt

RUN pip install -U pip

ENV PYTHONDONTWRITEBYTECODE 1

RUN apt update \
    && apt install -y libpq-dev gcc nano

WORKDIR /backend
COPY ./backend-django-desafio-dev /backend/
