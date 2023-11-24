'''This script will plot the ECRF from 2021 to now'''
from __future__ import division
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from datetime import datetime, timedelta
import csv

import numpy as np
from os import listdir

import pickle
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import matplotlib.gridspec as gridspec
import matplotlib.ticker as ticker

import datetime
from matplotlib.dates import drange
from matplotlib.ticker import FormatStrFormatter

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
#remove the brackets from inside the list
ecrf = [item for sublist in ecrf for item in sublist]


fom = [0.001836]*30
vom = [0.002792]*30
investment = [0.001159]*30



#Create bottom of the bar chart
p3bottom = np.add(ecrf, fom)
p4bottom = np.add(p3bottom, vom)

#print the shape of ecrf
print(np.shape(ecrf))
print(fom)
print(np.shape(vom))

#Plot

fig, ax = plt.subplots(figsize=(20,8))
index = np.arange(30)
bar_width = 0.5
opacity = 1
#Make stacked bar plots with the capacity of each system component on the y axis and year on the x axis
p1 = plt.bar(index, ecrf, bar_width, alpha=opacity, color='blue', label='Energy Cost\n Recovery Factor')
p2 = plt.bar(index, fom, bar_width, alpha=opacity, color='green', label='Fixed O&M', bottom=ecrf)
p3 = plt.bar(index, vom, bar_width, alpha=opacity, color='red', label='Variable O&M', bottom=p3bottom)
p4 = plt.bar(index, investment, bar_width, alpha=opacity, color='orange', label='Investment', bottom=p4bottom)

#add a black border to the bars
for bar in p1 + p2 + p3 + p4:
    bar.set_linewidth(1)
    bar.set_edgecolor('black')

ax.set_xlabel('Date', fontsize=14)
plt.ylabel('Cost ($/kWh)', fontsize=14)
plt.title('Estimated Cost per kWh \nof Current Electricity System', fontsize=18, pad = 12)
plt.ylim(0, 0.35)

ax.set_xticks(np.arange(0, 30, 1))
months =['Jan 2021', 'Feb 2021', 'Mar 2021', 'Apr 2021', 'May 2021', 'Jun 2021', 'Jul 2021', 'Aug 2021', 'Sep 2021', 'Oct 2021', 'Nov 2021', 'Dec 2021', 'Jan 2022', 'Feb 2022', 'Mar 2022', 'Apr 2022', 'May 2022', 'Jun 2022', 'Jul 2022', 'Aug 2022', 'Sep 2022', 'Oct 2022', 'Nov 2022', 'Dec 2022', 'Jan 2023', 'Feb 2023', 'Mar 2023', 'Apr 2023', 'May 2023', 'Jun 2023']
ax.set_xticklabels(months)

ax.tick_params(axis='y', which='major', labelsize=12)
ax.tick_params(axis='x', which='major', labelsize=10)

y = ['Energy Cost\nRecovery Factor', 'Fixed O&M', 'Variable O&M', 'Payment on \nInvestment']
legend = plt.legend(reversed([p1, p2, p3, p4]), reversed(y),bbox_to_anchor=(1, 0.65),fontsize='14', edgecolor='black')

for handle in legend.legendHandles:
    handle.set_edgecolor('black')

for bar in p1 + p2 + p3 + p4:
    bar.set_linewidth(1)
    bar.set_edgecolor('black')

plt.xticks(rotation=45)

plt.savefig('C:\\Users\\Dominic\\desktop\\Oahu Results\\system cost_over_time.png', dpi=300, bbox_inches='tight')
plt.show()