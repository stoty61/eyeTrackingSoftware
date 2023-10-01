# integrated warning display system with UDP listner, time-based approach

# libraries used
from logging import warning
from tkinter import * # user interface
from PIL import ImageTk, Image # use of image, "Pillow"
import socket # UDP data stream
from datetime import datetime, timedelta # time calculation
import pygame # warning sound
import time # UNIX timestamp

# set up the timestamp for the file
time_year = datetime.now().strftime("%Y")
time_month = datetime.now().strftime("%m")
time_day = datetime.now().strftime("%d")
time_hour = datetime.now().strftime("%H")
time_minute = datetime.now().strftime("%M")
time_second = datetime.now().strftime("%S")
file_timestamp = f"{time_year}{time_month}{time_day} {time_hour}_{time_minute}_{time_second}"


# UI setup
root = Tk() # create the instance of frame
root.geometry("720x480") # set the size of the frame
root.title("Warning Display System") # set the title of the frame
root.configure(bg="black")


# warning display setup
warning_icon = ImageTk.PhotoImage(Image.open(r"C:\Users\hfast_2\Documents\WarningDisplay\icon.png")) # get the image of warning icon
warning_display = Label(image = warning_icon, borderwidth=0, background="black") # use as the icon of the warning
warning_display.pack(fill="both", expand=1) # display the warning
warning_display.pack_forget() # hide the warning


# initialize the mixer module from pygame
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\hfast_2\Documents\WarningDisplay\warning.mp3")


# UDP connection setup
local_ip = "127.0.0.1" # ip address of localhost
local_port = 1501 # port used by D-Lab
buffer_size = 1024

# create a datagram socket
UDP_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# bind to the local ip address and port
UDP_socket.bind((local_ip, local_port))


# variable initialization
current_state = False # a flag to mark the current state of the system, True = warning triggered
warning_detection = False # a flag to mark if the warning detection has started, True = started
glance_detection = False # a flag to mark if the glance detection has started, True = started

warning_detection_start_time = time.time() # warning detection period start time
glance_detection_strart_time = time.time() # glance detection period start time


# period definition
glance_period = 0.160 # set the glance interval
warning_period = 2.500 # set time interval for warning


# the file handling function that writes data to the log
def file_handling(code): # code: a string of information that is going to be written with timestamp

    # open the file with the current study timestamp
    with open(f"{file_timestamp}_log.txt", "a+") as log_file:
        unix_time = time.time()
        local_time = datetime.fromtimestamp(time.mktime(time.localtime(unix_time)))
        unix_timestamp = ("%.3f" % round(unix_time, 3)).replace(".", "")
        log_file.write(f"{code}, {unix_timestamp}, {local_time}\n")


# the function to display warning icon
def display():

    # use the global variable
    global current_state
    global warning_detection
    global glance_detection
    global warning_detection_start_time
    global glance_detection_strart_time

    global glance_period
    global warning_period

    global file_timestamp


    # UDP data receiver
    data_received = UDP_socket.recvfrom(buffer_size) # receive UDP data
    data = data_received[0].decode("utf-8")[-6:-1].strip() # get the data from the received UDP data
    time_received = time.time() # get the time when the UDP data is received

    # logger for the data
    with open(f"{file_timestamp}_log.txt", "a+") as log_file:
        unix_timestamp = ("%.3f" % round(time_received, 3)).replace(".", "")
        local_time = datetime.fromtimestamp(time.mktime(time.localtime(time_received)))
        log_file.write(f"{data} data received, {unix_timestamp}, {local_time}\n")


    if current_state == False and warning_detection == False and glance_detection == False:

        if data == "false": # if the data is outside AOI

            warning_detection = True # start the warning detection
            warning_detection_start_time = time.time() # set the start of the warning detection period

            file_handling("warning detection started")

    elif current_state == False and warning_detection == True and glance_detection == False:

        if time_received - warning_detection_start_time < warning_period: # if the warning period has not exceeded the minimum trigger time

            if data == "true": # if the data is inside AOI

                glance_detection = True # start the glance detection
                glance_detection_strart_time = time.time() # set the start of the glance detection period

                file_handling("glance detection started")


        if time_received - warning_detection_start_time >= warning_period: # if the warning period has exceeded the minimum trigger time
    
            current_state = True

            warning_detection = False # end the warning detection

            pygame.mixer.music.play() # start to play the warning sound
            warning_display.pack(fill="both", expand=1) # display the warning icon

            file_handling("warning triggered")


    elif current_state == False and warning_detection == True and glance_detection == True:

        if time_received - glance_detection_strart_time < glance_period: # if it is not a glance

            if data == "false":

                glance_detection = False # end the glance detection

                file_handling("glance detection ended")

        else:

            warning_detection = False # end the warning detection
            glance_detection = False # end the glance detection

            file_handling("warning detection and glance detection ended")

    elif current_state == True and warning_detection == False and glance_detection == False:

        if data == "true": # if the data is inside AOI        
            
            glance_detection = True # start the glance detection
            glance_detection_strart_time = time.time() # set the start of the glance detection period

            file_handling("glance detection started")
    
    elif current_state == True and warning_detection == False and glance_detection == True:

        if time_received - glance_detection_strart_time < glance_period: # if it is not a glance

            if data == "false":

                glance_detection = False # end the glance detection

                file_handling("glance detection ended")

        else:

            current_state = False
            glance_detection = False # end the glance detection

            warning_display.pack_forget() # stop displaying the warning
            pygame.mixer.music.stop() # stop playing the warning sound

            file_handling("warning disabled")

    else:
        file_handling("exception")


    root.after(1, display) # put in a "while true loop"


# GUI Window refresh
root.after(1, display) # put in a "while true loop"
root.mainloop()
