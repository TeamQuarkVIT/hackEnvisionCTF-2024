FROM php:8.2-cli

WORKDIR /var/www/html
COPY src/index.php .
COPY src/favicon.png.png .

RUN mkdir -p /flag
COPY src/*.txt /flag

RUN useradd ctf 
RUN chown -R ctf:ctf /flag

EXPOSE 80
USER ctf

CMD ["php", "-S", "0.0.0.0:80", "-t", "./"]
