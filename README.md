# fastapi-docker
basic fastapi with docker

## Overview
* gets a test file from s3
* starts server on localhost:8801a
* / returns hello world
* /error retuns 404
* /anything all other routes return json formatted csv file

### Run
1. docker build -t fake_api:latest .
2. docker-compose up


### Notes
uses https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker
