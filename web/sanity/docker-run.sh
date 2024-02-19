#!/bin/bash

/usr/bin/docker rmi --force web_sanity:latest

/usr/bin/docker build -t  web_sanity:latest .

/usr/bin/docker run -p 0.0.0.0:5000:5000  web_sanity:latest
