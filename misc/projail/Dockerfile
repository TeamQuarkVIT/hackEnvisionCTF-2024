FROM python:3.9

RUN apt-get update && \
    apt-get install socat -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m ctf

WORKDIR /home/ctf/challenge
COPY src/. .


RUN chown -R ctf:ctf /home/ctf/challenge

EXPOSE 1337
CMD socat -dd tcp-listen:1337,fork,reuseaddr,su=ctf exec:"python3 -u chall.py"
