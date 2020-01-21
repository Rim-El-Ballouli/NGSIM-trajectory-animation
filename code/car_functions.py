""" A module containing usefull functions to deal """
from car import Car, Frame

def get_dataframe_by_frameID(frame_ID, dataset):
    """ Returns a subdataframe which contains all the cars that are
    present in a given frame ID"""
    ds  = dataset[dataset.Frame_ID == frame_ID]
    return ds

def create_frame(frame_id, dataset):
    """ returns a frame object representing an actual frame in the dataset
     A frame is a bunch of car objects that are visible in a certain frame """
    dataset = get_dataframe_by_frameID(frame_id, dataset)

    cars = []
    for row in dataset.iterrows():
        row = row[1] # row is a list of header and values (skip index at location 0)
        x_value = row.Local_X
        y_value = row.Local_Y
        width = row.v_Width
        length = row.v_Length
        type = row.v_Class
        vehicle_id = "{:.0f}".format(row.Vehicle_ID) # remove decimal from ID
        car = Car(vehicle_id, width, length, type, x_value, y_value)
        cars.append(car)

    frame = Frame(cars)
    return frame

def create_frames_in_range(frame_id_min, frame_id_max, dataset):
    """ Returns a list of frame objects in the specified range"""
    frames = []
    for i in range(frame_id_min, frame_id_max + 1):
        frame = create_frame(i, dataset)
        frames.append(frame)

    return frames




