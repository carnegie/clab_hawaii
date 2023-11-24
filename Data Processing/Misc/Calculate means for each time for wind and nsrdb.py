'''
This script will average the values for each hour of the 91 points in the WIND toolkit data and the 91 points in the nsrdb data.'''

import os
import sys
import csv
import numpy as np
import pandas as pd
from pathlib import Path

# Create path to the folder that contains the csv files with the new nsrdb data
nsrdb = Path("/Users/Dominic/Desktop/4 - MEM ready solar cfs by location with leap")

#Create path to the folder that contains the csv files with the WIND toolkit data
wind = Path("/Users/Dominic/Desktop/WIND Toolkit cfs with leap/2009")

wind_csv = Path("/Users/Dominic/Desktop/Oahu wind toolkit means.csv")
nsrdb_csv = Path("/Users/Dominic/Desktop/Oahu nsrdb means.csv")

#Take the average of every 91 values for each hour in the nsrdb data
all_nsrdb = pd.DataFrame()
all_nsrdb_mean = pd.DataFrame()
for file in nsrdb.iterdir():
    read_nsrdb = pd.read_csv(file, sep=",", dtype=str, header = None, usecols=[4], skiprows=[0,1,2,3,4,5,])
    print(read_nsrdb)
    print(read_nsrdb.shape)
    all_nsrdb = pd.concat([all_nsrdb, read_nsrdb], axis=1)
    print(all_nsrdb)
all_nsrdb = all_nsrdb.astype(float)
all_nsrdb['mean'] = all_nsrdb.mean(axis=1)
print(all_nsrdb)
        
all_nsrdb_mean = pd.concat([all_nsrdb_mean, all_nsrdb['mean']], axis=0)
print(all_nsrdb_mean)
print(all_nsrdb_mean.shape)       

all_nsrdb_mean.to_csv(nsrdb_csv, sep=",", header = False, index = False, mode = 'a')

'''
#Add the values from each file in the wind toolkit to a dataframe
all_wind = pd.DataFrame()
all_wind_mean = pd.DataFrame()

for file in wind.iterdir():
    read_wind = pd.read_csv(file, sep=",", dtype=str, header = None)
    read_wind = read_wind.T
    #print(read_wind)
    #print(read_wind.shape)
    #print(len(read_wind))
    #concatenate read_wind to all_wind
    all_wind = pd.concat([all_wind, read_wind], axis=1)
    print(all_wind)
    #Take the average of the 91 columns for every row
#convert every value in all_wind to a float
all_wind = all_wind.astype(float)
all_wind['mean'] = all_wind.mean(axis=1)
print(all_wind)

#append the mean column to a dataframe named all_wind_mean
all_wind_mean = pd.concat([all_wind_mean, all_wind['mean']], axis=0)
print(all_wind_mean)
print(all_wind_mean.shape)


#Append the data to a a csv file
all_wind_mean.to_csv(wind_csv, sep=",", header = False, index = False, mode = 'a')
'''