#!/usr/bin/python
import time
from threading import Thread
import os
import commands

bridge_list = ['s1','s2','s3','s4','s5','s6','s7','s8','s9','s10']
c1 = ['s1','s3','s4','s5','s6']
c2 = ['s2','s7','s8','s9','s10']

while True:

	time.sleep(3)
	#hostname = "127.0.0.1:6633"
	#response = os.system("ping -c 1 " + hostname)

	reponse = ""
	for i in range(1,10):
		response = commands.getstatusoutput("sudo ovs-vsctl get controller "+ bridge_list[i] + " is_connected")
		#print(response)
		if response[1] == "false":
			#print[bridge_list[i]]
			if bridge_list[i] in c1:
				os.system("sudo ovs-vsctl set-controller " +bridge_list[i]+ " tcp:127.0.0.1:6639")
				print(bridge_list[i]+" connected c2")
			elif bridge_list[i] in c2:
				os.system("sudo ovs-vsctl set-controller " +bridge_list[i]+ " tcp:127.0.0.1:6633")
				print(bridge_list[i]+" connected c1")
		
	#	if response==true:
	#	print("ping geliyor abi")
	#else: 
	#	print("gelmiyor abi")

	
	