'''
This code will calculate and graph the land use of each technology in the Oahu system. It will also graph the land use of the entire system.
'''
from __future__ import division
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
import pandas as pd


##==========================================
# Tech colors
##==========================================

solar_q = 'orange'
wind_q = 'blue'
batt_q = 'purple'
h2storage_q = 'pink'
fuel_cell_q = 'green'


wind_land = [(1613.00*(30*0.00404686)),(266.77*(30*0.00404686))]
print(wind_land)
solar_land  = [(6500.65*(5*0.00404686)),(4907.54*(5*0.00404686))]
print(solar_land)
batt_land  = [(6634.80*(0.02296*0.00404686)),(3805.59*(0.02296*0.00404686))]
print(batt_land)
fuel_cell_land =[(0*(0.062*0.00404686)),(687.63*(0.062*0.00404686))]
print(fuel_cell_land)



cases = listdir('/Users/Dominic/Desktop/Oahu Results/(Pypsa) costs using mean nsrdb and wind, 14 year/plotting/')


#Prep for plotting    
N = 2
ind = np.arange(N)    # the x locations for the groups
width = 0.7       # the width of the bars: can also be len(x) sequence

data1 = np.array(wind_land)
data2 = np.array(solar_land)
data3 = np.array(batt_land) 
data4 = np.array(fuel_cell_land)

##======================================================================================================
# Make bar graph
##======================================================================================================

params = {'legend.fontsize': 'medium',
         'axes.labelsize': 'large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'medium',
         'ytick.labelsize':'large'}
pylab.rcParams.update(params)

fig = plt.figure(figsize=(8,10))
ax1 = plt.subplot2grid((2, 2), (0, 0), colspan=1, rowspan=1)
p1 = ax1.bar(ind, data1, width, color=wind_q)
p2 = ax1.bar(ind, data2, width, bottom=data1, color=solar_q)
p3 = ax1.bar(ind, data3, width, bottom=data1+data2, color=batt_q)
p4 = ax1.bar(ind, data4, width, bottom=data1+data2+data3, color=fuel_cell_q)



plt.ylabel('System Land Use (km^2)')
plt.xticks(rotation=45, ha='right')

ax = plt.gca() 
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
#plt.grid(True, which = 'major', axis = 'y', c = 'lightgray')

ax.set_ylim(0, 350)
ax.yaxis.set_major_locator(ticker.MultipleLocator(50))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax.set_title('Oahu Renewable Energy System Land Use', y=1.05)

plt.xticks(ind, ('Least Cost System', 'Least Cost Below Ground H2 Storage System'))


y = ['Wind','Solar', 'Battery', 'Fuel Cell']
ax1.legend(y, loc="upper right")

##======================================================================================================
# Save plots as jpg
##======================================================================================================


plt.savefig('Oahu Land Use.jpg', dpi = 300, bbox_inches='tight')
plt.show()
