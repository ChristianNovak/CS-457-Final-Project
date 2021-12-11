import sys
import os
import configparser

def crackMenu():
	print("1. Crack a WEP/WPA/WPA2 key")
	
def crackInput():
	crackMenu()
	if command == "1":
		keyCrack(config)
	else:
		return

def keyCrack(config):
	#Aircrack command to crack the key in the traffic dump
	wordList = config['host']['wordlist']
	bssid = config['ap']['bssid']
	capFile = input("Please specify a capture file: ")
	cmd = "sudo aircrack-ng -w " + wordList + " -b " + bssid + " " + capFile
	os.system(cmd)
