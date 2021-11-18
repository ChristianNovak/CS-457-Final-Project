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
		elif command == "3":
			#Fire airodump-ng
			capture(runtimeData)
		elif command == "4":
			#Fire aircrack-ng
			crack(runtimeData)
		elif command == "5":
			#Fire airmon-ng
			listDevices(runtimeData)
			command = "-1"
		elif command == "6":
			switchNIC(runtimeData)
			command = "-1"
		elif command == "?":
			usage()
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
	apMAC = input("AP MAC: ")
	supMAC = input("Target client MAC: ")
	#Aireplay command to send deauth packets
	cmd = " aireplay-ng -0 1 -a " + apMAC + " -c " + supMAC + " " + runtimeData.userNic
	os.system(cmd)

def setPromisc(runtimeData):
	#Airmon command to set nic to promiscous
	if sys.platform == "win32":
		cmd = "idk how to escalate permissions in windows"
	else:
		cmd = "sudo airmon-ng start " + runtimeData.userNic

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
	cmd = ""
	
def crack(runtimeData):
	#Aircrack command to crack the key in the traffic dump
	cmd = ""

if __name__ == '__main__':
    main()
 