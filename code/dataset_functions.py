import pandas as pd

def load_dataset():
    # specify the path to the input NGSIM dataset and the path to the output smoothed dataset
    path_to_dataset = 'C:/Users/relballouli/PycharmProjects/helloworld/trajectory/dataset/'

    # change the file names as needed
    file_name1 = '0750_0805_us101.csv'
    file_name2 = '0805_0820_us101.csv'
    file_name3 = '0820_0835_us101.csv'

    # load the NGSIM data from the CSV files
    train1 = pd.read_csv(path_to_dataset + file_name1, sep=',', encoding='latin-1')
    train2 = pd.read_csv(path_to_dataset + file_name2, sep=',', encoding='latin-1')
    train3 = pd.read_csv(path_to_dataset + file_name3, sep=',', encoding='latin-1')

    return [train1, train2, train3]

def concat_dataset(train):
    train_concat = pd.concat([train[0], train[1], train[3]], ignore_index=True)
    return train_concat