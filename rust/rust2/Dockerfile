FROM ubuntu:latest

WORKDIR /app

COPY src/. .

RUN apt-get update && \
    apt-get install -y socat && \
    rm -rf /var/lib/apt/lists/*


RUN chmod 111 maalik
RUN chmod 444 flag.txt

EXPOSE 1337

CMD socat -dd tcp-listen:1337,fork,reuseaddr,su=nobody exec:"./maalik"
