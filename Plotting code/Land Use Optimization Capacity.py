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
solarroof_q = 'red'
wind_q = 'blue'
batt_q = 'purple'
pgp_q = 'pink'


sys_costs = []
wind_costs = []
solar_costs = []
solarroof_costs = []
batt_costs = []
pgp_costs = []

cases = listdir('/Users/Dominic/Desktop/Oahu Results/(Pypsa) costs using mean nsrdb and wind, 14 year/plotting/')
print(cases)

sys_costs = [711702,14.76521]
wind_costs = [0, 1.61622]
solar_costs = [0.3579625,2.539279]
solarroof_costs = [3.965331,3.965331]
batt_costs = [21.56353, 6.64438]
pgp_costs = [690.1347,0]


#Prep for plotting    
N = 2
ind = np.arange(N)    # the x locations for the groups
width = 0.7       # the width of the bars: can also be len(x) sequence

data1 = np.array(solar_costs) #pv
data2 = np.array(solarroof_costs)
data3 = np.array(wind_costs) #wind
data4 = np.array(batt_costs) #batt
data5 = np.array(pgp_costs)

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
p1 = ax1.bar(ind, data1, width, color=solar_q)
p2 = ax1.bar(ind, data2, width, bottom=data1, color=solarroof_q)
p3 = ax1.bar(ind, data3, width, bottom=data1+data2, color=wind_q)
p4 = ax1.bar(ind, data4, width, bottom=data1+data2+data3, color=batt_q)
p5 = ax1.bar(ind, data5, width, bottom=data1+data2+data3+data4, color=pgp_q)



plt.ylabel('System Capacity (GW or GWh)')
plt.xticks(rotation=45, ha='right')

ax = plt.gca() 
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
#plt.grid(True, which = 'major', axis = 'y', c = 'lightgray')

ax.set_ylim(0, 50)
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(2))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax.set_title('Oahu Renewable Energy System Optimized for Minimal Land Use', y=1.05)

#plt.xticks(ind, ('PV, Wind, Li-ion Battery', 'PV, Wind, Li-ion Battery, PGP (Above Ground Storage)', 'PV, Wind, Li-ion Battery, PGP (Below Ground Storage)'))
plt.xticks(ind, ('Optimal Land Use', 'Least Cost'))
y = ['Solar','Rooftop Solar', 'Wind', 'Battery', 'H2 Storage']
ax1.legend(y, loc="upper right")

#xlocs=[0,1]
#for i, v in enumerate(sys_costs):
   #plt.text(xlocs[i] - 0.35, v + 0.01, format(v, '.2f'))

##======================================================================================================
# Save plots as jpg
##======================================================================================================


plt.savefig('Oahu Renewable Energy System Optimized for Minimal Land Use Zoomed.jpg', dpi = 300, bbox_inches='tight')
plt.show()
