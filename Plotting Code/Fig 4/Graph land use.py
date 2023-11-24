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

#Input Paths
no_pgp = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure 4 - Optimized System Capacity/Outputs/oahu_optimized_system_no_normal_no_PGP_output.pickle'
pgp_above = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure 4 - Optimized System Capacity/Outputs/oahu_optimized_system_no_normal_w_PGP_output.pickle'

solar_q = 'orange'
wind_q = 'blue'
pgp_q = 'pink'
batt_q = 'purple'
electrolysis_q = 'gray'
fuelcell_q = 'green'


combo_wind_solar = np.array([])
wind_arr = np.array([])
battery_arr = np.array([])
h2store_arr = np.array([])
fuelcell_arr = np.array([])
electrolyzer_arr = np.array([])

with open(no_pgp, 'rb') as f:
    data1 = pickle.load(f)
    component_results = data1['component results']
    capacity = component_results['Optimal Capacity [MW]']
    generator = capacity['Generator']
    wind = generator['wind']
    solar = generator['solar']
    batt = capacity['StorageUnit']
    battery = batt['battery']
    h2store = [0]
    fuelcell = [0]
    electrolyzer = [0]

    '''
    #Account for the fact that 3965.3305 MW solar can be built on existing developments, thus taking up no more land
    solar = solar - 3965.3305
    if solar < 0:
        solar = 0
    '''
    '''
    #Account for the fact that (1/8.112107623) MW of wind can be built per MW of solar, since turbines can be built on the same land as PV
    if solar > 0:
        wind = wind - (solar/8.112107623)
    else:
        wind = wind
    '''
    combo_wind_solar = np.append(combo_wind_solar, solar)
    wind_arr = np.append(wind_arr, wind)
    battery_arr = np.append(battery_arr, battery)
    h2store_arr = np.append(h2store_arr, h2store)
    fuelcell_arr = np.append(fuelcell_arr, fuelcell)
    electrolyzer_arr = np.append(electrolyzer_arr, electrolyzer)
    
#======================================================== If you want to plot two side-by-side =====================================  
with open(pgp_above, 'rb') as f:
    data1 = pickle.load(f)
    component_results = data1['component results']
    capacity = component_results['Optimal Capacity [MW]']
    generator = capacity['Generator']
    wind = generator['wind']
    solar = generator['solar']
    batt = capacity['StorageUnit']
    battery = batt['battery']
    h2 = capacity['Store']
    h2store = h2['h2_storage']
    cell = capacity['Link']
    fuelcell = cell['fuel_cell']
    electrolysis = cell['electrolysis']

    '''
    #Account for the fact that 3965.3305MW solar can be built on existing developments, thus taking up no more land
    solar = solar - 3965.3305
    if solar < 0:
        solar = 0
    '''
    '''
    #Account for the fact that (1/8.112107623) GW of onwind can be built per GW of solar, since turbines can be built on the same land as PV
    if solar > 0:
        wind = wind - (solar/8.112107623)
    else:
        wind = wind
    '''
    combo_wind_solar = np.append(combo_wind_solar, solar)
    wind_arr = np.append(wind_arr, wind)
    battery_arr = np.append(battery_arr, battery)
    h2store_arr = np.append(h2store_arr, h2store)
    fuelcell_arr = np.append(fuelcell_arr, fuelcell)
    electrolyzer_arr = np.append(electrolyzer_arr, electrolysis)

full_wind_space = np.array([])
full_wind_space = (wind_arr*(0.1809))
print('full wind space needed',full_wind_space)
    #Append the value of sys_land to sys_land_use
    #sys_land_use = np.append(sys_land_use, sys_land)
wind_arr = (wind_arr*(0.1809*0.02))
combo_wind_solar = (combo_wind_solar*0.0223)
battery_arr = (battery_arr*0.0000249)
h2store_arr = (h2store_arr*0.0000267)
electrolyzer_arr = (electrolyzer_arr*0.0000250)
fuelcell_arr = (fuelcell_arr*0.0000198)



print('combo wind solar',combo_wind_solar)
print('wind', wind_arr)
print('battery arr',battery_arr)
print('h2 store',h2store_arr)
print('fuel cell',fuelcell_arr)
print('electrolyzer',electrolyzer_arr)

