# Data classification based on AOI detection temp code
# Last updated May 10, 2022 by Charlie
# TEST VERSION

def data_transformation(TCP_data):
    """
    transform the TCP data into a more readable data for data processing
    """

    cleaned_data = str(TCP_data).replace("\\n", "").replace("b\'", "").replace("'", "").replace("\\r","").split("\\t") # turn the TCP data to a list
    cleaned_data[-1] = cleaned_data[-1].strip() # clean the data

    coded_data = []

    try:
        coded_data = [float(i) for i in cleaned_data] # turn the cleaned data into double type

    except:
        print("ERROR")

    return coded_data
