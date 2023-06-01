'''This code will determine the correlation or anticorrelation between wind and solar capacity factors'''

import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import seaborn as sns
from pathlib import Path
import os
from scipy.stats import linregress

HI_wind = Path("/Users/Dominic/Desktop/WIND weighted average Oahu wind cfs 2006-2019.csv")
HI_solar = Path("/Users/Dominic/Desktop/NSRDB weighted average Oahu solar cfs 2006-2019.csv")
output_path = '/Users/Dominic/desktop/'

#Read in the data
df_wind = pd.DataFrame()
df_wind = pd.read_csv(HI_wind, header=5, usecols=[4])

df_solar = pd.DataFrame()
df_solar = pd.read_csv(HI_solar, header=5, usecols=[4])

#take the mean of every 24 rows (every day) of df
df_wind = df_wind.groupby(np.arange(len(df_wind))//24).mean()
df_solar = df_solar.groupby(np.arange(len(df_solar))//24).mean()

# Calculate the regression line
x = np.array(df_wind)
y = np.array(df_solar)
slope, intercept, r_value, p_value, std_err = linregress(x[:,0], y[:,0])
regression_line = slope * np.array(x) + intercept

# Calculate the R-squared value
r_squared = r_value**2

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)
fig, ax = plt.subplots(figsize=(6, 6)) #make square
ax.plot(x, y, 'o')
ax.plot(x, regression_line, color='black', label=f'$R^2$ = {r_squared:.6f}')
ax.set_xlabel('Average Wind Capacity Factor Per Day',fontsize=14)
ax.set_ylabel('Average Solar Capacity Factor Per Day',fontsize=14)
ax.set_title('Average Wind and Solar Capacity\nFactors Per Day Over 14-Year Period', fontsize = 16, pad = 10)
ax.tick_params(axis='both', which='major', labelsize=12)
ax.legend(fontsize=12)

plt.legend()
plt.savefig('C:\\Users\\Dominic\\desktop\\Oahu Results\\Average Wind and Solar Capacity Factors Per Day Over 14-Year Period.png', dpi=300, bbox_inches='tight')
plt.show()
