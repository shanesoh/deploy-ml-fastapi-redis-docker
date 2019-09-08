FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt

COPY . /app
