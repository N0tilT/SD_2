FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

# TODO: add required packages
RUN pip install --no-cache-dir

COPY . .

EXPOSE 8731

CMD ["gunicorn", "--bind", "0.0.0.0:8731", "app:app"]