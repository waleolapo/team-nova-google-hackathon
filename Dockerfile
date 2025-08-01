FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=src.main

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "src.main:app"]