#!/bin/bash

/usr/bin/docker rmi --force web_mongologin:latest

/usr/bin/docker build -t  web_mongologin:latest .

/usr/bin/docker run -d -p 0.0.0.0:4000:4000  web_mongologin:latest
