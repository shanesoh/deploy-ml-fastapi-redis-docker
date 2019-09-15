FROM python:3.7-slim-buster

COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt

# Download ResNet50 model and cache in image
RUN python -c "from keras.applications import ResNet50; ResNet50(weights='imagenet')"

COPY . /app

CMD ["python", "/app/main.py"]
