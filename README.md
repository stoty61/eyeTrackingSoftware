# DLab
Programs that establish the TCP connection with D-Lab, relay the data in real-time, sort the data, and process the data stream in real-time.

## Components
This repository includes all the codes in order for D-Lab to relay the data in real-time. The D-Lab data relay system consists of 3 layers:

1. Connection Layer (CL)
2. Transition Layer (TL)
3. Processing Layer (PL)

These 3 layers ensures the integrity and customizability of the data relay system, where each layer can be modified and maintained independently, for easier future updates.

### Connection Layer (CL)

The Connection Layer is responsible to establish the connection between D-Lab and the external system. The connection is established by using Transmission Control Protocol (TCP/IP) information provided in D-Lab relay module. The Connection Layer should not be modified unless the problem is identified as a TCP/IP connectivity issue.

**TCP_Connection.connect**

The connect.py file uses the socket library of Python 3 which is installed by default. The two functions are:

- *connect*
Takes two arguments (ip_address, port).
Returns NULL.

Function that establishes the connection with D-Lab, using the IP_address and port provided in D-Lab relay module. The current version of *connect* does not allow the user to input the IP address and port when running the system. If the change of IP address and port is needed, the user must modify the *run.py* manually.

- *data_relay*
Returns the received raw data from TCP/IP connection.

Function that returns the information received on socket by a size of 1024 bytes, when a TCP/IP connection is already established.

**Further Steps**

The future steps for the Connection Layer includes:
- Adding a new method of taking user input for the IP address and port
- Error handling and performance test in a simulated real participant study environment

### Transition Layer (TL)

The Transition Layer is responsible to convert the data received from D-Lab to a format that can be further processed with a Parameter of Interest (POI) at user's discretion. The data transformation uses the build-in Python text-modification and list-modification methods. The Transition Layer should not be modified unless the problem is identified as a data structure issue.

**Transition_Layer.data_sort**

The data_sort.py file solely uses the Python build-in methods to complete the data transformation between TCP/IP data and Python processable data. THe two functions are:

- *data_transformation*
Takes one argument (TCP_data).
Returns a list of data in float.

Function that transforms the raw data relayed from D-Lab to a list, where all the original data should be in a number format. The returned list will have all the data in a list of float.

Includes error handling to avoid potential conversion errors, such as a string in data. When the error is raised, the system will print "Data Transformation Error" on the screen.

- *data_relay*
Takes one argument (TCP_data).
Returns a list of data in string.

Function that transforms the raw data relayed from D-Lab to a list, where all the original data will be included in the returned list of strings. This function should only be used for header extraction, for data identification purposes.

### Processing Layer (PL)

The Processing Layer is responsible to process the data from previous layers to satisfy certain user needs, based on the research Parameters of Interest, such as Area of Interest (AOI), Blink Rate (BR), etc. The processing is done based on the requirement of the user, as well as other factors such as performance.

The Processing Layer should take information provided from Transition Layer, and use an Object-Oriented Programming approach to maximize efficiency and customizability. The Classes and Methods created in this layer must be independent from all contents in previous layers.

Currently, the only Parameter of Interst being offered in Processing Layer is Area of Interst (AOI).

**Data_Processing.AOI**

The *AOI.py* includes all the components that are necessary to complete the required feature based on real-time data relay from D-Lab. The main Class of the *AOI.py* is area_of_interest, where the four parameters of AOI object are:

- *name*: the name of the AOI
- *QR_x*: a list of x-coordinates of the QR codes that defines the AOI
- *QR_y*: a list of y-coordinates of the QR codes that defines the AOI
- *QR_name*: a list of names of the QR codes that defines the AOI

And the methods associated with the area_of_interest class are:

- *sample_rate_detection*
A temporary method that is used to determine performance of the system based the sample rate. **Have not been tested**

- *inside_aoi*
Takes 4 arguments (pupil_x, pupil_y, QR_x, QR_y).
Returns 1 when the pupil focus is inside, and returns 0 when the pupil focus is outside.

***Still needs to be tested...***

The method that detects if the current pupil focus location is inside of the specified Area of Interest (AOI). The method takes the real-time data to compare the pupil focus location with the AOI, and returns either 0 or 1 for further process.

The method ONLY works with a rectangular AOI. If an AOI of another shape is required, the current method will NOT be functioning as expected.

- *get_QR_name*
Takes no argument.
Returns NULL.

The method that sets the names of the AOI object, and the QR codes that defines the AOI. The method will show the AOI in a graphic-like format for user verification.


# Work Session Notes

**June 20, 2022 - Charlie Sun**
Issue 1: The eye-tracker wasn't able to connect at first, and it was diagnosed as a connection issue from previous experience. I repeated the previous debug process, by trying different USB ports on the D-Lab computer, and no luck. After a few tests between the D-Lab computer in both Analysis Room and Simulator Room, my assumption is, D-Lab Analysis key needs to be plugged into a USB port that is fast enough in order to enable a driver called "VRmagic USB", which is essentially an Analog-to-Digital Converter according to my research. After the "VRmagic USB" driver is enabled (that should be automatically done if the D-Lab Analysis Key is detected and running), the problem should be resolved.
Issue 2: When D-Lab working path is not there anymore, D-Lab can no longer start. D-Lab will be in an infinite loop of loading, and I cannot seem to find a good solution at this moment. I discovered this issue by removing the Z drive (which is mapped to the HFASt MIE Drive), and D-Lab can no longer start after the working path warning popped up. I reconnected the HFASt MIE Drive and mapped it to Z drive again, the issue is resolved.
