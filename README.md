# ConPlot: Online Analysis of Contact Plots

[![Actions Status](https://github.com/rigdenlab/conplot/workflows/Test%20&%20Build/badge.svg)](https://github.com/rigdenlab/conplot/actions)
[![Docker Automated build](https://img.shields.io/docker/automated/filosanrod/conplot)](https://hub.docker.com/r/filosanrod/conplot)
[![RRID](https://img.shields.io/badge/RRID-SCR_019216-informational)](https://scicrunch.org/scicrunch/Resources/record/nlx_144509-1/SCR_019216/resolver)
[![DOI](https://img.shields.io/badge/DOI-10.1093%2Fbioinformatics%2Fbtab049-blue.svg)](https://doi.org/10.1093/bioinformatics/btab049)

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
[here](http://www.conplot.org). Alternatively, it is also possible to use ConPlot locally on your personal machine using 
the localhost. There are two possible ways to achieve this.

### Using Docker image at DockerHub

ConPlot is distributed as a docker image on the project's 
[Docker hub repository](https://hub.docker.com/r/filosanrod/conplot). To use it, you will need to link it with a Redis 
container:

```bash
$   docker pull filosanrod/conplot:latest
$   docker run --name redis_db -d redis:latest
$   docker run --name conplot_app --link redis_db:redis -e KEYDB_URL="redis://redis_db:6379" -p 80:80 -d filosanrod/conplot:latest gunicorn app:server --preload --workers=6 --timeout 120 --graceful-timeout 120 --max-requests 5 --log-level=info -b :80
```

After you set up running the docker container, you will be able to access the app on `http://0.0.0.0:80/home`.

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

Now you'll need to clone this repository, install the requirements and setup environment variables. 
Please note that ConPlot requires at least `python 3.6`.

```bash
$   git clone https://github.com/rigdenlab/conplot
$   cd conplot
$   python3.6 -m pip install -r requirements.txt
$   echo "KEYDB_URL=0://localhost:6379" > .env
```

With that last command you will also have created an environment variable called `KEYDB_URL` with 
the URL to connect to the redis server you previously started on your machine. The only thing 
left to do is to start the Flask development server on your machine:

```bash
$   python3.6 app.py
```

Now you will be able to access the app on `http://127.0.0.1:8050/home`. Please 
note that when running locally, ConPlot will not be able to establish a connection 
with our database, so all the user account related features will be disabled. Similarly, 
you will not be able to get in touch with us using the "Get in touch" tab.
