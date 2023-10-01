# import python default libraries
import socket

def connect():
	"""
	connect the TCP to D-Lab
	"""
	# set up the server information for receiving information from D-Lab
	dlab_host = "192.168.17.174" # IP Address of the MiniSim computer
	dlab_port = 9015 # port to listen from d-lab (default value)


	# function to establish d-lab and mini-sim connection
	dlab_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	dlab_sock.connect((dlab_host, dlab_port))
	return dlab_sock


def data_relay(sock):
	"""
	data transmission using TCP
	"""
	return sock.recv(1024)
