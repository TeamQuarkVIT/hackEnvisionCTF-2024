FROM python:3.9-slim

WORKDIR /app

COPY src/. .

RUN pip install --no-cache-dir -r requirements.txt

RUN echo 'quarkCTF{wh3n_w1LL-d3vlopERs_staRT_usING_besT_pr4ct1c35}' > /flagUTLSCS.txt

RUN chmod 555 /app
RUN chmod 444 /flagUTLSCS.txt

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

