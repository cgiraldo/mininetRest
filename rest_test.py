from mininet.net import Mininet
from mininet.link import TCLink
from mininet.node import OVSController
from mininet_rest import MininetRest
from mininet.cli import CLI

import thread

net = Mininet()
net.addHost('h1')
net.addHost('h2')
net.addSwitch('s1')
net.addLink('h1','s1', cls=TCLink, total_bw=123)
net.addLink('h2','s1', cls=TCLink, total_bw=111)
net.addController('c0',controller=OVSController)

net.start()

thread.start_new_thread(CLI, (net,))
print "#############IMPORTANT#################"
print "To quit FIRST write exit to quit mininet CLI and then Ctrl-C to quit Bottle server"
mininet_rest = MininetRest('myapp',net)
mininet_rest.run(quiet=True)
net.stop()