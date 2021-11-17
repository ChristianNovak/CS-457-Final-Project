command = -1

while command == -1:
	print("1. Issue a deauthentication attack.\n")
	print("2. Set NIC to promiscous mode.\n")
	print("3. Capture an authentication packet.\n")
	print("4. Crack a WPA2 key.\n")
	
	print("Enter one of the above commands:\n")
	
	command=input("> ")
	
	if command == 1:
		#Fire aireplay-ng
		deauth()
		
	else if command == 2:
		#Fire airmon-ng
		monitor()
		
	else if command == 3:
		#Fire airodump-ng
		capture()
		
	else if command == 4:
		#Fire aircrack-ng
		crack()
	else:
		print("Please enter a valid command.\n");
		command == -1
	
def deauth():
	#Aireplay command to send deauth packets
	cmd = ""
	
def monitor():
	#Airmon command to set nic to promiscous
	cmd = ""
	
def capture():
	#Airodump command to capture authentication traffic
	cmd = ""
	
def crack():
	#Aircrack command to crack the key in the traffic dump
	cmd = ""
