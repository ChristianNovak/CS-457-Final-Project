import json

def newFile():
	print("It seems you did not specify a configuration file. Let's help you create a new one.\n")
	print("Specify the filepath to which you would like to save your configuration file.\n")
	filePath = input("> ")
	print("Please enter the BSSID of your target WAP:\n")
	bssid = input("> ")
	print("Please enter the wireless NIC you wish to use:\n")
	nic = input("> ")
	
	configData = {
		"bssid": bssid,
		"nic": nic
	}
	
	configFile = open(filePath, "w")
	json.dump(configData, configFile)
	configFile.close()
	
	return filePath
	

def configMenu():
	print("1. Set WAP BSSID")
	print("2. Set Default NIC")
	
def configInput(runtimeData):
	configMenu()
	command = "-1"
	command = input("> ")
	if command == "1":
		listDevices(runtimeData)
	elif command == "2":
		switchNIC(runtimeData)
	elif command == "3":
		setPromisc(runtimeData)
	elif command == "quit" or command == "exit" or command == "e" or command == "q":
		command = "-1"
	else:
		menu()
		
		
def setBSSID(runtimeData):
	print("Please enter the BSSID of your target WAP: \n")
	bssid = input("> ")
	configFile = open(runtimeData.configFile)
	jsonFile = json.load(configFile)
	jsonFile["bssid"] = bssid
	jsonFile = json.dump(configFile)
	
	

def setNIC(runtimeData):
	print("Please enter the wireless NIC you wish to use: \n")
	nic = input("> ")
	configFile = open(runtimeData.configFile)
	jsonFile = json.load(configFile)
	jsonFile["nic"] = nic
	jsonFile = json.dump(configFile)
