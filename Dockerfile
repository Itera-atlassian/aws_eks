FROM python:3.6
RUN mkdir /app
COPY main.py /app
ENTRYPOINT uvicorn main:app --reload --port 5000 --host 0.0.0.0