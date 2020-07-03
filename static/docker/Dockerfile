FROM centos:8 AS build
RUN dnf update -y
RUN dnf install curl gcc initscripts postgresql-server systemd postgresql-contrib python3-devel python3-pip redis -y
RUN mkdir /opt/conplot
RUN curl https://codeload.github.com/rigdenlab/conplot/tar.gz/v0.1 | tar zx -C /opt/conplot/
WORKDIR /opt/conplot/conplot-0.1
RUN pip3 install -r requirements.txt
