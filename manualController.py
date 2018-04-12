#!/usr/bin/python
import time
from threading import Thread
import os
import commands

bridge_list = ['s1','s2','s3','s4','s5','s6','s7','s8','s9','s10']

while True:

	time.sleep(3)

	reponse = ""
	for i in range(1,10):
		getcontr = commands.getstatusoutput("sudo ovs-vsctl get-controller "+ bridge_list[i])
		if(getcontr[1] == "tcp:127.0.0.1:6633"):
			response = commands.getstatusoutput("sudo ovs-vsctl get controller "+ bridge_list[i] + " is_connected")
			if response[1] == "false":
				os.system("sudo ovs-vsctl set-controller " +bridge_list[i]+ " tcp:127.0.0.1:6639")
				print("switch :: "+bridge_list[i]+" is connected to controller:c2")
		elif(getcontr[1] == "tcp:127.0.0.1:6639"):
			response = commands.getstatusoutput("sudo ovs-vsctl get controller "+ bridge_list[i] + " is_connected")
			if response[1] == "false":
				os.system("sudo ovs-vsctl set-controller " +bridge_list[i]+ " tcp:127.0.0.1:6633")
				print("switch :: "+bridge_list[i]+" is connected to controller:c1")

	
	
