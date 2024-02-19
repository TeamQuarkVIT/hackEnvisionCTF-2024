FROM python:3.11-slim

WORKDIR /code

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./src .

EXPOSE 1337

CMD [ "python3", "server.py" , "1337"]

