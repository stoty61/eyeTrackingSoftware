import socket
import sys
import pandas as pd
from datetime import datetime

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

BUFFER_SIZE = 1024

# Bind the socket to the port
server_address = ("192.168.17.174", 9013)

sock.connect(server_address)
data=[]
pupilx = 0
pupily = 1
qr1x = 0
qr1y = 0
qr2x =0
qr3x = 0
qr4x = 0
qr2y = 0
qr3y =0
qr4y = 0
check = []
valid = False
initialize = 200

# going up is negativbe
# going right is positive
def checkRegion(row, pupilx, pupily, qr1x, qr1y, qr2x, qr2y, qr3x, qr3y, qr4x, qr4y):
	if (row[pupily] < row[qr1y] or row[pupily] < row[qr2y]):
		print("Looking above of qr code region")
		return (1)

	elif (row[pupilx] < row[qr1x] or row[pupilx] < row[qr3x]):
		print("looking to the left of qr code region")
		return (1)

	elif (row[pupilx] > row[qr2x] or row[pupilx] > row[qr4x]):
		print("looking to the right of qr code region")
		return (1)

	elif (row[pupily] > row[qr3y] or row[pupily] > row[qr4y]):
		print("Looking below of qr code region")
		return (1)

	else:
		return (0)

## total time = time at point 1000 - time at point 0
#avg time = total time / length of list
def getAvgTime(lis):
	totTime = (datetime.fromtimestamp(lis[lis.len][0]) - datetime.fromtimestamp(lis[0][0])).totaltime()
	return (totTime / lis.len)

while True:
	line = str(sock.recv(1024))
	row = line.replace("\\n", "").replace("\\r","").split("\\t")
	row[-1] =row[-1].strip()
	doublerows = [float(i) for i in row]
	data.append(doublerows)
	#print(sock.recv(1024))
	binary = checkRegion(row, pupilx, pupily, qr1x, qr1y, qr2x, qr2y, qr3x, qr3y, qr4x, qr4y)
	check.append(binary)
	if (len(data) == initialize):
		time = getAvgTime(data)
	if (len(data)> 2/time): # number/sec *2 sec
		check = check[1:]
		if (sum(check)/len(check) > 0.95):
			print("EXTREME WARNING")
