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

#Create path to folder with all the solar capacity factor csv files
docs = Path("/Users/Dominic/Desktop/Step 3 Trial")
for folder in docs.iterdir():
    print(folder)
    for file in folder.iterdir():
        print(file)

        data = pd.read_csv(file, sep=",", skiprows=8764, nrows=8759)

        #Create a new csv named after the folder in the path docs

        folder_name = folder.stem + '.csv'
        print(folder_name)


        data.to_csv((folder_name), sep=",", index=0, mode='a')