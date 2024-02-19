#!/bin/bash

/usr/bin/docker rmi --force crypto_one_time_use:latest

/usr/bin/docker build -t  crypto_one_time_use:latest .

/usr/bin/docker run -p 0.0.0.0:1337:1337  crypto_one_time_use:latest
