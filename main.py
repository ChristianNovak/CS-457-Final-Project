#!/bin/python
import sys

# This class contains state data used throughout the program
# This may need to move to its own file if it gets too large
class RuntimeData:
  def __init__(self, userNic, userChannel):
    self.userNic = userNic
    self.userChannel = userChannel

# Main script starts here
def main():
	if len(sys.argv) < 2:
		print("error: No wireless interface provided\n")
		usage()
		sys.exit(1)

	userChannel = 1
	if len(sys.argv) > 2:
		userChannel = sys.argv[2]

	runtimeData = RuntimeData(sys.argv[1], userChannel)
	print("Using channel " + runtimeData.userChannel + " on " + runtimeData.userNic + "\n")
	inputLoop(runtimeData)

def usage():
	print("usage: " + __file__ + " <device name> [channel]\n")

def inputLoop(runtimeData):
	command = -1

	while command == -1:
		print("1. Issue a deauthentication attack.\n")
		print("2. Set NIC to promiscous mode.\n")
		print("3. Capture an authentication packet.\n")
		print("4. Crack a WPA2 key.\n")
		print("5. Usage")
		
		print("Enter one of the above commands:\n")
		
		command = input("> ")
		
		if command == 1:
			#Fire aireplay-ng
			deauth()
		elif command == 2:
			#Fire airmon-ng
			monitor()
		elif command == 3:
			#Fire airodump-ng
			capture()
		elif command == 4:
			#Fire aircrack-ng
			crack()
		elif command == 5:
			usage()
		else:
			print("Please enter a valid command.\n")
			command = -1
	
def deauth():
	#Aireplay command to send deauth packets
	cmd = ""
	
def monitor():
	#Airmon command to set nic to promiscous
	cmd = ""
	
def capture():
	#Airodump command to capture authentication traffic
	cmd = ""
	
def crack():
	#Aircrack command to crack the key in the traffic dump
	cmd = ""

if __name__ == '__main__':
    main()
 