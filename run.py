import TCP_Connection.connect as conn
import Transition_Layer.data_sort as sort
import Data_Processing.AOI as aoi
import socket

# set up the MiniSim TCP server information
host = "192.168.17.19" # IP Address of the MiniSim computer
sim_port = 28960 # a designated port on the MiniSim computer to send information to


# function that receives the information from the server
send_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
send_sock.connect((host, sim_port))

def run_aoi():
    """
    Run the real-time AOI detection from the relayed data
    """

    test_aoi_1 = aoi.area_of_interest.__new__(aoi.area_of_interest) # create the test AOI object

    test_aoi_1.get_QR_name()

    dlab_sock = conn.connect() # establish the TCP connection

    header_data = sort.header_detection(conn.data_relay(dlab_sock)) # get the header data from the current session

    aoi_index = aoi.data_feed(header_data, test_aoi_1) # get the indices for the required data

    while True:
        rt_data = sort.data_transformation(conn.data_relay(dlab_sock)) # get the real-time data
        aoi_data = test_aoi_1.inside_AOI(rt_data[aoi_index[0]], rt_data[aoi_index[1]], [rt_data[aoi_index[2][0][0]], rt_data[aoi_index[2][0][1]], rt_data[aoi_index[2][0][2]], rt_data[aoi_index[2][0][3]]], [rt_data[aoi_index[3][0][0]], rt_data[aoi_index[3][0][1]], rt_data[aoi_index[3][0][2]], rt_data[aoi_index[3][0][3]]])
        send_sock.sendall(bytes(str(aoi_data), "utf-8"))  # send the data received from D-Lab
        # try: # error handling
        #     print(test_aoi_1.inside_AOI(rt_data[aoi_index[0]], rt_data[aoi_index[1]], [rt_data[aoi_index[2][0]], rt_data[aoi_index[2][1]], rt_data[aoi_index[2][2]], rt_data[aoi_index[2][3]]], [rt_data[aoi_index[3][0]], rt_data[aoi_index[3][1]], rt_data[aoi_index[3][2]], rt_data[aoi_index[3][3]]]))
        # except Exception as e:
        #     print(e)

run_aoi()
