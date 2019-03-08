FROM python:alpine

WORKDIR /app
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev \
    && pip install psycopg2 \
    && pip install Flask-SQLAlchemy \
    && pip install 'sentry-sdk[flask]==0.7.6'
COPY take_home.py /app
COPY app_entry.sh /app
CMD ["python", "take_home.py"]