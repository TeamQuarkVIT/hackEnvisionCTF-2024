FROM python:3.11-slim

WORKDIR /code

COPY ./src .
RUN pip3 install -r requirements.txt

EXPOSE 1337

CMD [ "python3", "server.py" , "1337"]

