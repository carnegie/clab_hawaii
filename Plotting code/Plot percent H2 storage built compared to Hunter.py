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

path0 = 'C:\\Users\\Dominic\\desktop\\fourteen_year_above_storage_jackie_price_no_normal_all_mw_e6.pickle'
path1 = 'C:\\Users\\Dominic\\desktop\\run one increasing h2 storage cost no normal.pickle'
path2 = 'C:\\Users\\Dominic\\desktop\\run two increasing h2 storage cost no normal.pickle'
path3 = 'C:\\Users\\Dominic\\desktop\\run three increasing h2 storage cost no normal.pickle'
path4 = 'C:\\Users\\Dominic\\desktop\\run four increasing h2 storage cost no normal.pickle'
path5 = 'C:\\Users\\Dominic\\desktop\\run five increasing h2 storage cost no normal.pickle'

h2store_arr = np.array([])

list1 = [path0, path1, path2, path3, path4, path5]

for path in list1:
    with open(path, 'rb') as f:
        data = pickle.load(f)
        component_results = data['component results']
        land_use = component_results['Optimal Capacity']
        h2 = land_use['Store']
        h2store = h2['h2_storage']
        h2store_arr = np.append(h2store_arr, h2store)
print(h2store_arr)

#Convert the values to percent of the first value
h2store_arr = (h2store_arr/h2store_arr[0])*100
print(h2store_arr)

#Plot the values
x = [0.140060273, 0.240060273, 0.340060273, 0.440060273, 0.540060273, 0.640060273]
y = [h2store_arr[0], h2store_arr[1], h2store_arr[2], h2store_arr[3], h2store_arr[4], h2store_arr[5]]

# Calculate the regression line
slope, intercept, r_value, p_value, std_err = linregress(x, y)
regression_line = slope * np.array(x) + intercept

# Calculate the R-squared value
r_squared = r_value**2


fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)
fig, ax = plt.subplots(figsize=(6, 6)) #make square
ax.plot(x, y, 'o',color='blue', label='Data')
ax.plot(x, regression_line, color='black', label=f'y = {slope:.2f}x + {intercept:.2f}  |  $R^2$ = {r_squared:.2f}')
ax.set_xlabel('Cost of H2 Storage ($/kW/hour)', fontsize=14)
ax.set_ylabel('Percent H2 Storage Built \n Compared to Base Case', fontsize=14)
ax.set_title('Percent of Hydrogen Storage Built Compared \nto Case Using Costs from Hunter et al.', fontsize=16, pad = 20)
ax.set_ylim(0, 110)
ax.set_xlim(0.13, 0.65)
ax.set_xticks([0.140060273, 0.240060273, 0.340060273, 0.440060273, 0.540060273, 0.640060273])
ax.set_xticklabels(['0.14', '0.24', '0.34', '0.44', '0.54', '0.64']) #Shortened values to 2 decimals
ax.tick_params(axis='both', which='major', labelsize=14)

plt.legend()
plt.savefig('C:\\Users\\Dominic\\desktop\\Oahu Results\\percent_h2_storage_built.png', dpi=300, bbox_inches='tight')
plt.show()
