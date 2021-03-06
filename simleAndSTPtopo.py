#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def myTopo():

    net = Mininet(controller=RemoteController, switch=OVSKernelSwitch)

    c1 = net.addController('c1', controller=RemoteController, ip="127.0.0.1", port=6633)
    c2 = net.addController('c2', controller=RemoteController, ip="127.0.0.1", port=6639)

    h1 = net.addHost( 'h1', ip='10.0.0.1' )
    h2 = net.addHost( 'h2', ip='10.0.0.2' )
    h3 = net.addHost( 'h3', ip='10.0.0.3' )
    h4 = net.addHost( 'h4', ip='10.0.0.4' )
    h5 = net.addHost( 'h5', ip='10.0.0.5' )
    h6 = net.addHost( 'h6', ip='10.0.0.6' )
    h7 = net.addHost( 'h7', ip='10.0.0.7' )
    h8 = net.addHost( 'h8', ip='10.0.0.8' )
    h9 = net.addHost( 'h9', ip='10.0.0.9' )
    h10 = net.addHost( 'h10', ip='10.0.0.10' )

    s1 = net.addSwitch( 's1' )
    s2 = net.addSwitch( 's2' )

    s3 = net.addSwitch( 's3' )
    s4 = net.addSwitch( 's4' )
    s5 = net.addSwitch( 's5' )
    s6 = net.addSwitch( 's6' )

    s7 = net.addSwitch( 's7' )
    s8 = net.addSwitch( 's8' )
    s9 = net.addSwitch( 's9' )
    s10 = net.addSwitch( 's10' )

    s1.linkTo( s2 )

    net.addLink( s1 , s3 )
    net.addLink( s3 , s4 )
    net.addLink( s3 , s5 )
    net.addLink( s5 , s6 )

    s2.linkTo( s7 )
    s2.linkTo( s8 )    
    s7.linkTo( s8 )
    s7.linkTo( s9 )
    s7.linkTo(s10 )
    s8.linkTo( s9 )

    s3.linkTo( h1 )
    s3.linkTo( h2 )
    s4.linkTo( h3 )
    s5.linkTo( h4 )
    s6.linkTo( h5 )

    s7.linkTo( h6 )
    s7.linkTo( h7 )
    s8.linkTo( h8 )
    s9.linkTo( h9 )
    s10.linkTo(h10)

    net.build()
    
    s1.start([c1])
    s2.start([c2])
    s3.start([c1])
    s4.start([c1])
    s5.start([c1])
    s6.start([c1])
    s7.start([c2])
    s8.start([c2])
    s9.start([c2])
    s10.start([c2])

    h3.cmd('python -m SimpleHTTPServer 80 &')
    h5.cmd('python -m SimpleHTTPServer 80 &')
    h7.cmd('python -m SimpleHTTPServer 80 &')
    h9.cmd('python -m SimpleHTTPServer 80 &')

    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myTopo()
