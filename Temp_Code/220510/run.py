# The run file for data analysis on certain Parameter of Interests
# Last updated May 10, 2022 by Charlie
# TEST VERSION

import TCP_Connection.connect as conn
import Transition_Layer.data_sort as sort
import Data_Processing.AOI as aoi

def run():
    """
    Only works for AOI at this point
    """

    test_aoi_1 = aoi.area_of_interest([], []) # create the test AOI object


    conn.connect("192.168.17.174", 9013) # establish the TCP connection

    while True:
        rt_data = sort.data_transformation(conn.data_relay()) # get the real-time data
        print(len(rt_data))
        try:
            print(test_aoi_1.inside_AOI(rt_data[0], rt_data[1], [rt_data[2], rt_data[4], rt_data[6], rt_data[8]], [rt_data[3], rt_data[5], rt_data[7], rt_data[9]]))
        except Exception as e:
            print(e)

run()