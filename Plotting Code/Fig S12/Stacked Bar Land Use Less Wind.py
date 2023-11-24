'''This code will plot the land use of optimized Oahu systems with 
different levels of wind generation allowed'''

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

solar_q = 'orange'
wind_q = 'blue'
pgp_q = 'pink'
batt_q = 'purple'
electrolysis_q = 'gray'
fuelcell_q = 'green'

#Input paths
no_hes_0 = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something4 - Decreasing Land Use/No PGP/Outputs/dec_land_use_no_normal_no_PGP_0wind_output.pickle'
no_hes_25 = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something4 - Decreasing Land Use/No PGP/Outputs/dec_land_use_no_normal_no_PGP_25wind_output.pickle'
no_hes_50 = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something4 - Decreasing Land Use/No PGP/Outputs/dec_land_use_no_normal_no_PGP_50wind_output.pickle'
no_hes_75 = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something4 - Decreasing Land Use/No PGP/Outputs/dec_land_use_no_normal_no_PGP_75wind_output.pickle'
no_hes_100 = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something4 - Decreasing Land Use/No PGP/Outputs/dec_land_use_no_normal_no_PGP_100wind_output.pickle'

yes_hes_0 = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something4 - Decreasing Land Use/Yes PGP/Outputs/dec_land_use_no_normal_yes_PGP_0wind_output.pickle'
yes_hes_25 = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something4 - Decreasing Land Use/Yes PGP/Outputs/dec_land_use_no_normal_yes_PGP_25wind_output.pickle'
yes_hes_50 = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something4 - Decreasing Land Use/Yes PGP/Outputs/dec_land_use_no_normal_yes_PGP_50wind_output.pickle'
yes_hes_75 = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something4 - Decreasing Land Use/Yes PGP/Outputs/dec_land_use_no_normal_yes_PGP_75wind_output.pickle'
yes_hes_100 = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something4 - Decreasing Land Use/Yes PGP/Outputs/dec_land_use_no_normal_yes_PGP_100wind_output.pickle'


combo_wind_solar = np.array([])
wind_arr = np.array([])
battery_arr = np.array([])
h2store_arr = np.array([])
fuelcell_arr = np.array([])
electrolyzer_arr = np.array([])


with open(no_hes_0, 'rb') as f:
    data1 = pickle.load(f)
    component_results = data1['component results']
    capacity = component_results['Optimal Capacity [MW]']
    generator = capacity['Generator']
    solar = generator['solar']
    batt = capacity['StorageUnit']
    battery = batt['battery']
    h2store = [0]
    fuelcell = [0]
    electrolyzer = [0]
    wind = [0]    

    '''
    #Account for the fact that 3965.3305 MW solar can be built on existing developments, thus taking up no more land
    solar = solar - 3965.3305
    if solar < 0:
        solar = 0
    
    
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
    

noHES = [no_hes_25, no_hes_50, no_hes_75, no_hes_100]
for no_pgp in noHES:
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

N = 5
ind = np.arange(N)    

data1 = combo_wind_solar
data2 = full_wind_space #can use wind_arr to get just the turbine space without inlcuding the unused land in between turbines
data3 = battery_arr
data4 = h2store_arr
data5 = electrolyzer_arr
data6 = fuelcell_arr

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

plt.ylabel(r'System Land Use (km$^2$)',labelpad = 6)
plt.xlabel('Percent of Wind Capacity\n Compared to Base Case')

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
ax.set_title('Land Use With Wind\nCapacity Constraints', y=1.)


#make x and y axis text fontsize 14
for item in ([ax.xaxis.label] + ax.get_xticklabels() + ax.get_yticklabels()):
    item.set_fontsize(24)
    
    
ax.yaxis.label.set_fontsize(26)

ax.title.set_fontsize(30)

plt.xticks(ind, ('0% wind', '25% wind', '50% wind', '75% wind', '100% wind'))
y = ['Solar', 'Wind', 'Battery']
legend = plt.legend(reversed([p1, p2, p3]), reversed(y), loc="best", bbox_to_anchor=(1, 0.6), fontsize='22', edgecolor='black')


for handle in legend.legendHandles:
    handle.set_edgecolor('black')

for bar in p1 + p2 + p3:
    bar.set_linewidth(1)
    bar.set_edgecolor('black')
    
# a dashed line at 3965.3305*0.0223 to represent the land used by solar on existing developments
plt.axhline(y=3965.3305*0.0223, color='k', linestyle='--', linewidth=1)
plt.text(4.7, 3965.3305*0.0223-3.5, '*', color='k', fontsize=25, ha='center', va='center')
plt.text(4.9, 3965.3305*0.0223+5.5, 'Solar capacity below\ndashed line could be\nbuilt on rooftops,\nrequiring zero land use', color='k', fontsize=22, ha='left', va='top')

plt.savefig('C:\\Users\\Dominic\\desktop\\Oahu Results\\Dec wind amount no HES.jpg', dpi = 300, bbox_inches='tight')
plt.show()
