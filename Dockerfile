FROM python:3.8

COPY . /app

COPY ./requirements.txt /app

WORKDIR /app

RUN pip3 install -r requirements.txt

RUN python3 app/main.py

EXPOSE 8000
