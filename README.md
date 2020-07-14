# ConPlot: Online Analysis of Contact Plots

[![Heroku App Status](http://heroku-shields.herokuapp.com/random-cheesecake)](https://random-cheesecake.herokuapp.com/conplot)
[![CI Status](https://travis-ci.com/rigdenlab/conplot.svg?branch=master)](https://travis-ci.com/rigdenlab/conplot)
![Docker Automated build](https://img.shields.io/docker/automated/filosanrod/conplot)

## About ConPlot


ConPlot is a web-based application for the visualisation of information
derived from residue contact predictions in combination with other
sources of information, such as secondary structure predictions,
transmembrane helical topology, sequence conservation. The plot allows
the visual cross-referencing of sequence-based prediction data from
multiple sources. The exploitation of this novel cross-referencing
method can be useful to potentially expose structural features that
would otherwise go undetected. Developed by the the
[Rigden](https://github.com/rigdenlab) group at the [University of
Liverpool](https://www.liverpool.ac.uk/), this new tool provides an
interactive interface for researchers in the field of protein
bioinformatics that are interested in analysing data on a given protein
at a glance.

## Using ConPlot


ConPlot is a web-based application that can be used 
[here](https://random-cheesecake.herokuapp.com/conplot/). Alternatively,
it is also possible to use ConPlot locally on your personal machine using 
the localhost. There are two possible ways to achieve this.

### Using Docker image at DockerHub

ConPlot is distributed as a docker image on the project's 
[Docker hub repository](https://hub.docker.com/r/filosanrod/conplot). To use it, you will need to link it with a Redis 
container:

```bash
$   docker pull filosanrod/conplot:latest
$   docker run --name redis_db -d redis:latest
$   docker run --name conplot_app --link redis_db:redis -e REDISCLOUD_URL="redis://redis_db:6379" -p 5000:5000 -d filosanrod/conplot:latest gunicorn app:server --preload --workers=6 --timeout 120 --graceful-timeout 120 --max-requests 5 --log-level=info -b :5000
```

However, if you want to deploy ConPlot as a docker container, we recommend you automate the creation of the 
multiple containers required to run the app using the `static/docker/docker-compose.yml` file. Do this by running:

```bash 
$   git clone https://github.com/rigdenlab/conplot
$   cd conplot/static/docker
$   docker-compose up -d
```

After you set up running the docker container, you will be able to access the app on `http://0.0.0.0:5000/conplot`.

### Locally using Flask development server

It is also possible to use Flask development server to run ConPlot on your localhost. 
To do this you will first need to install `redis`, which is  the cache memory server used by ConPlot.

```bash
$   sudo apt update
$   sudo apt install redis-server
```

Once you have installed `redis`, you will need to start the service by running:

```bash
$   sudo service redis start
```

You will also need to create a environment variable called `REDISCLOUD_URL` with 
the URL to connect to the redis server you just started on your machine:

```bash
$   REDISCLOUD_URL=redis://localhost:6379
```

After this, all you need to do is clone this repository, install the requirements 
and start the Flask development server on your machine. Please note that ConPlot 
requires at least `python 3.6`.

```bash
$   git clone https://github.com/rigdenlab/conplot
$   cd conplot
$   python3.6 -m pip install -r requirements
$   python3.6 app.py
```

Now you will be able to access the app on `http://127.0.0.1:8050/conplot`. Please 
note that when running locally, ConPlot will not be able to establish a connection 
with our database, so all the user account related features will be disabled. Similarly, 
you will not be able to get in touch with us using the "Get in touch" tab.
