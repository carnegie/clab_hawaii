'''This script will plot the ECRF from 2021 to now'''

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from datetime import datetime, timedelta
import csv

# input path
ecrf_csv = '/Users/Dominic/Desktop/22-23 ECRFs.csv'

# Read all rows in column three of the file into a list
with open(ecrf_csv, 'r') as f:
    ecrf = pd.read_csv(f, sep=",", usecols=[2])

#Flip the list so that the oldest data is first
ecrf = ecrf.iloc[::-1].reset_index(drop=True)

#convert to numpy array
ecrf = np.array(ecrf)
ecrf = ecrf/100

#convert to list
ecrf = ecrf.tolist()

#Plot
fig = plt.figure(figsize=(10, 5))
ax1 = plt.subplot2grid((1, 1), (0, 0), colspan=1, rowspan=1)
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(ecrf,color='blue')
ax.plot(ecrf, 'o',color='blue', markeredgecolor = 'black')
#ax.set_xlabel('Date', fontsize=16)
ax.set_ylabel('Energy Cost Recovery Factor \n($/kWh)', fontsize=16)
ax.set_title('Energy Cost Recovery Factor\nOver Time', fontsize=18, pad = 12)


ax.set_xticks(np.arange(0, 36, 3))
months =['Jan 2021', 'Apr 2021', 'July 2021', 'Oct 2021', 'Jan 2022', 'Apr 2022', 'July 2022', 'Oct 2022', 'Jan 2023', 'Apr 2023', 'July 2023', 'Oct 2023']
ax.set_xticklabels(months)

ax.set_ylim(0,0.35)
ax.tick_params(axis='y', which='major', labelsize=12)
ax.tick_params(axis='x', which='major', labelsize=12)


#make x and y axis text fontsize 14
for item in ([ax.xaxis.label] + ax.get_xticklabels() + ax.get_yticklabels()):
    item.set_fontsize(20)
    
for item in (ax.get_xticklabels()):    
    item.set_rotation(45)
    
    
ax.yaxis.label.set_fontsize(22)

ax.title.set_fontsize(26)



plt.grid(visible=False)

plt.xticks(rotation=45)
plt.savefig('C:\\Users\\Dominic\\desktop\\Oahu Results\\ecrf_over_time.png', dpi=300, bbox_inches='tight')
plt.show()