FROM python:3.8

COPY . /app

COPY ./requirements.txt /app

WORKDIR /app

RUN pip3 install -r requirements.txt

# RUN python3 app/main.py

CMD ["uvicorn", "app.main:app",  "--host", "0.0.0.0", "--port", PORT]
