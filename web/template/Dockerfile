FROM python:3.9-slim

WORKDIR /app

COPY src/. .

RUN useradd -m ctf

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod 111 /app/app.py
RUN chmod 444 /app/flag1.txt
RUN chown -R ctf:ctf /app/flag2.txt

USER ctf

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
