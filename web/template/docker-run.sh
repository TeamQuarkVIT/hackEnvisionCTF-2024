#!/bin/bash

/usr/bin/docker rmi --force web_difference:latest

/usr/bin/docker build -t  web_difference:latest .

/usr/bin/docker run -p 0.0.0.0:1337:1337  web_difference:latest
