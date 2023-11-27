FROM python:3.10-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

COPY . .

COPY wait-for-postgres.sh .
RUN chmod +x wait-for-postgres.sh

RUN pip install gunicorn

#CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]
