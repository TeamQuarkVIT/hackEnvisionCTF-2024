FROM python:3.9-slim

WORKDIR /app
COPY src/. .

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -m ctf

RUN chown -R ctf /app

EXPOSE 5000

USER ctf
ENV PYTHONUNBUFFERED 1

CMD ["waitress-serve", "--host=0.0.0.0", "--port=5000", "app:app"]
