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

path0 = 'C:\\Users\\Dominic\\desktop\\13-6-23 Rerun\\Figure S8 - Leakage Analysis\\Outputs\\run_one_increasing_h2_leakage_yes_normal_output.pickle'
path1 = 'C:\\Users\\Dominic\\desktop\\13-6-23 Rerun\\Figure S8 - Leakage Analysis\\Outputs\\run_two_increasing_h2_leakage_yes_normal_output.pickle'
path2 = 'C:\\Users\\Dominic\\desktop\\13-6-23 Rerun\\Figure S8 - Leakage Analysis\\Outputs\\run_three_increasing_h2_leakage_yes_normal_output.pickle'
path3 = 'C:\\Users\\Dominic\\desktop\\13-6-23 Rerun\\Figure S8 - Leakage Analysis\\Outputs\\run_four_increasing_h2_leakage_yes_normal_output.pickle'
path4 = 'C:\\Users\\Dominic\\desktop\\13-6-23 Rerun\\Figure S8 - Leakage Analysis\\Outputs\\run_five_increasing_h2_leakage_yes_normal_output.pickle'
path5 = 'C:\\Users\\Dominic\\desktop\\13-6-23 Rerun\\Figure S8 - Leakage Analysis\\Outputs\\run_six_increasing_h2_leakage_yes_normal_output.pickle'
path6 = 'C:\\Users\\Dominic\\desktop\\13-6-23 Rerun\\Figure S8 - Leakage Analysis\\Outputs\\run_seven_increasing_h2_leakage_yes_normal_output.pickle'

cost_arr = np.array([])

list1 = [path0, path1, path2, path3, path4, path5, path6]
for path in list1:
    with open(path, 'rb') as f:
        data1 = pickle.load(f)
        case_results = data1['case results']
        cost = case_results['system cost [$/h]']
        cost_arr = np.append(cost_arr, cost)

#Convert from system $/Mwh to $/kWh
cost_arr = cost_arr/1000
print(cost_arr)

#Plot the values
x = np.array([0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24])
y = [cost_arr[0], cost_arr[1], cost_arr[2], cost_arr[3], cost_arr[4], cost_arr[5], cost_arr[6]]/cost_arr[0]*100

# Calculate the regression line
slope, intercept, r_value, p_value, std_err = linregress(x, y)
regression_line = slope * np.array(x) + intercept

# Calculate the R-squared value
r_squared = r_value**2

print(r_squared)

# Plot
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)
fig, ax = plt.subplots(figsize=(6, 6)) #make square
ax.plot(x, y, 'o',color='blue', markeredgecolor='black', markersize=11)
ax.plot
ax.plot(x, regression_line, color='black', label=f'y = {slope:.4f}x + {intercept:.2f}  |  $R^2$ = {r_squared:.4f}')
ax.set_xlabel('Leakage of H2 Storage (%/day)', fontsize=20)
ax.set_ylabel('Percent System Cost\nCompared to Base Case', fontsize=22)
ax.set_title('Percent System Cost\nvs H2 Leakage', fontsize=24, pad = 12)
ax.set_ylim(99,101)
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_xlim(-0.01, 0.25)
ax.set_xticks([0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24])
ax.set_xticklabels(['0', '0.04', '0.08', '0.12', '0.16', '0.2', '0.24']) 
ax.tick_params(axis='both', which='major', labelsize=20)
for tick in ax.get_xticklabels():
    tick.set_rotation(45)

#plt.legend(fontsize=16, loc='upper right')
plt.savefig('C:\\Users\\Dominic\\desktop\\Oahu Results\\system_cost_leakage.png', dpi=300, bbox_inches='tight')
plt.show()