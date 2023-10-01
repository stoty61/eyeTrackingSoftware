# Establish TCP connection with D-Lab data relay
# Last updated May 10, 2022 by Charlie
# TEST VERSION

# import python default libraries
import socket
import sys


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def connect(ip_address, port):
	"""
	connect the TCP to D-Lab
	"""
	# (IP address, port) - as shown in D-Lab
	server_address = (ip_address, port)

	# connect the sock to the server address and port
	sock.connect(server_address)

def data_relay():
	"""
	data transmission using TCP
	"""
	return sock.recv(1024)
