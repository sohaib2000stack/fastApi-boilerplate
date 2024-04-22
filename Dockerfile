FROM python:3.10.10

WORKDIR /fastapi-app
COPY . /fastapi-app

RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "main.py"]