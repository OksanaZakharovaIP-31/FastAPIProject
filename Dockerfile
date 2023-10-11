FROM python:3.10.2

RUN mkdir /fastapi_project

WORKDIR /fastapi_project

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR src

CMD gunicorn main:app --bind=0.0.0.0:8000