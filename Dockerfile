FROM python:3.8-alpine

RUN pip install flask

COPY . /myweb

WORKDIR /myweb

ENV FLASK_APP=/myweb/app.py
ENV FLASK_ENV=development

CMD flask run --host=0.0.0.0
