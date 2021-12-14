import sys
import os
import configparser
import subprocess as subprocess
import time

def krackMenu():
	print("1. Check a WAP for FT authentication (KRACK vulnerability)")

def krackInput(config):
	krackMenu()
	command = input("> ")
	if command == "1":
		apCheck(config)
	else:
		return

def apCheck(config):
	nic = config['host']['nic']
	ssid = config['ap']['ssid']
	psk = config['ap']['psk']
	
	#Prompt user for file path to supplicant file
	print("Please enter a filepath for the temporary WPA supplicant file")
	path = input("> ")
	
	supplicantFile = open(path, "w")
	
	#Write data to krack config file
	supplicantFile.write("ctrl_interface=/var/run/wpa_supplicant\nnetwork={\n\tssid=\"" + ssid + 
		"\"\n\tkey_mgmt=NONE\n\tpsk=\"" + psk + "\"\n}")
	
	#Close the supplicant file
	supplicantFile.close()
	
	#Disable wifi
	cmd = "sudo service network-manager stop"
	os.system(cmd)
	
	
	#sleep(2)
	
	#Enable krack to use wifi
	cmd = "sudo rfkill unblock wifi"
	os.system(cmd)
	
	#Kill existing wpa_supplicant instances
	cmd = "sudo killall wpa_supplicant"
	os.system(cmd)
	
	time.sleep(2)
	#Issue the command to check for FT authentication
	cmd = "sudo wpa_supplicant -D nl80211 -i " + nic + " -c " + path
	os.system(cmd)
	
	#Re-enable wifi
	cmd = "sudo service network-manager start"
	os.system(cmd)
	
