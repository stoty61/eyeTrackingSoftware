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


    def inside_AOI(self, pupil_x, pupil_y, QR_x, QR_y):
        """
        return a boolean that indicates the status of the focus with respect to AOI
        """

        self.QR_x = QR_x # initialize the x-coordinate(s) of the QR code(s)
        self.QR_y = QR_y # initialize the y-coordinate(s) of the QR code(s)

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
