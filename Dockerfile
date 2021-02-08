# pull official base image
FROM python:3.7

RUN adduser myproj
WORKDIR /home/myproj
# RUN mkdir -p /usr/src/app
# set working directory
#WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY api.py ./

# aws credentials
run mkdir .aws
COPY $HOME/.aws/credentials ./.aws/credentials
RUN chown -R myproj:myproj ./
USER myproj

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8801"]

