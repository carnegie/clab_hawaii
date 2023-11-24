'''
This script will take the full 1998-2020 solar capacity factor csv files for each location,
plus a correct-format csv for input into the model, and create a new csv file per location
that is properly formatted for use in the model.
'''

#Import modules
import pandas as pd
import numpy as np
import os
from pathlib import Path
from datetime import datetime
import csv

#Create path to folder with the input csv
format = Path("/Users/Dominic/Desktop/last trial format/full iwth leap solar cfs format.csv")

#Create path to folder with all the solar capacity factor csv files
docs = Path("/Users/Dominic/Desktop/NSRDB Wind Cfs full 23 years by location")

read_format = pd.read_csv(format, sep=",", dtype=str)
#print(read_format)
#print(read_format.shape)

for file in docs.iterdir():
    #print(file)
    read_numbers = pd.read_csv(file, header = None)
    #print(read_numbers)
    #print(read_numbers.shape)

    #Add the solar capacity factor data to the proper column in the format dataframe
    read_format.iloc[5:,4] = read_numbers.iloc[0:,0]
    #print(read_format)
    
    #Save the full dataframe to a new csv file
    new_file = file.stem + ' with cfs.csv'
    read_format.to_csv(new_file, sep=",", index = False, columns=['Wind cfs', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'])