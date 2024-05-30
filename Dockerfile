FROM python:3

WORKDIR /app

COPY app.py /app/app.py

CMD ["python", "/app/app.py"]