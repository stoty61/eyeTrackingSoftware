import socket
import sys
import pandas as pd
from datetime import datetime
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

BUFFER_SIZE = 1024

# Bind the socket to the port
server_address = ("192.168.17.174", 9015)

sock.connect(server_address)
data=[]
pupilx = 0
pupily = 1
qr1x = 2
qr1y = 3
qr2x =4
qr2y = 5
qr3x = 6
qr3y =7
qr4x = 8
qr4y=9

check = []
valid = False
initialize = 200

# going up is negativbe
# going right is positive
def checkRegion(row, pupilx, pupily, qr1x, qr1y, qr2x, qr2y, qr3x, qr3y, qr4x, qr4y):
	topLeft = True
	topRight = True
	bottomLeft = True
	bottomRight = True

	if (row[qr1x] == 0 and row[qr1y] == 0):
		print("qr1 is missing???")
		topLeft = False

	if (row[qr2x] == 0 and row[qr2y] == 0):
		print("qr2 is missing???")
		topRight = False

	if (row[qr3x] == 0 and row[qr3y] == 0):
		print("qr3 is missing???")
		bottomLeft = False

	if (row[qr4x] == 0 and row[qr4y] == 0):
		print("qr4 is missing???")
		bottomRight = False

	if ( (topLeft == False) and (topRight == False) and (bottomRight == False) and (bottomLeft == False) ):
		print("No Qr Code Detected")
		return (1)

	elif ((topLeft and topRight and (row[pupily] < row[qr1y] or row[pupily] < row[qr2y])) or (
			topLeft == False and topRight and row[pupily] < row[qr2y]) or (
			topRight == False and topLeft and row[pupily] < row[qr1y])):
		print("Looking above of qr code region")
		return (1)

	elif ((topLeft and bottomLeft and (row[pupilx] < row[qr1x] or row[pupilx] < row[qr3x])) or (
				topLeft == False and bottomLeft and row[pupilx] < row[qr3x]) or (
				bottomLeft == False and topLeft and row[pupilx] < row[qr1x])):
		print("looking to the left of qr code region")
		return (1)

	elif ((topRight and bottomRight and (row[pupilx] > row[qr2x] or row[pupilx] > row[qr4x])) or (
				topRight == False and bottomRight == True and row[pupilx] > row[qr4x]) or (
				bottomRight == False and topRight == True and row[pupilx] > row[qr2x])):
		print("looking to the right of qr code region")
		return (1)

	elif ((bottomLeft and bottomRight and (row[pupily] > row[qr3y] or row[pupily] > row[qr4y])) or (
				bottomRight == False and bottomLeft and row[pupily] > row[qr3y]) or (
				bottomLeft == False and bottomRight and row[pupily] > row[qr4y])):
		print("Looking below of qr code region")
		return (1)

	else:
		print("Looking in AOI region!!!!!!!!!!!!!!!!!!!!!!!")
		return (0)

## total time = time at point 1000 - time at point 0
#avg time = total time / length of list

fTime = 0.0
counter =0
while True:
	line = str(sock.recv(1024))
	print(line)
	row = line.replace("\\n", "").replace("b\'", "").replace("'", "").replace("\\r","").split("\\t")
	row[-1] =row[-1].strip()
	counter += 1
	if counter ==1:
		print(row)
	if counter !=1:
		if counter == 2:
			startTime = time.time()
		if counter == 201:
			endTime = time.time()
		doublerows = [float(i) for i in row]
		data.append(doublerows)
		#print(sock.recv(1024))
		binary = checkRegion(doublerows, pupilx, pupily, qr1x, qr1y, qr2x, qr2y, qr3x, qr3y, qr4x, qr4y)
		check.append(binary)


		if (len(data) == initialize):
			time = endTime - startTime
			fTime = float(time)/200

		if (len(data) >= initialize):
			if (len(data)> 3/fTime): # number/sec *3 sec
				check = check[1:]
				if (sum(check)>2/fTime):
					print("EXTREME WARNING")
