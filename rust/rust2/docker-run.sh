#!/bin/bash

/usr/bin/docker rmi --force maalik:latest

/usr/bin/docker build -t  maalik:latest .

/usr/bin/docker run -p 0.0.0.0:1337:1337 maalik:latest
