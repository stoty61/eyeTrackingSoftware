# this TCP server should be run on the MiniSim computer for alart purposes
# all bytes-like information should be encoded in utf-8

import socket

# set up the server information
host = "192.168.17.19" # IP Address of the MiniSim computer
# dlab_port = 25565 # port to listen from d-lab
sim_port = 28960 # a designated port to receive information

# function to establish d-lab and mini-sim connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((host, sim_port))
    sock.listen()
    conn, addr = sock.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode("utf-8"))
