'''
This code will calculate and graph the land use of each technology in the Oahu system. It will also graph the land use of the entire system.
'''
from __future__ import division
import numpy as np
from os import listdir
import os
import pickle
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import matplotlib.gridspec as gridspec
import matplotlib.ticker as ticker

import datetime
from matplotlib.dates import drange
from matplotlib.ticker import FormatStrFormatter
import pandas as pd

path1 = '/Users/Dominic/desktop/fourteen_year_land_use/fourteen_year_above_storage_no_normal_all_mw_e6.pickle'
path2 = '/Users/Dominic/desktop/fourteen_year_land_use/fourteen_year_no_normal_space_optimization.pickle'


combo_wind_solar = np.array([])
wind_arr = np.array([])
battery_arr = np.array([])
h2store_arr = np.array([])
fuelcell_arr = np.array([])

with open(path1, 'rb') as f:
    data = pickle.load(f)
    component_results = data['component results']
    #print(component_results)
    land_use = component_results['Optimal Capacity']
    #print(land_use)
    gen = land_use['Generator']
    #print(gen)
    wind = gen['onwind']
    wind = wind*(10**3)
    print(wind)
    solar = gen['solar']
    solar = solar*(10**3)
    print(solar)
    batt = land_use['StorageUnit']
    #print(batt)
    battery = batt['battery']
    #print(battery)
    h2 = land_use['Store']
    #print(h2)
    h2store = h2['h2_storage']
    #print(h2store)
    cell = land_use['Link']
    #print(cell)
    fuelcell = cell['fuel_cell']
    #print(fuelcell)
    
    #all the above values are in GW
    #Account for the fact that 3.9653305GW solar can be built on existing developments, thus taking up no more land
    solar = solar - 3.9653305
    if solar < 0:
        solar = 0
    
    #Account for the fact that (1/6) GW of onwind can be built per GW of solar, since turbines can be built on the same land as PV
    if solar > 0:
        wind = wind - (solar/6)
    else:
        wind = wind

    combo_wind_solar = np.append(combo_wind_solar, solar)
    wind_arr = np.append(wind_arr, wind)
    battery_arr = np.append(battery_arr, battery)
    h2store_arr = np.append(h2store_arr, h2store)
    fuelcell_arr = np.append(fuelcell_arr, fuelcell)
'''  
#======================================================== If you want to plot two side-by-side =====================================  
with open(path2, 'rb') as f:
    data = pickle.load(f)
    component_results = data['component results']
    #print(component_results)
    land_use = component_results['Optimal Capacity']
    #print(land_use)
    gen = land_use['Generator']
    #print(gen)
    wind = gen['onwind']
    wind = wind/(10**3)
    print(wind)
    solar = gen['solar']
    solar = solar/(10**3)
    print(solar)
    batt = land_use['StorageUnit']
    #print(batt)
    battery = batt['battery']
    #print(battery)
    h2 = land_use['Store']
    #print(h2)
    h2store = h2['h2_storage']
    #print(h2store)
    cell = land_use['Link']
    #print(cell)
    fuelcell = cell['fuel_cell']
    #print(fuelcell)
    
    #all the above values are in GW
    #Account for the fact that 3.9653305GW solar can be built on existing developments, thus taking up no more land
    solar = solar - 3.9653305
    if solar < 0:
        solar = 0
    
    #Account for the fact that (1/6) GW of onwind can be built per GW of solar, since turbines can be built on the same land as PV
    if solar > 0:
        wind = wind - (solar/6)
    else:
        wind = wind

combo_wind_solar = np.append(combo_wind_solar, solar)
wind_arr = np.append(wind_arr, wind)
battery_arr = np.append(battery_arr, battery)
h2store_arr = np.append(h2store_arr, h2store)
fuelcell_arr = np.append(fuelcell_arr, fuelcell)


    #Append the value of sys_land to sys_land_use
    #sys_land_use = np.append(sys_land_use, sys_land)
wind_arr = (wind_arr*121.4058)
combo_wind_solar = (combo_wind_solar*20.2343)
battery_arr = (battery_arr*0.092916/1000)
h2store_arr = (h2store_arr*0.0046417/1000)
fuelcell_arr = (fuelcell_arr*0.250905/1000)
'''

wind_arr = (wind_arr*121.4058)
combo_wind_solar = (combo_wind_solar*20.2343)
battery_arr = (battery_arr*0.092916/1000)
h2store_arr = (h2store_arr*0.0046417/1000)
fuelcell_arr = (fuelcell_arr*0.250905/1000)

N = 2
#ind = np.arange(N)    

data1 = combo_wind_solar
data2 = wind_arr
data3 = battery_arr
data4 = fuelcell_arr
data5 = h2store_arr

ind = ['Least Cost System']
width = 0.7

params = {'legend.fontsize': 'medium',
         'axes.labelsize': 'large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'medium',
         'ytick.labelsize':'large'}
pylab.rcParams.update(params)

fig = plt.figure(figsize=(6,10))
ax1 = plt.subplot2grid((2, 2), (0, 0), colspan=1, rowspan=1)
p1 = ax1.bar(ind, data1, width, color='orange', hatch='///', edgecolor='blue')
#https://stackoverflow.com/questions/53849888/make-patches-bigger-used-as-legend-inside-matplotlib
p2 = ax1.bar(ind, data2, width, bottom=data1, color='blue',edgecolor='blue')
p3 = ax1.bar(ind, data3, width, bottom=data1+data2, color='purple', edgecolor='purple')
p4 = ax1.bar(ind, data4, width, bottom=data1+data2+data3, color='green')
p5 = ax1.bar(ind, data5, width, bottom=data1+data2+data3+data4, color='pink')



plt.ylabel('System Land Use (km^2)',labelpad = 6)

plt.xticks(rotation=45, ha='right')

ax = plt.gca() 
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
#plt.grid(True, which = 'major', axis = 'y', c = 'lightgray')

ax.set_ylim(0, 200)
ax.yaxis.set_major_locator(ticker.MultipleLocator(50))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax.set_title('Oahu Renewable Energy System Land Use', y=1.05)

#plt.xticks(ind, ('Least Cost System', 'Space Optimized System'))

#y = ['Wind and Solar','Wind Only', 'Battery', 'Fuel Cell', 'Hydrogen Storage']
y = ['Wind and Solar','Wind Only', 'Battery']
ax1.legend(y, loc="center right", bbox_to_anchor=(1.9, 0.5), fontsize = 12)
##======================================================================================================
# Save plots as jpg
##======================================================================================================


plt.savefig('Oahu Land Use.jpg', dpi = 300, bbox_inches='tight')
plt.show()
