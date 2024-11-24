FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev gcc

COPY app.py /app/

RUN pip install --no-cache-dir psycopg2

CMD ["python", "app.py"]
