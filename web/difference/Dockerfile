FROM python:3.9-slim

WORKDIR /app

RUN pip install flask

RUN pip install gunicorn

COPY src/.  .

RUN chmod -R 555 /app

USER 1000:1000

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
