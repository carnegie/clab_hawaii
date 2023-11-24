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


##==========================================
# Tech colors
##==========================================

solar_q = 'orange'
wind_q = 'blue'
pgp_q = 'pink'
batt_q = 'purple'
fuelcell_q = 'green'
electrolysis_q = 'gray'

sys_cap = []
wind_cap = []
solar_cap = []
batt_cap = []
pgp_cap = []
fuelcell_cap = []
electrolyzer_cap = []

#Input Paths
no_pgp = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure 4 - Optimized System Capacity/Outputs/oahu_optimized_system_no_normal_no_PGP_output.pickle'
pgp_above = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure 4 - Optimized System Capacity/Outputs/oahu_optimized_system_no_normal_w_PGP_output.pickle'

with open(no_pgp, 'rb') as f:
        data1 = pickle.load(f)
        component_results = data1['component results']
        capacity = component_results['Optimal Capacity [MW]']
        generator = capacity['Generator']
        wind = generator['wind']
        solar = generator['solar']
        batt = capacity['StorageUnit']
        battery = batt['battery']

        wind_cap.append(wind)
        solar_cap.append(solar)
        batt_cap.append(battery)
        pgp_cap.append(0)
        fuelcell_cap.append(0)
        electrolyzer_cap.append(0)

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

        wind_cap.append(wind)
        solar_cap.append(solar)
        batt_cap.append(battery)
        pgp_cap.append(h2store)
        fuelcell_cap.append(fuelcell)
        electrolyzer_cap.append(electrolysis)

wind_cap = np.array(wind_cap)
solar_cap = np.array(solar_cap)
batt_cap = np.array(batt_cap)
h2_store = np.array(pgp_cap)
fuelcell_cap = np.array(fuelcell_cap)
electrolyzer_cap = np.array(electrolyzer_cap)

batt_cap = batt_cap * 4 #Multiply batt_cap by charging time (4) to account for pypsa giving built power while we want build energy storage

print(wind_cap)
print(solar_cap)
print(batt_cap)
print(h2_store)
print(fuelcell_cap)
print(electrolyzer_cap)

wind_cap = wind_cap/1000
solar_cap=solar_cap/1000
batt_cap=batt_cap/1000
h2_store=h2_store/1000
fuelcell_cap=fuelcell_cap/1000
electrolyzer_cap=electrolyzer_cap/1000




#Prep for plotting    
N = 2
ind = np.arange(N)    # the x locations for the groups
width = 0.7       # the width of the bars: can also be len(x) sequence

data1 = np.array(solar_cap) #pv
data2 = np.array(wind_cap) #wind
data3 = np.array(batt_cap) #batt
data4 = np.array(h2_store)
data5 = np.array(electrolyzer_cap)
data6 = np.array(fuelcell_cap)

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
ax1 = plt.subplot2grid((1, 1), (0, 0), colspan=1, rowspan=1)
#p1 = ax1.bar(ind, data1, width, color=solar_q)
#p2 = ax1.bar(ind, data2, width, bottom=data1, color=wind_q)
p3 = ax1.bar(ind, data3, width, color=batt_q)
p4 = ax1.bar(ind, data4, width, bottom=data3, color=pgp_q)
#p5 = ax1.bar(ind, data5, width, bottom=data3+data4, color=electrolysis_q)
#p6 = ax1.bar(ind, data6, width, bottom=data3+data4+data5, color=fuelcell_q)

plt.ylabel('System Storage Capacity\n(GWh)')
plt.xticks(rotation=45, ha='right')

ax = plt.gca() 
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Set the linewidth of the spines
ax.spines['left'].set_linewidth(1)
ax.spines['bottom'].set_linewidth(1)

plt.grid(False)


ax.set_ylim(0, 80)
ax.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(4))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax.set_title('Oahu Optimized Renewable\nSystem Storage Capacity', y=1.015)

#make x and y axis text fontsize 14
for item in ([ax.xaxis.label] + ax.get_xticklabels() + ax.get_yticklabels()):
    item.set_fontsize(24)
    
for item in ([ax.xaxis.label] + ax.get_xticklabels()):    
    item.set_rotation(45)


ax.yaxis.label.set_fontsize(28)

ax.title.set_fontsize(30)

#plt.xticks(ind, ('PV, Wind, Li-ion Battery', 'PV, Wind, Li-ion Battery, PGP (Above Ground Storage)', 'PV, Wind, Li-ion Battery, PGP (Below Ground Storage)'))
plt.xticks(ind, ('Without HES', 'With HES'))
y = ['Battery', 'H2 Storage']
#legend = plt.legend(reversed([p3, p4]), reversed(y), loc="best", bbox_to_anchor=(1, 0.7), fontsize='12', edgecolor='black')

for handle in legend.legendHandles:
    handle.set_edgecolor('black')

for bar in p3 + p4:
    bar.set_linewidth(1)
    bar.set_edgecolor('black')

plt.xticks(ha='center')

plt.savefig('C:\\Users\\Dominic\\desktop\\Oahu Results\\Oahu Optimized Renewable System Storage Capacity.jpg', dpi = 300, bbox_inches='tight')
plt.show()
