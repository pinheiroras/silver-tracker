FROM python:3.10

USER root
COPY . /usr/src/silvertracker
WORKDIR /usr/src/silvertracker

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt update
RUN apt-get install -y curl vim

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN python contrib/env_gen.py
COPY config/settings-docker backend/settings.py