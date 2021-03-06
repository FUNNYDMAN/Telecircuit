FROM python:3.5
RUN mkdir /source

ADD . /source

WORKDIR /source

RUN apt-get update && \
    apt-get install -y postgresql-client curl

RUN chmod +x entrypoint.sh

RUN pip install -r requirements/requirements.txt