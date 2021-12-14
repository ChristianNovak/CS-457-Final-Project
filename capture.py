import sys
import os
import configparser

def captureMenu():
	print("1. Start a packet capture")

def captureInput(config):
	captureMenu()
	command = input("> ")
	if command == "1":
		capture(config)
	else:
		return

#Airodump command to capture authentication traffic
def capture(config):
	#Get appropriate values from config
	bssid = config['ap']['bssid']
	nic = config['host']['monitor_nic']
	channel = config['host']['channel']
	
	#Promt the user for a capture file
	capFile = input("Please specify a capture file to save to: ")
	
	#Issue airodump command to capture 802.11 traffic
	cmd = "sudo airodump-ng -c " + channel + " --bssid " + bssid + " -w " + capFile + " " + nic
	os.system(cmd)
