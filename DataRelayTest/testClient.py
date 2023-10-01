import socket

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
