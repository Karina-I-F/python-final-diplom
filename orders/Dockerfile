# pull official base image
FROM python:3.10

# set work directory
WORKDIR /orders

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
#RUN apk update \
#    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r ./requirements.txt
RUN pip install wait-for-it

#share port
EXPOSE 8000

# copy project
COPY . .
