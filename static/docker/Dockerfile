FROM centos:8 AS build
RUN dnf update -y
RUN dnf install curl gcc initscripts postgresql-server postgresql-contrib python3-devel python3-pip redis systemd  -y
RUN mkdir /opt/conplot
RUN curl https://codeload.github.com/rigdenlab/conplot/tar.gz/master | tar zx -C /opt/conplot/
WORKDIR /opt/conplot/conplot-master
RUN python3.6 -m pip install --upgrade pip
RUN python3.6 -m pip install gevent
RUN python3.6 -m pip install -r requirements.txt
