'''
This script will identify the values from one file that are most similar to values in another file and save them to a new file
'''

#Import modules
import pandas as pd
import numpy as np
import os
from pathlib import Path
from datetime import datetime

#Create path to folder with the first csv
working = Path("/Users/Dominic/Desktop/hawaii 2019 h5 just oahu.csv")
ref_csv = Path("/Users/Dominic/Desktop/lat and lon of nsrdb solar data points.csv")

#append the data from column 2 of ref_csv into a pandas dataframe
ref_long = pd.read_csv(ref_csv, sep=",", header=0, usecols=[1])
#print(ref_long)

ref_lat = pd.read_csv(ref_csv, sep=",", header=0, usecols=[0])
#print(ref_lat)

working_lat = pd.read_csv(working, sep=",", header=0, usecols=[1])
#print(working_lat)

working_long = pd.read_csv(working, sep=",", header=0, usecols=[2])
#print(working_long)

latlist = []
longlist = []
difflist = []
closestlist = []
for i in range(len(ref_lat)):
#for each value in ref_lat, find the absolute value of the difference between that value and each value in working_lat

#print(ref_lat.iloc[0,0])
    for index, row in working_lat.iterrows():
        latlist.append(abs(abs(row['Column1'])-abs(ref_lat.iloc[i,0])))
    #print(latlist)
        #print(latlist)
    for index, row in working_long.iterrows():
        longlist.append(abs(abs(row['Column2'])-abs(ref_long.iloc[i,0])))

    for j in range(len(latlist)):
        difflist.append(latlist[j]+longlist[j])
    
    smallest_value_index = difflist.index(min(difflist),0,934)
    closestlist.append(smallest_value_index)
    latlist=[]
    longlist=[]
    difflist=[]
    #print(latlist)
print(closestlist)
  
#use the values from closestlist to import the values from that index of working into a new dataframe
newdf = pd.DataFrame()
newdf2 = pd.DataFrame()
newdf= pd.read_csv(working, sep=",", header=0)
for i in range(len(closestlist)):
    newdf2 = newdf2.append(newdf.iloc[closestlist[i],:], ignore_index=True)
print(newdf2)

#save the values from newdf2 to a new csv
newdf2.to_csv("/Users/Dominic/Desktop/hawaii 2019 h5 just oahu closest to nsrdb.csv", index=False)