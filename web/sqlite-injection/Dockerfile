FROM python:3.9-slim-bullseye

WORKDIR /app

RUN pip install gunicorn
RUN pip install flask

COPY src/. .

CMD gunicorn -b 0.0.0.0:5000 sqli_chal:app
EXPOSE 5000
