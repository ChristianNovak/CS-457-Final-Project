import sys
import os

def graphMenu():
	print("1. Create a Client to Access Point Relationship Graph")
	print("2. Create a Client to Probe Request Graph")
	
def graphInput():
	graphMenu()
	command = input("> ")
	if command == "1":
		clientAPGraph()
	elif command == "2":
		clientProbeGraph()
	else:
		return

def clientAPGraph():
	print("Please specify the source CSV file:")
	csv = input("> ")
	print("Please specify the output PNG file:")
	png = input("> ")
	
	cmd = "sudo airgraph-ng -i " + csv + " -o " + png + " -g CAPR"
	os.system(cmd)
	
def clientProbeGraph():
	print("Please specify the source CSV file:")
	csv = input("> ")
	print("Please specify the output PNG file:")
	png = input("> ")
	
	cmd = "sudo airgraph-ng -i " + csv + " -o " + png + " -g CPG"
	os.system(cmd)
