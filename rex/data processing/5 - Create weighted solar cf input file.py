'''This script will weight the different input files and add their weighted values to produce one weighted average csv file.'''
#Import modules
import pandas as pd
import numpy as np
import os
from pathlib import Path
from datetime import datetime
import csv

#Create path to folder with all the solar capacity factor csv files
docs = Path("/Users/Dominic/Desktop/test/")

weight = Path("/Users/Dominic/Desktop/Solar Weights.csv")

#Read in the 4th column of the weight csv file starting at row 2
read_weight = pd.read_csv(weight, sep=",", usecols=[3], skiprows=0)
#print(read_weight)

#read in the first column of the weight csv file starting at row 2
read_weight_location = pd.read_csv(weight, sep=",", usecols=[0], skiprows=0)
#print(read_weight_location)


#print(read_weight_location.iloc[1,0])
#print(read_weight.iloc[1,0])


combined_values = pd.DataFrame()

#ensuring that the correct file is being chosen for the correct weighting
for file in docs.iterdir():
    print(file)
for i in range(108):
    print(read_weight_location.iloc[i][0])
    print(read_weight.iloc[i][0])
    
    

for file in docs.iterdir():
    print(file)
    data = pd.read_csv(file, sep=",")
    combined_values[file.stem[0:5]] = data.iloc[5:,4]
    combined_values[file.stem[0:5]] = combined_values[file.stem[0:5]].astype(float)
    
print(combined_values)

print(combined_values.dtypes)

for i in range(108):
    #multiply the combined_values[read_weight_location[i][0]] by read_weight.iloc[i][0]
    
    combined_values[str(read_weight_location.iloc[i][0])] = combined_values[str(read_weight_location.iloc[i][0])] * read_weight.iloc[i][0]

#Sum the values in each row
combined_values['Sum'] = combined_values.sum(axis=1)
print(combined_values)

#Save combined_values['Average'] to a new csv file
new_file = 'Weighted Solar CFs.csv'
combined_values.to_csv(new_file, sep=",", index = False, columns=['Sum'])