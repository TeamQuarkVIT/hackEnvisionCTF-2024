FROM ubuntu:latest

WORKDIR /app

COPY src/. .

RUN apt-get update && \
    apt-get install -y socat && \
    rm -rf /var/lib/apt/lists/*


RUN chmod 111 pwn01
RUN chmod 444 flag.txt

EXPOSE 1337

#CMD ["tcpserver", "-v", "0.0.0.0", "1337", "./pwn01"]
CMD socat -dd tcp-listen:1337,fork,reuseaddr,su=nobody exec:"./pwn01"
