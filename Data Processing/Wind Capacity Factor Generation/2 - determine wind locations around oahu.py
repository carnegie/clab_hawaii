'''This script will read the .h5 file and extract the point and latitudes and longitudes of the points in a square around Oahu.'''

import h5py
import numpy as np
import sys
import argparse
import pandas as pd
import csv
import os

path = 'D:\Hawaii_h5'
os.chdir(path)

f = h5py.File('Hawaii_2006_100m.h5', 'r')
print(f.keys())

valid_points = []
lat_valid = []
lon_valid = []

#Determine the index values of points in 'coordinates' that have a latitude between 21.23 and 21.74 and a longitude between -158.33 and -157.62
for i in range(306112):
    if f["coordinates"][i][0] >= 21.23 and f["coordinates"][i][0] <= 21.74 and f["coordinates"][i][1] >= -158.33 and f["coordinates"][i][1] <= -157.62:
        valid_points = np.append(valid_points, i)
        lat_valid = np.append(lat_valid, f["coordinates"][i][0])
        lon_valid = np.append(lon_valid, f["coordinates"][i][1])

        print(i)
    else:
        continue

#Save valid points, lat_valid, and lon_valid to a csv
with open('valid_points.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(valid_points)
    writer.writerow(lat_valid)
    writer.writerow(lon_valid)
    
