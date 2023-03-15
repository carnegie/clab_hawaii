'''
This script will take the solar capacity factors specific to each location
and concatenate them so that all the capacity factors for the whole 
1998-2020 period are in one csv file. 
'''
#Import modules
import pandas as pd
import numpy as np
import os
from pathlib import Path
from datetime import datetime
import csv
import re


#Create path to folder with all the solar capacity factor csv files
docs = Path("/Users/Dominic/Desktop/Leap years data and cfs by location")

for folder in docs.iterdir():
    print(folder)
    for file in folder.iterdir():
        print(file)
        year = re.split('_', file.stem)
        print(year[3])

        if year[3] == ' 2000':
            data = pd.read_csv(file, sep=",", skiprows=17573, nrows=8785)
        elif year[3] == ' 2004':
            data = pd.read_csv(file, sep=",", skiprows=17573, nrows=8785)
        elif year[3] == ' 2008':
            data = pd.read_csv(file, sep=",", skiprows=17573, nrows=8785)
        elif year[3] == ' 2012':
            data = pd.read_csv(file, sep=",", skiprows=17573, nrows=8785)
        elif year[3] == ' 2016':
            data = pd.read_csv(file, sep=",", skiprows=17573, nrows=8785)
        elif year[3] == ' 2020':
            data = pd.read_csv(file, sep=",", skiprows=17573, nrows=8785)
        else:
            data = pd.read_csv(file, sep=",", skiprows=17525, nrows=8761)

        print(data)
        #Create a new csv named after the folder in the path docs
        folder_name = folder.stem + '.csv'
        print(folder_name)


        data.to_csv((folder_name), sep=",", index=0, mode='a')
