'''
This script will add the names of each location's data file (either wind or solar) to a new csv.
'''

#Import modules
import pandas as pd
import numpy as np
import os
from pathlib import Path
from datetime import datetime
import csv

#Create path to folder with the input csv
format = Path("/Users/Dominic/Desktop/4 - MEM ready wind cfs by location with leap")

#Add the name of each file in the folder to a list
file_names = []
for file in format.iterdir():
    file_names.append(file.name)
    print(file.name)

    #Append the list to a new csv file
    with open('MEM ready wind cfs by location with leap.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(file_names)
        file_names = []