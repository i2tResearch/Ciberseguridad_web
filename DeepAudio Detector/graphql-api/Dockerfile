FROM python:3.7.8

RUN apt-get update
RUN apt-get install libsndfile1 -y

ENV PYTHONUNBUFFERED=1
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/
RUN pip install -r core/requirements/development.txt

RUN adduser user
USER user

CMD python manage.py runserver 0.0.0.0:$PORT