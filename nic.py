import sys
import os
import configparser

def nicMenu():
	#Show available NIC-related commands
	print("1. List available network interfaces")
	print("2. Switch currently selected NIC")
	print("3. Set current NIC to promiscous")
	
def nicInput(config):
	#Arbitrary value for command
	command = "-1"
	
	#Show available commands and prompt
	nicMenu()
	command = input("> ")
	
	#Show available NICs
	if command == "1":
		listDevices()
	#Change the current NIC (does not change config file)
	elif command == "2":
		switchNIC(config)
	#Set current NIC to Promiscous
	elif command == "3":
		setPromisc(config)
	#Return to the main menu
	else:
		return
		

def listDevices():
	#Airmon command to list devices
	cmd = "sudo airmon-ng"
	os.system(cmd)
	
def switchNIC(config):
	#Get names of old and new nic
	oldNic = config['host']['nic']
	newNic = input("Enter NIC device name: ")
	
	#Stop the current nic
	cmd = "sudo airmon-ng stop " + oldNic
	os.system(cmd)
	
	#Start the new nic
	cmd = "sudo airmon-ng start " + newNic
	os.system(cmd)

def setPromisc(config):
	#Read user's NIC from config
	nic = config['host']['nic']
	#Issue airmon command to set NIC to promiscuous
	cmd = "sudo airmon-ng start " + config.userNic
	os.system(cmd)