print(combo_wind_solar+full_wind_space+battery_arr+h2store_arr+fuelcell_arr+electrolyzer_arr)
N = 2
#ind = np.arange(N)    

data1 = combo_wind_solar
data2 = full_wind_space #can use wind_arr to get just the turbine space without inlcuding the unused land in between turbines
data3 = battery_arr
data4 = h2store_arr
data5 = electrolyzer_arr
data6 = fuelcell_arr

ind = ['Without PGP','With PGP']
width = 0.7

params = {'legend.fontsize': 'medium',
         'axes.labelsize': 'large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'medium',
         'ytick.labelsize':'large'}
pylab.rcParams.update(params)


fig = plt.figure(figsize=(6,10))
ax1 = plt.subplot2grid((1,1), (0, 0), colspan=1, rowspan=1)
p1 = ax1.bar(ind, data1, width, color=solar_q)#hatch='///'
#https://stackoverflow.com/questions/53849888/make-patches-bigger-used-as-legend-inside-matplotlib
p2 = ax1.bar(ind, data2, width, bottom=data1, color=wind_q)
p3 = ax1.bar(ind, data3, width, bottom=data1+data2,color=batt_q)
p4 = ax1.bar(ind, data4, width, bottom=data1+data2+data3, color=pgp_q)
p5 = ax1.bar(ind, data5, width, bottom=data1+data2+data3+data4, color=pgp_q, hatch='//')
p6 = ax1.bar(ind, data6, width, bottom=data1+data2+data3+data4+data5, color=pgp_q, hatch='\\\\')




plt.ylabel(r'System Land Use (km$^2$)',labelpad = 6)

plt.xticks(rotation=45, ha='right')

ax = plt.gca() 
# Set the color of the spines
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Set the linewidth of the spines
ax.spines['left'].set_linewidth(1)
ax.spines['bottom'].set_linewidth(1)

plt.grid(False)
ax.set_ylim(0, 350)
ax.yaxis.set_major_locator(ticker.MultipleLocator(50))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
plt.tick_params(axis='y', which='both', left='on', labelleft='on')
ax.set_title('Oahu Renewable Energy\nSystem Land Use', y=1.015)


#make x and y axis text fontsize 14
for item in ([ax.xaxis.label] + ax.get_xticklabels() + ax.get_yticklabels()):
    item.set_fontsize(24)
    
for item in ([ax.xaxis.label] + ax.get_xticklabels()):    
    item.set_rotation(45)
    
    
ax.yaxis.label.set_fontsize(26)

ax.title.set_fontsize(30)

plt.xticks(ind, ('Modeled\nWithout HES', 'Modeled\nWith HES'))
y = ['Solar', 'Wind', 'Battery', 'H2 Storage', 'Electrolyzer', 'Fuel Cell']
legend = plt.legend(reversed([p1, p2, p3, p4, p5, p6]), reversed(y), loc="best", bbox_to_anchor=(1, 0.8), fontsize='24', edgecolor='black')


for handle in legend.legendHandles:
    handle.set_edgecolor('black')

for bar in p1 + p2 + p3 + p4 + p5 + p6:
    bar.set_linewidth(1)
    bar.set_edgecolor('black')

plt.xticks(ha='center')

# a dashed line at 3965.3305*0.0223 to represent the land used by solar on existing developments
plt.axhline(y=3965.3305*0.0223, color='k', linestyle='--', linewidth=1)
plt.text(1.47, 3965.3305*0.0223-3.5, '*', color='k', fontsize=25, ha='center', va='center')
plt.text(1.53, 3965.3305*0.0223+5.5, 'Solar capacity below\ndashed line could be\nbuilt on rooftops,\nrequiring zero land use', color='k', fontsize=22, ha='left', va='top')
###Unused below###
#Add a dashed line at 3965.3305*0.0223 to represent the land used by solar on existing developments
#plt.axhline(y=3965.3305*0.0223, xmin=0.46, xmax=0.54,color='k', linestyle='-', linewidth=2)
#x_position = 0.5
#ax1.axvline(x_position, ymin=0, ymax=0.25,color='k', linestyle='--', linewidth=2)  # Customize line color, style, and width

plt.savefig('C:\\Users\\Dominic\\desktop\\Oahu Results\\Oahu Renewable Energy System Land Use.jpg', dpi = 300, bbox_inches='tight')
plt.show()