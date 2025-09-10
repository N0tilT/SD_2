FROM python:3.12-slim

WORKDIR /src
COPY ["./", "./"]

RUN pip install --no-cache-dir psycopg2-binary

CMD ["python", "main.py"]