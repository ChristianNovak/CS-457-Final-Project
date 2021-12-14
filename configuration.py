import configparser

def newFile():
	print("It seems you did not specify a configuration file. Let's help you create a new one.")
	print("Specify the filepath to which you would like to save your configuration file.")
	filePath = input("> ")
	
	print("Please enter the SSID of your target WAP:")
	ssid = input("> ")
	print("Please enter the BSSID of your target WAP:")
	bssid = input("> ")
	print("Please enter the PSK of your target WAP (if known, otherwise leave blank)")
	psk = input("> ")
	print("Please enter a MAC address for the target client on your network:")
	target = input("> ")
	print("Please enter the wireless NIC you wish to use:")
	nic = input("> ")
	print("Please enter the channel you will be using:")
	channel = input("> ")
	print("Please enter the wordlist file you will be using for cracking operations:")
	wordList = input("> ")
	
	print("Please enter the path to your dragonslayer installation directory (Only for WPA3 DragonBlood Testing, leave blank otherwise):")
	dragonslayerDir = input("> ")
	
	newConfig = configparser.ConfigParser()
	
	newConfig.add_section('ap')
	newConfig.add_section('target')
	newConfig.add_section('host')
	
	newConfig.add_section('dragonblood')
	
	newConfig['ap']['ssid'] = ssid
	newConfig['ap']['bssid'] = bssid
	newConfig['ap']['psk'] = psk
	newConfig['target']['mac'] = target
	newConfig['host']['nic'] = nic
	newConfig['host']['monitor_nic'] = nic + "mon"
	newConfig['host']['channel'] = channel
	newConfig['host']['wordlist'] = wordList
	
	newConfig['dragonblood']['dragonslayerDir'] = dragonslayerDir
	
	with open(filePath, 'w') as configFile:
		newConfig.write(configFile)
	
	return filePath
	

def configMenu():
	print("1. Set WAP BSSID")
	print("2. Set Default NIC")
	print("3. Set Injection Target")
	print("4. Set Wireless Channel")
	print("5. Set Default Wordlist")
	
def configInput(config, configPath):
	configMenu()
	command = "-1"
	command = input("> ")
	if command == "1":
		setBSSID(config, configPath)
	elif command == "2":
		setNIC(config, configPath)
	elif command == "3":
		setTarget(config, configPath)
	elif command == "4":
		setChannel(config, configPath)
	elif command == "5":
		setChannel(config, configPath)
	else:
		return
		
		
def setBSSID(config, filePath):
	print("Please enter the BSSID of your target WAP:")
	bssid = input("> ")
	config['ap']['bssid'] = bssid
	
	with open(filePath, 'w') as configFile:
		config.write(configFile)
	configFile.close()

def setNIC(config, filePath):
	print("Please enter the wireless NIC you wish to use:")
	nic = input("> ")
	config['host']['nic'] = nic
	
	with open(filePath, 'w') as configFile:
		config.write(configFile)
	configFile.close()

def setTarget(config, filePath):
	print("Please enter a MAC address for the target client on your network:")
	target = input("> ")
	config['target']['mac'] = target
	
	with open(filePath, 'w') as configFile:
		config.write(configFile)
	configFile.close()

def setChannel(config, filePath):
	print("Please enter the channel you will be using:")
	channel = input("> ")
	config['host']['channel'] = channel
	
	with open(filePath, 'w') as configFile:
		config.write(configFile)
		
	configFile.close()

def setWordList(config, filePath):
	print("Please enter the wordlist file you will be using for cracking operations:")
	wordList = input("> ")
	config['host']['wordlist'] = wordList
	
	with open(filePath, 'w') as configFile:
		config.write(configFile)
		
	configFile.close()
