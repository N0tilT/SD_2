FROM python:3.13-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /src
COPY ["./", "./"]

RUN pip install --no-cache-dir psycopg2-binary fastapi uvicorn

CMD ["uvicorn", "main:app", "--reload","--host","0.0.0.0", "--port","8088"]