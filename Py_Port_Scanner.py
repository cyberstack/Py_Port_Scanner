#!/usr/bin/env python

#-------------------------------------------------------------------------------
# Name:        Py_Port_Scanner
# Purpose:     Simple, quick and easy port scanner 
# Version:     Version 1.0 (P2-20191026)
# Author:      CyberStack
# Created:     26/10/2019
#-------------------------------------------------------------------------------

'''To Do:
    * Error checking for input from users
    * Get local machine's IP as starting point
    * Extra advanced features
'''
import socket
import subprocess
import sys
from datetime import datetime

# Clear screen
subprocess.call('clear', shell=True)

# Prompt for host and end port
remoteServer    = raw_input("Enter a remote host to scan: ")
endPort    = raw_input("Scan port 1 to: ")
subprocess.call('clear', shell=True)
remoteHostIP  = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print "-" * 35
print "Scanning remote host", remoteHostIP
print "-" * 35

# Check scan start time
scan_Start = datetime.now()

# We also put in some error handling for catching errors

try:
    for port in range(1,int(endPort)):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteHostIP, port))
        if result == 0:
            print "Port {}:  ---------->	 Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Host could not be found. Good bye'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()

# Checking current time
scan_Stop = datetime.now()

# Calculates the port scan time 
scan_Time =  scan_Stop - scan_Start

# Output of port scan
print 'Scanning Completed in: ', scan_Time

# Ref & Cred - Inspired by code from 
# https://www.pythonforbeginners.com/code-snippets-source-code/port-scanner-in-python/
