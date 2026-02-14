FROM python:3.11-slim

WORKDIR /app

COPY app.py .

RUN pip install flask flask-cors requests beautifulsoup4

CMD ["python", "app.py"]
