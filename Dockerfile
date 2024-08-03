FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8000

ENV MODULE_NAME=app.main

CMD ["python", "letswift-server/main.py"]
