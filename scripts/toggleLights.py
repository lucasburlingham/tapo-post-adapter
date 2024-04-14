from PyP100 import PyL530
from os import system as shell_exec

# This script is used to toggle the lights on and off


# Get username and password from the ../credentials.env file
# The file should contain the username on the first line and the password on the second line
with open('credentials.env', 'r') as f:
	credentials = f.readlines()
	username = credentials[0].strip()
	password = credentials[1].strip()
	url = credentials[2].strip()
	f.close()

# THIS IS WHERE YOU NEED TO CHANGE THE IP ADDRESSES TO MATCH YOUR LIGHTBULBS/PLUGS
#  MINE LOOK LIKE THIS BUT YOURS WILL PROBABLY BE DIFFERENT
# 192.168.1.4 TSM1
# 192.168.1.5 TSM2 
# 192.168.1.6 TSM3 
# 192.168.1.7 TSM4


# Connect to the lightbulbs
# TSM1 = PyL530.L530("192.168.1.4", username, password)
# TSM2 = PyL530.L530("192.168.1.5", username, password)
# TSM3 = PyL530.L530("192.168.1.6", username, password)
TSM4 = PyL530.L530("192.168.1.7", username, password)


# ping the lightbulbs to test if they are connected to the network
result = shell_exec("ping 192.168.1.7 -c1")
if (result == 0):
	print("ping successful")
else:
	print("ping failed")
	exit()

# Get cookies for remainder of session
# TSM1.handshake()
# TSM2.handshake()
# TSM3.handshake()
TSM4.handshake()

# login to the lightbulbs
# TSM1.login()
# TSM2.login()
# TSM3.login()
TSM4.login()

# Get the value of the first line of the ../iterator.env file
with open('iterate.env', 'r') as f:
	iterator = f.readline()
	iterator = int(iterator)
	f.close()

# Toggle the lights
if iterator == 0:
	# TSM1.setBrightness(80)
	# TSM2.setBrightness(80)
	# TSM3.setBrightness(80)
	TSM4.setBrightness(80)
 
	# Set the color temperature to a warm white
	# TSM1.setColorTemp(2700)
	# TSM2.setColorTemp(2700)
	# TSM3.setColorTemp(2700)
	TSM4.setColorTemp(2700)
	
	# Set the color to a warm white
	# TSM1.setColor(30, 80)
	# TSM2.setColor(30, 80)
	# TSM3.setColor(30, 80)
	TSM4.setColor(30, 80)

	iterator = 1
else:
	# TSM1.setBrightness(0)
	# TSM2.setBrightness(0)
	# TSM3.setBrightness(0)
	TSM4.setBrightness(0)
	iterator = 0

# Write the new value of the iterator to the ../iterator.env file
with open('../iterator.env', 'w') as f:
	f.write(str(iterator))
	f.close()
 
