import sys
import os
import configparser

def crackMenu():
	print("1. Crack a WEP/WPA/WPA2 key with a wordlist")
	print("2. Crack a WEP key with IVs")
	print("3. Crack a WEP key with IVs using KoreK method")
	
def crackInput():
	crackMenu()
	if command == "1":
		keyCrack(config)
	elif command == "2":
			wepCrack(config)
	elif command == "3":
			wepCrackKoreK(config)
	else:
		return

def keyCrack(config):
	#Aircrack command to crack the key in the traffic dump
	wordList = config['host']['wordlist']
	bssid = config['ap']['bssid']
	capFile = input("Please specify a capture file: ")
	cmd = "sudo aircrack-ng -w " + wordList + " -b " + bssid + " " + capFile
	os.system(cmd)

def wepCrack(config):
    #Aircrack command to crack the key in the traffic dump
    	bssid = config['ap']['bssid']
    	capFile = input("Please specify a capture file: ")
    	cmd = "sudo aircrack-ng -b " + bssid + " " + capFile

def wepCrackKoreK(config):
    #Aircrack command to crack the key in the traffic dump
    	bssid = config['ap']['bssid']
    	capFile = input("Please specify a capture file: ")
		cmd = "sudo aircrack-ng -K -b " + bssid + " " + capFile
