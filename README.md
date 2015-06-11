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

File `demo.py` is an example of how to launch mininetRest. 
MininetRest accepts a Mininet Object. 'demo.py' instantiates a singleSwitch with 2 hosts.

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
MininetRest class at file `mininet_rest.py` is the core of mininetRest. 
It is a derived class of the Bottle class (http://bottlepy.org/docs/dev/index.html)

## Authoring

* Carlos Giraldo
carlitosgiraldo@gmail.com
AtlantTIC Research Center, University of Vigo, Spain
http://atlanttic.uvigo.es/en/

