#!/usr/bin/python
from bottle import Bottle, request
import time

"""
MininetRest adds a REST API to mininet.

"""

__author__ = 'Carlos Giraldo'
__copyright__ = "Copyright 2015, AtlantTIC - University of Vigo"
__credits__ = ["Carlos Giraldo"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Carlos Giraldo"
__email__ = "carlitosgiraldo@gmail.com"
__status__ = "Prototype"


class MininetRest(Bottle):
    def __init__(self, net):
        super(MininetRest, self).__init__()
        self.net = net
        self.route('/nodes', callback=self.get_nodes)
        self.route('/nodes/<node_name>', callback=self.get_node)
        self.route('/nodes/<node_name>', method='POST', callback=self.post_node)
        self.route('/nodes/<node_name>/cmd', method='POST', callback=self.do_cmd)
        self.route('/nodes/<node_name>/<intf_name>', callback=self.get_intf)
        self.route('/nodes/<node_name>/<intf_name>', method='POST', callback=self.post_intf)
        self.route('/hosts', method='GET', callback=self.get_hosts)
        self.route('/switches', method='GET', callback=self.get_switches)
        self.route('/links', method='GET', callback=self.get_links)

    def get_nodes(self):
        return {'nodes': [n for n in self.net]}

    def get_node(self, node_name):
        node = self.net[node_name]
        return {'intfs': [i.name for i in node.intfList()], 'params': node.params}

    def post_node(self, node_name):
        node = self.net[node_name]
        node.params.update(request.json['params'])


    def get_intf(self, node_name, intf_name):
        node = self.net[node_name]
        intf = node.nameToIntf[intf_name]
        return {'name': intf.name, 'status': 'up' if intf.name in intf.cmd('ifconfig') else 'down',
                "params": intf.params}

    def post_intf(self, node_name, intf_name):
        node = self.net[node_name]
        intf = node.nameToIntf[intf_name]
        if 'status' in request.json:
            intf.ifconfig(request.json['status'])
        if 'params' in request.json:
            intf_params = request.json['params']
            intf.config(**intf_params)
            intf.params.update(intf_params)

    def get_hosts(self):
        return {'hosts': [h.name for h in self.net.hosts]}

    def get_switches(self):
        return {'switches': [s.name for s in self.net.switches]}

    def get_links(self):
        return {'links': [dict(name=l.intf1.node.name + '-' + l.intf2.node.name,
                               node1=l.intf1.node.name, node2=l.intf2.node.name,
                               intf1=l.intf1.name, intf2=l.intf2.name) for l in self.net.links]}

    def do_cmd(self, node_name):
        args = request.body.read()
        node = self.net[node_name]
        rest = args.split(' ')
        # Substitute IP addresses for node names in command
        # If updateIP() returns None, then use node name
        rest = [self.net[arg].defaultIntf().updateIP() or arg
                if arg in self.net else arg
                for arg in rest]
        rest = ' '.join(rest)
        # Run cmd on node:
        node.sendCmd(rest)
        output = ''
        init_time = time.time()
        while node.waiting:
            exec_time = time.time() - init_time
            #timeout of 5 seconds
            if exec_time > 5:
                break
            data = node.monitor(timeoutms=1000)
            output += data
        # Force process to stop if not stopped in timeout
        if node.waiting:
            node.sendInt()
            time.sleep(0.5)
            data = node.monitor(timeoutms=1000)
            output += data
            node.waiting = False
        return output
