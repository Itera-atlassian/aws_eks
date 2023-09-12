FROM python:3.11
RUN mkdir /app
COPY requeriments.txt .
RUN pip install -r requeriments.txt
COPY main.py .
COPY template.html .
#ENTRYPOINT uvicorn main:app --reload --port 5000 --host 0.0.0.0
ENTRYPOINT python main.py