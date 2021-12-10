import sys
import os

def nicMenu():
	
	print("1. List available network interfaces")
	print("2. Switch currently selected NIC")
	print("3. Set current NIC to promiscous")
	
def nicInput(runtimeData):
	command = "-1"
	command = input("> ")
	if command == "1":
		listDevices(runtimeData)
	elif command == "2":
		switchNIC(runtimeData)
	elif command == "3":
		setPromisc(runtimeData)
	elif command == "quit" or command == "exit" or command == "e" or command == "q":
		command = "-1"
	else:
		menu()
		

def listDevices(runtimeData):
	#Airmon command to list devices
	cmd = "sudo airmon-ng"
	os.system(cmd)
	
def switchNIC(runtimeData):
	newNic = input("Enter NIC device name: ")
	cmd = "sudo airmon-ng stop " + runtimeData.userNic
	runtimeData["nic"] = command
	os.system(cmd)

def setPromisc(runtimeData):
	cmd = "sudo airmon-ng start " + runtimeData.userNic
	os.system(cmd)
