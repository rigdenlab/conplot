# ConPlot: Online Analysis of Contact Plots

[![Heroku App Status](http://heroku-shields.herokuapp.com/random-cheesecake)](https://random-cheesecake.herokuapp.com/conplot)
[![CI Status](https://travis-ci.com/rigdenlab/conplot.svg?branch=master)](https://travis-ci.com/rigdenlab/conplot)

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
your local host. To do this, first install `redis`, which is the cache memory
service used by ConPlot.

```bash
$   sudo apt update
$   sudo apt install redis-server
```

Once you have installed redis, you will need to start the service by running:

```bash
$   sudo service redis start
```

After this, all you need to do is clone this repository, install the requirements 
and start the Flask development server on your machine. 

```bash
$   git clone https://github.com/rigdenlab/conplot
$   cd conplot
$   python3.6 -m pip install -r requirements
$   python3.6 app.py
```

Now you will be able to access the app on http://127.0.0.1:8050/conplot/
