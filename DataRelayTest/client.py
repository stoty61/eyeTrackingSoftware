# this TCP server and client should be run on the D-Lab computer for data relay
# all bytes-like information should be encoded in utf-8

import socket

# set up the server information for receiving information from D-Lab
dlab_host = "192.168.17.174" # IP Address of the MiniSim computer
dlab_port = 25566 # port to listen from d-lab


# function to establish d-lab and mini-sim connection
dlab_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dlab_sock.connect((dlab_host, dlab_port))




# set up the MiniSim TCP server information
host = "192.168.17.19" # IP Address of the MiniSim computer
sim_port = 28960 # a designated port on the MiniSim computer to send information to


# function that receives the information from the server
send_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
send_sock.connect((host, sim_port))

while True:
    data = dlab_sock.recv(1024)
    send_sock.sendall(data)  # send the data received from D-Lab
    if not data:
        break

    """
    test information

    for i in range(1000):
        statement = "Client send to server, test message " + str(i) + "\n"
        sock.sendall(bytes(statement, "utf-8"))
    """
