FROM python:3.10.13-slim-bullseye

RUN pip install flask
RUN pip install gunicorn

WORKDIR /app

COPY  . .

ENV PORT 80
CMD gunicorn -b 0.0.0.0:$PORT app:app
EXPOSE 80
