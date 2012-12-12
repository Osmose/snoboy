from array import array
from ctypes import c_ubyte

cart_data = array('B')

def loadCart(filename):
	global cart_data
	f = open(filename, 'rb')
	
	# Move to end and get the filesize
	f.seek(0,2)
	size = f.tell()
	f.seek(0,0)

	# Read the file
	cart_data = (c_ubyte * size)()
	f.readinto(cart_data)

	#cart_data is now loaded