#!/bin/bash

docker build -t avg_jail .
docker run -p 1337:1337 --name=avg_jail --rm -it avg_jail
