#!/bin/bash

/usr/bin/docker rmi --force web_deepcopy:latest

/usr/bin/docker build -t  web_deepcopy:latest .

/usr/bin/docker run -p 0.0.0.0:4000:4000  web_deepcopy:latest
