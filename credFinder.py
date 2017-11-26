#!/usr/bin/env python
# -*-coding:Utf-8 -*

# File to return credentials stocked in another secured file

import re
import base64

def returnCred():
	# Get credentials from MySQL Python Agent config file
	fid = open('/home/ubuntu/pythonAgent.conf', 'r')
	ConfigFileBody = fid.read()
	fid.close()

	# Parse credentials
	Username = re.findall(r'USER\=(.*)\n', ConfigFileBody)[0]
	Password = re.findall(r'PASS\=(.*)\n', ConfigFileBody)[0]

	mypassword=base64.b64decode(Password).decode('utf-8')

	return(Username, mypassword)
