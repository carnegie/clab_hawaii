'''
This script will plot the percent of hydrogen storage built compared to the least cost solution using the Hunter et al. cost data
'''
from __future__ import division
import numpy as np
from os import listdir
import os
import pickle
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.ticker as ticker
from scipy.stats import linregress
import datetime
from matplotlib.dates import drange
from matplotlib.ticker import FormatStrFormatter
import pandas as pd

path0 = '/Users/covel/OneDrive/Desktop/13-6-23 Rerun/Figure S7 - Sensitivity Analysis/Outputs/run_one_increasing_h2_storage_cost_yes_normal_output.pickle'
path1 = '/Users/covel/OneDrive/Desktop/13-6-23 Rerun/Figure S7 - Sensitivity Analysis/Outputs/run_two_increasing_h2_storage_cost_yes_normal_output.pickle'
path2 = '/Users/covel/OneDrive/Desktop/13-6-23 Rerun/Figure S7 - Sensitivity Analysis/Outputs/run_three_increasing_h2_storage_cost_yes_normal_output.pickle'
path3 = '/Users/covel/OneDrive/Desktop/13-6-23 Rerun/Figure S7 - Sensitivity Analysis/Outputs/run_four_increasing_h2_storage_cost_yes_normal_output.pickle'
path4 = '/Users/covel/OneDrive/Desktop/13-6-23 Rerun/Figure S7 - Sensitivity Analysis/Outputs/run_five_increasing_h2_storage_cost_yes_normal_output.pickle'
path5 = '/Users/covel/OneDrive/Desktop/13-6-23 Rerun/Figure S7 - Sensitivity Analysis/Outputs/run_six_increasing_h2_storage_cost_yes_normal_output.pickle'
path6 = '/Users/covel/OneDrive/Desktop/13-6-23 Rerun/Figure S7 - Sensitivity Analysis/Outputs/run_seven_increasing_h2_storage_cost_yes_normal_output.pickle'
path7 = '/Users/covel/OneDrive/Desktop/13-6-23 Rerun/Figure S7 - Sensitivity Analysis/Outputs/run_eight_increasing_h2_storage_cost_yes_normal_output.pickle'


h2store_arr = np.array([])

list1 = [path0, path1, path2, path3, path4, path5, path6, path7]

for path in list1:
    with open(path, 'rb') as f:
        data1 = pickle.load(f)
        component_results = data1['component results']
        capacity = component_results['Optimal Capacity [MW]']
        h2 = capacity['Store']
        h2store = h2['h2_storage']
        h2store_arr = np.append(h2store_arr, h2store)
print(h2store_arr)

#Convert the values to percent of the first value
h2store_arr = (h2store_arr/h2store_arr[0])*100
print(h2store_arr)

#Plot the values
x = [0.132497018, 0.232497018, 0.332497018, 0.432497018, 0.532497018, 0.632497018, 0.732497018, 0.832497018]
y = [h2store_arr[0], h2store_arr[1], h2store_arr[2], h2store_arr[3], h2store_arr[4], h2store_arr[5], h2store_arr[6], h2store_arr[7]]

# Calculate the regression line
slope, intercept, r_value, p_value, std_err = linregress(x, y)
regression_line = slope * np.array(x) + intercept

# Calculate the R-squared value
r_squared = r_value**2


fig = plt.figure(figsize=(10, 5))
ax1 = plt.subplot2grid((1, 1), (0, 0), colspan=1, rowspan=1)
fig, ax = plt.subplots(figsize=(6, 6)) #make square
ax.plot(x, y, 'o',color='pink',markeredgecolor='black',markersize=11)
#ax.plot(x, regression_line, color='black', label=f'y = {slope:.2f}x + {intercept:.2f}  |  $R^2$ = {r_squared:.3f}')
ax.set_xlabel('Cost of H$_2$ Storage (\$/kWh/hour)', fontsize=20)
ax.set_ylabel('Percent H$_2$ Storage Deployed\nCompared to Base Case', fontsize=22)
#ax.set_title('Hydrogen Storage Built\nvs Hydrogen Storage Cost', fontsize=24, pad = 12)
ax.set_ylim(0, 110)
ax.set_xlim(0.12, 0.65)
ax.set_xticks([0.132497018, 0.232497018, 0.332497018, 0.432497018, 0.532497018, 0.632497018, 0.732497018, 0.832497018])
ax.set_xticklabels(['0.1325', '0.2325', '0.3325', '0.4325', '0.5325', '0.6325', '0.7325', '0.8325']) #Shortened values to 4 decimals
ax.set_xticklabels(ax.get_xticklabels(), rotation=-45, ha='left')
ax.tick_params(axis='both', which='major', labelsize=20)

plt.savefig('C:\\Users\\covel\\OneDrive\\desktop\\Oahu Results\\percent_h2_storage_built.png', dpi=300, bbox_inches='tight')
plt.show()
