import time


def data_feed(header_list, aoi):
    """
    returns the indices of required data from rt_data in a list
    [pupil_x, pupil_y, [qr-coordinates], [y-coordinates]]
    """

    data_index = [] # the data index list
    qr_x_index = []
    qr_y_index = []

    pupil_x_index = header_list.index("Live Pupil X")
    pupil_y_index = header_list.index("Live Pupil Y")

    # assume the QR codes used are: Monaco, Rio, Zurich, Moscow
    QR_codes = aoi.QR_name

    for i in QR_codes:
        qr_x_index.append(header_list.index("Live " + i + " X1"))
        qr_y_index.append(header_list.index("Live " + i + " Y1"))

    return [pupil_x_index, pupil_y_index, [qr_x_index], [qr_y_index]]


class area_of_interest():

    name = "" # name of the AOI

    QR_x = [] # list of QR code x-coordinates
    QR_y = [] # list of QR code y-coordinates
    QR_name = [] # list of QR code names
    QR_integrity = [] # list of QR code integrity (detected or not)


    def __new__(cls):
        obj = object.__new__(cls)
        return obj


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


    def AOI_integrity(self, QR_x, QR_y, QR_integrity):
        """
        return a boolean that indicates the status of the focus with respect to AOI
        """

        self.QR_x = QR_x # initialize the x-coordinate(s) of the QR code(s)
        self.QR_y = QR_y # initialize the y-coordinate(s) of the QR code(s)
        self.QR_y = QR_integrity # intialize the integrity of the QR code(s)

        # QR code integrity value initialization (Default: True)
        for QR_number in len(self.QR_x):
            self.QR_integrity.append(True)
        # -- the code is to designed with more than 4 QR codes in mind, work-in-progress --


        # check the QR code integrity
        for QR_number in len(self.QR_x):
            if self.QR_x[QR_number] == 0 and self.QR_y[QR_number] == 0:
                self.QR_integrity[QR_number] = False # set the QR code integrity to false
                print("QR code number " + str(QR_number) + " is missing.") # print the error message for debug


    def AOI_detection_4(self, pupil_x, pupil_y, QR_x, QR_y, QR_integrity):
        self.pupil_x = pupil_x
        self.pupil_y = pupil_y
        self.QR_x = QR_x
        self.QR_y = QR_y
        self.QR_integrity = QR_integrity


        if True not in self.QR_integrity:
            return 2 # Error 2: No QR code is detected

        else:
            if self.QR_integrity.count(True) == 1: # only 1 QR code is detected

                index = self.QR_integrity.index(True)

                if index == 0:
                    if self.pupil_x[index] < self.QR_x[index] or self.pupil_y[index] < self.QR_y[index]:
                        return 1 # Code 1: Looking out of the AOI (top-left)
                elif index == 1:
                    if self.pupil_x[index] > self.QR_x[index] or self.pupil_y[index] < self.QR_y[index]:
                        return 1 # Code 1: Looking out of the AOI (top-right)
                elif index == 2:
                    if self.pupil_x[index] > self.QR_x[index] or self.pupil_y[index] > self.QR_y[index]:
                        return 1 # Code 1: Looking out of the AOI (bottom-right)
                elif index == 3:
                    if self.pupil_x[index] > self.QR_x[index] or self.pupil_y[index] < self.QR_y[index]:
                        return 1 # Code 1: Looking out of the AOI (bottom-left)
                else:
                    return 0 # Code 0: Looking at the AOI


            elif self.QR_integrity.count(True) == 2: # only 2 QR codes are detected

                index = list(i for i, status in enumerate(self.QR_integrity) if status == True) # find the index of the detected QR codes

                if sorted(index) == [0, 1]:
                    if self.pupil_x[0] < self.QR_x[0] or self.pupil_x[1] > self.QR_x[1] or self.pupil_y[0] < self.QR_y[0] or self.pupil_y[1] < self.QR_y[1]:
                        return 1 # Code 1: Looking out of the AOI (top-left-right)

                elif sorted(index) == [0, 2]:
                    if self.pupil_x[0] < self.QR_x[0] or self.pupil_x[2] > self.QR_x[2] or self.pupil_y[0] < self.QR_y[0] or self.pupil_y[2] > self.QR_y[2]:
                        return 1 # Code 1: Looking out of the AOI (top-left / bottom-right)

                elif sorted(index) == [0, 3]:
                    if self.pupil_x[0] < self.QR_x[0] or self.pupil_x[3] < self.QR_x[3] or self.pupil_y[0] < self.QR_y[0] or self.pupil_y[3] > self.QR_y[3]:
                        return 1 # Code 1: Looking out of the AOI (top-left-right)

                elif sorted(index) == [1, 2]:
                    if self.pupil_x[1] > self.QR_x[1] or self.pupil_x[2] > self.QR_x[2] or self.pupil_y[1] < self.QR_y[1] or self.pupil_y[2] > self.QR_y[2]:
                        return 1 # Code 1: Looking out of the AOI (top-left-right)

                elif sorted(index) == [1, 3]:
                    if self.pupil_x[1] > self.QR_x[1] or self.pupil_x[3] < self.QR_x[3] or self.pupil_y[1] < self.QR_y[1] or self.pupil_y[3] > self.QR_y[3]:
                        return 1 # Code 1: Looking out of the AOI (top-left-right)

                elif sorted(index) == [2, 3]:
                    if self.pupil_x[2] > self.QR_x[2] or self.pupil_x[3] < self.QR_x[3] or self.pupil_y[2] > self.QR_y[2] or self.pupil_y[3] > self.QR_y[3]:
                        return 1 # Code 1: Looking out of the AOI (top-left-right)

                else:
                    return 0 # Code 0: Looking at the AOI


            elif self.QR_integrity.count(True) == 3: # only 3 QR codes are detected

                index = list(i for i, status in enumerate(self.QR_integrity) if status == True) # find the index of the detected QR codes

                if sorted(index) == [0, 1, 2]:
                    if self.pupil_x[0] < self.QR_x[0] or self.pupil_x[1] > self.QR_x[1] or self.pupil_x[2] > self.QR_x[2] or self.pupil_y[0] < self.QR_y[0] or self.pupil_y[1] < self.QR_y[1]:
                        return 1 # Code 1: Looking out of the AOI (top-left-right)

                elif sorted(index) == [0, 1, 3]:
                    if self.pupil_x[0] < self.QR_x[0] or self.pupil_x[1] > self.QR_x[1] or self.pupil_x[3] < self.QR_x[3] or self.pupil_y[0] < self.QR_y[0] or self.pupil_y[1] < self.QR_y[1]:
                        return 1 # Code 1: Looking out of the AOI (top-left-right)

                elif sorted(index) == [0, 2, 3]:
                    if self.pupil_x[0] < self.QR_x[0] or self.pupil_x[2] > self.QR_x[2] or self.pupil_x[3] < self.QR_x[3] or self.pupil_y[2] > self.QR_y[2] or self.pupil_y[3] > self.QR_y[3]:
                        return 1 # Code 1: Looking out of the AOI (bottom-left-right)

                elif sorted(index) == [1, 2, 3]:
                    if self.pupil_x[3] < self.QR_x[3] or self.pupil_x[1] > self.QR_x[1] or self.pupil_x[2] > self.QR_x[2] or self.pupil_y[2] > self.QR_y[2] or self.pupil_y[3] > self.QR_y[3]:
                        return 1 # Code 1: Looking out of the AOI (bottom-left-right)

                else:
                    return 0 # Code 0: Looking at the AOI


            elif self.QR_integrity.count(True) == 4: # all 4 QR codes are detected

                if self.pupil_x[0] < self.QR_x[0] or self.pupil_x[3] < self.QR_x[3] or self.pupil_x[1] > self.QR_x[1] or self.pupil_x[2] > self.QR_x[2] or self.pupil_y[0] < self.QR_y[0] or self.pupil_y[1] < self.QR_y[1] or self.pupil_y[2] > self.QR_y[2] or self.pupil_y[3] > self.QR_y[3]:
                    return 1 # Code 1: Looking out of the AOI

                else:
                    return 0 # Code 0: Looking at the AOI


            else:
                return -1 # Code -1: Unknown Error 1



    def get_QR_name(self):
        """
        initialize the AOI with user defined parameters
        """

        self.name = input("Please create a name for the Area of Interst: ")

        print("\nYou have created Area of Interest " + self.name + ".")
        self.QR_name.append(input("\nPlease type the name of the QR code on the top-left corner: "))
        self.QR_name.append(input("Please type the name of the QR code on the top-right corner: "))
        self.QR_name.append(input("Please type the name of the QR code on the bottom-right corner: "))
        self.QR_name.append(input("Please type the name of the QR code on the bottom-left corner: "))

        print("\nThe Area of Interest " + self.name + " you created has following QR codes:")
        print(self.QR_name[0] + "           " + self.QR_name[1])
        print("\n" + self.QR_name[3] + "           " + self.QR_name[2])


    def signal_output(self, detection, timestamp, counter):
        """
        initiate a signal to trigger external actions

        designed to work with data-relay feature and warning-display feature
        """

        start_time = timestamp # the timestamp when the signal output system starts working
