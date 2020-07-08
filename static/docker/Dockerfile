FROM centos:8 AS build
RUN dnf update -y
RUN dnf install curl gcc initscripts postgresql-server postgresql-contrib python3-devel python3-pip redis systemd  -y
RUN mkdir /opt/conplot
RUN curl https://codeload.github.com/rigdenlab/conplot/tar.gz/v0.2.2 | tar zx -C /opt/conplot/
WORKDIR /opt/conplot/conplot-0.2.2
RUN pip3 install -r requirements.txt
