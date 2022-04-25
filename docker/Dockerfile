FROM ubuntu:18.04

WORKDIR /usr/src/app
COPY requirements.txt .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8


RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    python3-distutils \
    tesseract-ocr \
    libtesseract-dev \
    poppler-utils

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

COPY . .
EXPOSE 80
