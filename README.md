mininetRest: A REST API for mininet
========================================================

mininetRest 0.0.1

## Dependencies
* Bottle Web framework:
    `sudo pip install bottle`
* mininet:
    see http://mininet.org/download/

## How to use mininetRest?

MininetRest is a Bottle Web Application that wraps a Mininet Object
and allows to interact with Mininet through a REST API.

File `demo.py` is an example of how to launch mininetRest. First, a mininet
network should be configure. Then, the mininet network is passed in the constructor
of MininetRest and the method run is called to start the webApplication.

In order to test the launched webapp, we provide a postman collection (https://www.getpostman.com/)
that illustrate the available requests. The collection is the file `mininet-api.json.postman_collection`

## What can we do with the REST API?
At the moment the REST API allows:
* get a list of the mininet nodes. 
* get a list of the mininet hosts. 
* get a list of the mininet switches. 
* get a list of the mininet links.
* get the interfaces of a node.
* set an interface of a node up or down.
* set the bandwidth and delay of an interface of a node.
* execute a command in a node.

## How is it implemented?
File `mininet_rest.py` is the core of mininetRest. The main class is MininetRest,
derived from the Bottle Web Framework (http://bottlepy.org/docs/dev/index.html)

## Authoring

* Carlos Giraldo
carlitosgiraldo@gmail.com
AtlantTIC Research Center, University of Vigo, Spain
http://atlanttic.uvigo.es/en/

