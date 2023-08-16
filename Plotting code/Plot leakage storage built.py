'''This code will plot the leakage rate on the x-axis vs h2 storage built up on the y-axis.'''

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

h2store_arr = np.array([])
fuel_cell_arr = np.array([])

list1 = [path0, path1, path2, path3, path4, path5, path6]

for path in list1:
    with open(path, 'rb') as f:
        data = pickle.load(f)
        component_results = data['component results']
        land_use = component_results['Optimal Capacity']
        h2 = land_use['Store']
        h2store = h2['h2_storage']
        link = land_use['Link']
        fuel_cell = link['fuel_cell']
        h2store_arr = np.append(h2store_arr, h2store)
        fuel_cell_arr = np.append(fuel_cell_arr, fuel_cell)

#Plot the values
x = [0.0004, 0.0478, 0.0952, 0.1426, 0.19, 0.2374, 0.2848]
y = [h2store_arr[0], h2store_arr[1], h2store_arr[2], h2store_arr[3], h2store_arr[4], h2store_arr[5], h2store_arr[6]] / h2store_arr[0] * 100

#Plot the values of fuel_cell_arr on the same plot
y2 = [fuel_cell_arr[0], fuel_cell_arr[1], fuel_cell_arr[2], fuel_cell_arr[3], fuel_cell_arr[4], fuel_cell_arr[5], fuel_cell_arr[6]] / fuel_cell_arr[0] * 100

print(y, y2)

# Calculate the regression line
slope, intercept, r_value, p_value, std_err = linregress(x, y)
regression_line = slope * np.array(x) + intercept

# Calculate the R-squared value
r_squared = r_value**2

# Plot
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)
fig, ax = plt.subplots(figsize=(6, 6)) #make square
ax.plot(x, y, 'o',color='pink',markeredgecolor='black',markersize=9)
ax.plot(x, y2, 'o', color = 'green',markeredgecolor='black',markersize=9)
#ax.plot(x, regression_line, color='black', label=f'y = {slope:.2f}x + {intercept:.2f}  |  $R^2$ = {r_squared:.2f}')
ax.set_xlabel('Leakage of H2 Storage (%/day)', fontsize=14)
ax.set_ylabel(' H2 Storage and Fuel Cell Capacity Built \n(Percentage Compared to \nSmallest Leakage Case)', fontsize=14)
ax.set_title('Hydrogen Storage and Fuel Cell Capacity\n Built As Leakage Increases', fontsize=16, pad = 10)
ax.set_ylim(95, 110)
ax.set_xlim(0, 0.286)
ax.set_xticks([0.0004, 0.0478, 0.0952, 0.1426, 0.19, 0.2374, 0.2848])
ax.set_xticklabels(['0.0004', '0.0478', '0.0952', '0.1426', '0.19', '0.2374', '0.2848']) 
ax.tick_params(axis='both', which='major', labelsize=14)
#make the xtick labels 45 degrees
for tick in ax.get_xticklabels():
    tick.set_rotation(45)

ax.legend(['H2 Storage', 'Fuel Cell'], loc='upper right', fontsize=14)
plt.savefig('C:\\Users\\Dominic\\desktop\\Oahu Results\\h2_storage_built_leakage.png', dpi=300, bbox_inches='tight')
plt.show()
