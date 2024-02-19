#!/bin/bash

docker build -t misc_rmrf .
docker run -p 1337:1337 --name=misc_rmrf --rm -it misc_rmrf
