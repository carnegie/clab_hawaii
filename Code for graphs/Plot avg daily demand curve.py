'''
This script will plot the average daily demand for Oahu for the 14 year period.
'''

import os
import sys
import csv
import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

HI_demand = Path("/Users/Dominic/Desktop/2006_2020_Hawaii_State_Hourly_Demand_Proper_Format.csv")

#import data from column 4 starting at row 7 into a pandas dataframe
df = pd.DataFrame()
df = pd.read_csv(HI_demand, header=11, usecols=[4])
print(df)

#Gather every 24th row (every day) and average them
df3 = pd.DataFrame()
for i in range(24):
    df2 = pd.DataFrame()
    df2 = df.iloc[i::24].mean(axis=0)
    #concat df2 to df3
    df3 = pd.concat([df3, df2], axis=0, ignore_index = True)
    print(df2)
print(df3)

#add the final value in df3 to the beginning of df3
df4 = pd.DataFrame()
df4 = df4.append(df3.iloc[-1], ignore_index=True)
df4 = pd.concat([df4, df3], axis=0, ignore_index = True)
print(df4)


#Plot the average daily demand
plt.plot(df4)
plt.title('Average Daily Demand for Oahu')
plt.xlabel('Hour of Day')
plt.ylabel('Average Daily Demand (MW)')
#make the y axis start at 0
plt.ylim(bottom=0, top=1200)
#set x axis ticklabels to be every 4 hours
times = ['0:00', '4:00', '8:00', '12:00', '16:00', '20:00', '24:00']
plt.xticks(np.arange(0, 28, 4), times)
plt.show()
