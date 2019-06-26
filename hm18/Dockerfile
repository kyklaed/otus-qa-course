FROM ubuntu:latest
MAINTAINER vadim
RUN apt-get update && apt-get install -y\
    git \
    python3-pip \
    && pip3 install pytest \
    && pip3 install paramiko
CMD git clone https://github.com/kyklaed/otus-qa-course.git \
    && pytest -s -v otus-qa-course/hm14/testopencart.py


