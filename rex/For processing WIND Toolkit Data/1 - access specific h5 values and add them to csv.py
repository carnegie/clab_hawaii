'''
The script will extract the desired data from an h5 file
'''
import os
path = 'D:\Hawaii_h5'
os.chdir(path)

import h5py
import numpy as np
import sys
import argparse
import pandas as pd
import csv



f = h5py.File('Hawaii_2019_100m.h5', 'r')
print(f.keys())

list = [150482,151520,152559,153599,154639,143252,144795,145826,146859,147893,148928,150485,151523,152562,153602,154642,142227,143255,144798,145829,146862,147896,148931,149968,151525,152564,153604,141205,142230,143257,144800,145831,146864,147898,148933,149970,151527,152566,153606,141207,142232,143259, 144287,145833,146866,147900,148935,149973,151011,153609,140187,141209,142234,143262,144290,145836,146869,147903,148938,149975,140190,141212,142237,143264,144292,145838,146871,147905,148940,149977,138663,140192,141214,142239,143266,144294,145324,146873,147907,148942,143268,144297,145327,146876,147910,144299,145329,146878,147912,145331,146364]
#print(list)
#print(len(list))

newdf = pd.DataFrame()

for i in list:
    #Get the data from the columns of the h5 file
    #data = f["key"][column start:column end+1 ,row start:row end +1]
    data = f["windspeed_100m"][0:105120 , [i]]
    print(data)
    #print(data.shape)
    #print(data.size)
    newdf = pd.concat([newdf, pd.DataFrame(data)], axis=1)
f.close()

#print(newdf)

#transpose newdf
newdf = newdf.T
#print(newdf)

#turn newdf into an array
newdf_array = newdf.to_numpy()
#print(newdf_array)
#print(newdf_array.shape)

hourly_wind = np.average(newdf_array.reshape(-1, 12), axis=1)
#print(hourly_wind)
#print(hourly_wind.shape)


hourly_wind = np.array(hourly_wind).reshape(-1, 8760)
#print(hourly_wind)
#print(hourly_wind.shape)

#Divide each value in hourly_wind by 100 to get the wind speed in m/s
hourly_wind = hourly_wind/100
#print(hourly_wind)
#print(hourly_wind.shape)

#turn hourly_wind into a dataframe
u_ci = 3 # cut in speed in m/s
u_r = 12 # rated speed in m/s
u_co = 25 # cut out speed in m/s
wind_cfs = np.zeros((8760, 1))
wind_cfs_2 = pd.DataFrame()
wind_cfs_3 = pd.DataFrame()


hourly_wind = pd.DataFrame(hourly_wind)
#print(hourly_wind)
#print(len(hourly_wind))
for i in range(0, len(hourly_wind)):
    wind = hourly_wind.iloc[[i]]
    #transpose wind
    wind = wind.T
    print(wind)
    print(len(wind))
    for x in range(len(wind)):
        if wind.iloc[x,0] < 3:
            wind_cfs[x] = 0
        elif wind.iloc[x,0] >= 3 and wind.iloc[x,0] < 12:
            wind_cfs[x] = (wind.iloc[x,0])/(u_r**3)
        elif wind.iloc[x,0] >= 12 and wind.iloc[x,0] <= 25:
            wind_cfs[x] = 1
        elif wind.iloc[x,0] > 25:
            wind_cfs[x] = 0
    print(wind_cfs)
    print(wind_cfs.shape)
    #turn wind_cfs into a dataframe
    wind_cfs_2 = pd.DataFrame(wind_cfs)
    #concat wind_cfs_2 to wind_cfs_3
    wind_cfs_3 = pd.concat([wind_cfs_3, wind_cfs_2], axis=1)
    print(wind_cfs_3)
    print(wind_cfs_3.shape)
wind_cfs_3 = wind_cfs_3.T
print(wind_cfs_3)
print(wind_cfs_3.shape)
        

path = "C:/Users/Dominic/Desktop/WIND Toolkit cfs with leap/2019"
os.chdir(path)
#get name of each file in path
file_names = os.listdir(path)
#print(file_names)

print(wind_cfs_3[1])
print(wind_cfs_3.iloc[[1]])
print(wind_cfs_3.iloc[1,:])
#for name in file_names, create a new csv with the name
for i in range(0, len(file_names)):
    with open(file_names[i], 'w') as f:
        writer = csv.writer(f)
        writer.writerow(wind_cfs_3.iloc[i,:])

