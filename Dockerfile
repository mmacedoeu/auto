FROM albertsai/raspbian_buster
#FROM registry.gitlab.com/gabriel-technologia/board-video-history:base
#FROM python:3.7.9-slim-buster
MAINTAINER diego@gabriel.com.br
ADD . /autoprov
WORKDIR /autoprov
RUN apt update && apt upgrade -y && apt install python3.7 python3-pip -y
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN mkdir -p /autoprov && \
mkdir -p /.apps/common/
ENV HOME /
VOLUME ["/.apps/common/", "/var/run/docker.sock"]
ENV PYTHONPATH "${PYTHONPATH}:/autoprov"
ENTRYPOINT ["python3", "-m", "auto.repetidor"]