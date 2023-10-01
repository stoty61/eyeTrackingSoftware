# AOI Class based on AOI detection temp code
# Last updated May 10, 2022 by Charlie
# TEST VERSION

import time

class area_of_interest():
    def __init__(self, QR_x, QR_y):
        self.QR_x = QR_x
        self.QR_y = QR_y


    def sample_rate_detection(self, pupil_x):
        """
        return a integer of sample rate in the initialization process

        assuming 4 QR codes forming a rectangle, starting from top-left corner going clockwise
        """

        sample_list = [] # initialize the list of sample data
        sample_time = 5 # run the test for 5 seconds

        start_time = time.time() # record the start time

        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time

            data_list.append(self.pupil_x)

            if elapsed_time > sample_time: # stop the loop when the time
                break

        return int(len(data_list) / sample_time) # return the sample rate in Hertz


    def inside_AOI(self, pupil_x, pupil_y, QR_x, QR_y):
        """
        return a boolean that indicates the status of the focus with respect to AOI
        """
        self.QR_x = QR_x
        self.QR_y = QR_y

        # target point to the left of the rectangle
        if min(self.QR_x[0], self.QR_x[3]) > pupil_x:
            return 0

        # target point to the right of the rectangle
        elif max(self.QR_x[1], self.QR_x[2]) < pupil_x:
            return 0

        # target point to the top of the rectangle
        elif min(self.QR_y[0], self.QR_y[1]) > pupil_y:
            return 0

        # target point to the bottom of the rectangle
        elif max(self.QR_y[2], self.QR_y[3]) < pupil_y:
            return 0

        else:
            return 1
