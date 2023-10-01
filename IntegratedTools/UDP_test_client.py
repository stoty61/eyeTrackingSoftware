import socket
import time
import random

# msgFromClient = "Test Msg 1"

# bytesToSend = str.encode(msgFromClient)

serverAddressPort = ("127.0.0.1", 20001)

bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
while True:
    rng = random.random()
    msg = ""
    if (rng < 0.95):
        msg = "111111, false1"
    else:
        msg = "999999, true1"
    UDPClientSocket.sendto(str.encode(msg), serverAddressPort)
    time.sleep(0.20) 
