from mininet.net import Mininet
from mininet.link import TCLink
from mininet.node import OVSController
from mininet_rest import MininetRest
from mininet.topo import SingleSwitchTopo

net = Mininet(topo=SingleSwitchTopo(k=2),controller=OVSController,link=TCLink)

net.start()
mininet_rest = MininetRest(net)
mininet_rest.run()
net.stop()
