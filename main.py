#!/bin/python
import sys
import os
import configparser

import nic as nic
import configuration as configuration
import injection as injection
import capture as capture
import crack as crack
import graph as graph

# Store user configuation
config = configparser.ConfigParser()

# Main script starts here
def main():
	# Check passed args
	if len(sys.argv) < 2:
		configPath = configuration.newFile()
			
	else:
		configPath = sys.argv[1]
	
	config.read(configPath)
	
	# Initialize loop
	#print("Using channel " + config['host']['channel'] + " on " + config['host']['nic'] + "\n")
	inputLoop(config, configPath)

def usage():
	if sys.platform == "win32":
		print("usage: python " + __file__ + " <device name> [channel]")
	else:
		print("usage: ./" + __file__ + " <device name> [channel]")

def inputLoop(config, configPath):
	#Infinitely loop until program is exited
	command = "-1"
	while command == "-1":
		#Display menu info and prompt
		menu()
		command = input("> ")
		#Show configuration menu
		if command == "1":
			configuration.configInput(config, configPath)
			command = "-1"
		elif command == "2":
			#Show NIC menu
			#nic.nicMenu()
			nic.nicInput(config)
			command = "-1"
		elif command == "3":
			#Show Injection menu
			injection.injectionMenu(config)
			command = "-1"
		elif command == "4":
			#show Capture menu
			capture.captureInput(config)
			command = "-1"
		elif command == "5":
			#Show Cracking menu
			crack.crackInput(config)
			command = "-1"
		elif command == "6":
			#Show Graphing menu
			graph.graphInput()
			command = "-1"
		elif command == "?":
			usage()
			command = "-1"
		elif command == "quit" or command == "exit" or command == "e" or command == "q":
			break;
		else:
			menu()
			command = "-1"

def menu():
	print("1. Configuration Commands")
	print("2. NIC Commands")
	print("3. Injection Commands")
	print("4. Capture Commands")
	print("5. Cracking Commands")
	print("6. Graphing Commands")
	print("?  Usage")
	print("Enter one of the above commands:")

if __name__ == '__main__':
    main()
 
