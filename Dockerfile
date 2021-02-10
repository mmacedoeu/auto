FROM python:3.7.9-slim-buster
MAINTAINER diego@gabriel.com.br

ADD . /autoprov
WORKDIR /autoprov
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN mkdir -p /home/autoprov && \
mkdir -p /.apps/common/

ENV HOME /

VOLUME ["/.apps/common/", "/var/run/docker.sock"]
ENV PYTHONPATH "${PYTHONPATH}:/home/autoprov"
ENTRYPOINT ["python3", "-m", "auto.Main"]