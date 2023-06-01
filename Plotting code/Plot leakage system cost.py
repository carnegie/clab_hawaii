'''This code will plot the leakage rate on the x-axis vs cost of optimized system on the y-axis.'''

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

path0 = 'C:\\Users\\Dominic\\desktop\\Experiment Runs With Up-To-Date Inputs\\Leakage Analysis\\h2_leakage_analysis_0.0004_no_normal.pickle'
path1 = 'C:\\Users\\Dominic\\desktop\\Experiment Runs With Up-To-Date Inputs\\Leakage Analysis\\h2_leakage_analysis_0.0478_no_normal.pickle'
path2 = 'C:\\Users\\Dominic\\desktop\\Experiment Runs With Up-To-Date Inputs\\Leakage Analysis\\h2_leakage_analysis_0.0952_no_normal.pickle'
path3 = 'C:\\Users\\Dominic\\desktop\\Experiment Runs With Up-To-Date Inputs\\Leakage Analysis\\h2_leakage_analysis_0.1426_no_normal.pickle'
path4 = 'C:\\Users\\Dominic\\desktop\\Experiment Runs With Up-To-Date Inputs\\Leakage Analysis\\h2_leakage_analysis_0.19_no_normal.pickle'
path5 = 'C:\\Users\\Dominic\\desktop\\Experiment Runs With Up-To-Date Inputs\\Leakage Analysis\\h2_leakage_analysis_0.2374_no_normal.pickle'
path6 = 'C:\\Users\\Dominic\\desktop\\Experiment Runs With Up-To-Date Inputs\\Leakage Analysis\\h2_leakage_analysis_0.2848_no_normal.pickle'

cost_arr = np.array([])

list1 = [path0, path1, path2, path3, path4, path5, path6]
for path in list1:
    with open(path, 'rb') as f:
        data1 = pickle.load(f)
        case_results = data1['case results']
        cost = case_results['system cost [$/h]']
        cost_arr = np.append(cost_arr, cost)

#Convert from system $/h to $/kWh
cost_arr = cost_arr/1000/641.2960529
print(cost_arr)

#Plot the values
x = np.array([0.0004, 0.0478, 0.0952, 0.1426, 0.19, 0.2374, 0.2848])
y = [cost_arr[0], cost_arr[1], cost_arr[2], cost_arr[3], cost_arr[4], cost_arr[5], cost_arr[6]]

# Calculate the regression line
slope, intercept, r_value, p_value, std_err = linregress(x, y)
regression_line = slope * np.array(x) + intercept

# Calculate the R-squared value
r_squared = r_value**2

# Plot
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)
fig, ax = plt.subplots(figsize=(6, 6)) #make square
ax.plot(x, y, 'o',color='blue', label='Data')
ax.plot(x, regression_line, color='black', label=f'y = {slope:.4f}x + {intercept:.2f}  |  $R^2$ = {r_squared:.2f}')
ax.set_xlabel('Leakage of H2 Storage (%/day)', fontsize=14)
ax.set_ylabel('System Cost ($/kWh)', fontsize=14)
ax.set_title('System Cost As Leakage Increases', fontsize=16, pad = 12)
ax.set_ylim(0.15, 0.16)
ax.set_xlim(0, 0.2856)
ax.set_xticks([0.0004, 0.0478, 0.0952, 0.1426, 0.19, 0.2374, 0.2848])
ax.set_xticklabels(['0.0004', '0.0478', '0.0952', '0.1426', '0.19', '0.2374', '0.2848']) 
ax.tick_params(axis='both', which='major', labelsize=14)
for tick in ax.get_xticklabels():
    tick.set_rotation(45)

plt.legend()
plt.savefig('C:\\Users\\Dominic\\desktop\\Oahu Results\\system_cost_leakage.png', dpi=300, bbox_inches='tight')
plt.show()