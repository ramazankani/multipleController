#!/bin/bash

sudo ovs-vsctl set-controller s1 tcp:127.0.0.1:6633
sudo ovs-vsctl set-controller s3 tcp:127.0.0.1:6633
sudo ovs-vsctl set-controller s4 tcp:127.0.0.1:6633
sudo ovs-vsctl set-controller s5 tcp:127.0.0.1:6633
sudo ovs-vsctl set-controller s6 tcp:127.0.0.1:6633
sudo ovs-vsctl set-controller s2 tcp:127.0.0.1:6639
sudo ovs-vsctl set-controller s7 tcp:127.0.0.1:6639
sudo ovs-vsctl set-controller s8 tcp:127.0.0.1:6639
sudo ovs-vsctl set-controller s9 tcp:127.0.0.1:6639
sudo ovs-vsctl set-controller s10 tcp:127.0.0.1:6639