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

path0 = 'C:\\Users\\covel\\OneDrive\\desktop\\13-6-23 Rerun\\Figure S8 - Leakage Analysis\\Outputs\\run_one_increasing_h2_leakage_yes_normal_output.pickle'
path1 = 'C:\\Users\\covel\\OneDrive\\desktop\\13-6-23 Rerun\\Figure S8 - Leakage Analysis\\Outputs\\run_two_increasing_h2_leakage_yes_normal_output.pickle'
path2 = 'C:\\Users\\covel\\OneDrive\\desktop\\13-6-23 Rerun\\Figure S8 - Leakage Analysis\\Outputs\\run_three_increasing_h2_leakage_yes_normal_output.pickle'
path3 = 'C:\\Users\\covel\\OneDrive\\desktop\\13-6-23 Rerun\\Figure S8 - Leakage Analysis\\Outputs\\run_four_increasing_h2_leakage_yes_normal_output.pickle'
path4 = 'C:\\Users\\covel\\OneDrive\\desktop\\13-6-23 Rerun\\Figure S8 - Leakage Analysis\\Outputs\\run_five_increasing_h2_leakage_yes_normal_output.pickle'
path5 = 'C:\\Users\\covel\\OneDrive\\desktop\\13-6-23 Rerun\\Figure S8 - Leakage Analysis\\Outputs\\run_six_increasing_h2_leakage_yes_normal_output.pickle'
path6 = 'C:\\Users\\covel\\OneDrive\\desktop\\13-6-23 Rerun\\Figure S8 - Leakage Analysis\\Outputs\\run_seven_increasing_h2_leakage_yes_normal_output.pickle'

h2store_arr = np.array([])
fuel_cell_arr = np.array([])
electrolysis_arr = np.array([])

list1 = [path0, path1, path2, path3, path4, path5, path6]

for path in list1:
    with open(path, 'rb') as f:
        data = pickle.load(f)
        component_results = data['component results']
        land_use = component_results['Optimal Capacity [MW]']
        h2 = land_use['Store']
        h2store = h2['h2_storage']
        link = land_use['Link']
        fuel_cell = link['fuel_cell']
        electrolysis = link['electrolysis']
        h2store_arr = np.append(h2store_arr, h2store)
        fuel_cell_arr = np.append(fuel_cell_arr, fuel_cell)
        electrolysis_arr = np.append(electrolysis_arr, electrolysis)

#Plot the values
x = np.array([0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24])
y = [h2store_arr[0], h2store_arr[1], h2store_arr[2], h2store_arr[3], h2store_arr[4], h2store_arr[5], h2store_arr[6]] / h2store_arr[0] * 100

#Plot the values of fuel_cell_arr on the same plot
y2 = [fuel_cell_arr[0], fuel_cell_arr[1], fuel_cell_arr[2], fuel_cell_arr[3], fuel_cell_arr[4], fuel_cell_arr[5], fuel_cell_arr[6]] / fuel_cell_arr[0] * 100

#Plot the values of electrolysis_arr on the same plot
y3 = [electrolysis_arr[0], electrolysis_arr[1], electrolysis_arr[2], electrolysis_arr[3], electrolysis_arr[4], electrolysis_arr[5], electrolysis_arr[6]] / electrolysis_arr[0] * 100

print('h2 storage',y, '\nfuel cell',y2, 'electrolyzer',y3)

# Calculate the regression line
slope, intercept, r_value, p_value, std_err = linregress(x, y)
regression_line = slope * np.array(x) + intercept

# Calculate the R-squared value
r_squared = r_value**2

# Plot
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)
fig, ax = plt.subplots(figsize=(6, 6)) #make square
ax.plot(x, y2, 'o', color = 'green',markeredgecolor='black',markersize=11)
ax.plot(x, y3, 'o',color='gray',markeredgecolor='black',markersize=11)
ax.plot(x, y, 'o',color='pink',markeredgecolor='black',markersize=11)
#ax.plot(x, regression_line, color='black', label=f'y = {slope:.2f}x + {intercept:.2f}  |  $R^2$ = {r_squared:.2f}')
ax.set_xlabel('Leakage of H$_2$ Storage (%/day)', fontsize=20)
ax.set_ylabel('Percent HES Components\nDeployed Compared to Base Case', fontsize=20)
#ax.set_title('Percent HES Components\nBuilt vs H2 Leakage', fontsize=24, pad = 12)
ax.set_ylim(85, 115)
ax.set_xlim(-0.005, 0.25)
ax.set_xticks([0, 0.04, 0.08, 0.12, 0.16, 0.2,0.24])
ax.set_xticklabels(['0', '0.04', '0.08', '0.12', '0.16', '0.2', '0.24']) 
ax.tick_params(axis='both', which='major', labelsize=20)
#make the xtick labels 45 degrees
for tick in ax.get_xticklabels():
    tick.set_rotation(45)

ax.legend(['Fuel Cell','Electrolyzer', 'H2 Storage'], loc='upper left', fontsize=20)
#plt.savefig('C:\\Users\\covel\\OneDrive\\desktop\\Oahu Results\\h2_storage_built_leakage.png', dpi=300, bbox_inches='tight')
plt.show()
