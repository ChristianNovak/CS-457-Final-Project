import configparser

def newFile():
	print("It seems you did not specify a configuration file. Let's help you create a new one.\n")
	print("Specify the filepath to which you would like to save your configuration file.\n")
	filePath = input("> ")
	
	print("Please enter the BSSID of your target WAP:\n")
	bssid = input("> ")
	print("Please enter a MAC address for the target client on your network:\n")
	target = input("> ")
	print("Please enter the wireless NIC you wish to use:\n")
	nic = input("> ")
	print("Please enter the channel you will be using:\n")
	channel = input("> ")
	print("Please enter the wordlist file you will be using for cracking operations:\n")
	wordList = input("> ")
	
	newConfig = configparser.ConfigParser()
	
	newConfig['ap']['bssid'] = bssid
	newConfig['target']['mac'] = target
	newConfig['host']['nic'] = nic
	newConfig['host']['channel'] = channel
	newConfig['host']['wordlist'] = wordList
	
	with open(filePath, 'w') as configFile:
		newConfig.write(configFile)
	
	return filePath
	

def configMenu():
	print("1. Set WAP BSSID\n")
	print("2. Set Default NIC\n")
	print("3. Set Injection Target\n")
	print("4. Set Wireless Channel\n")
	print("5. Set Default Wordlist\n")
	
def configInput(config):
	configMenu()
	command = "-1"
	command = input("> ")
	if command == "1":
		listDevices(config)
	elif command == "2":
		switchNIC(config)
	elif command == "3":
		setPromisc(config)
	elif command == "quit" or command == "exit" or command == "e" or command == "q":
		command = "-1"
	else:
		menu()
		
		
def setBSSID(config, filePath):
	print("Please enter the BSSID of your target WAP: \n")
	bssid = input("> ")
	config['ap']['bssid'] = bssid
	
	with open(filePath, 'w') as configFile:
		config.write(configFile)
	configFile.close()

def setNIC(config):
	print("Please enter the wireless NIC you wish to use: \n")
	nic = input("> ")
	config['host']['nic'] = nic
	
	with open(filePath, 'w') as configFile:
		config.write(configFile)
	configFile.close()

def setTarget(config):
	print("Please enter a MAC address for the target client on your network:\n")
	target = input("> ")
	config['target']['mac'] = target
	
	with open(filePath, 'w') as configFile:
		config.write(configFile)
	configFile.close()

def setChannel(config):
	print("Please enter the channel you will be using:\n")
	channel = input("> ")
	config['host']['channel'] = channel
	
	with open(filePath, 'w') as configFile:
		config.write(configFile)
		
	configFile.close()

def setWordList(config):
	print("Please enter the wordlist file you will be using for cracking operations:\n")
	wordList = input("> ")
	config['host']['wordlist'] = wordList
	
	with open(filePath, 'w') as configFile:
		config.write(configFile)
		
	configFile.close()
