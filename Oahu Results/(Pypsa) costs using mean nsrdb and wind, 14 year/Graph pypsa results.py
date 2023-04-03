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

sys_costs = []
wind_costs = []
solar_costs = []
batt_costs = []
pgp_costs = []

cases = listdir('/Users/Dominic/Desktop/Oahu Results/(Pypsa) costs using mean nsrdb and wind, 14 year/plotting/')
print(cases)

sys_costs = [0.180665526, 0]
wind_costs = [0.022059533, 0]
solar_costs = [0.1150,0]
batt_costs = [0.0435892369, 0]
pgp_costs = [0,0]


#Prep for plotting    
N = 2
ind = np.arange(N)    # the x locations for the groups
width = 0.7       # the width of the bars: can also be len(x) sequence

data1 = np.array(solar_costs) #pv
data2 = np.array(wind_costs) #wind
data3 = np.array(batt_costs) #batt
data4 = np.array(pgp_costs)

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
p2 = ax1.bar(ind, data2, width, bottom=data1, color=wind_q)
p3 = ax1.bar(ind, data3, width, bottom=data1+data2, color=batt_q)
p4 = ax1.bar(ind, data4, width, bottom=data1+data2+data3, color=pgp_q)


plt.ylabel('System cost ($/kWh)')
plt.xticks(rotation=45, ha='right')

ax = plt.gca() 
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
#plt.grid(True, which = 'major', axis = 'y', c = 'lightgray')

ax.set_ylim(0, 0.4)
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.05))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax.set_title('PYPSA - Oahu Using Means from NSRDB and WIND', y=1.05)

plt.xticks(ind, ('PV, Wind, Li-ion Battery', 'PV, Wind, Li-ion Battery, PGP'))

#xlocs=[0,1]
#for i, v in enumerate(sys_costs):
   #plt.text(xlocs[i] - 0.35, v + 0.01, format(v, '.2f'))

##======================================================================================================
# Save plots as jpg
##======================================================================================================


plt.savefig('Oahu Pypsa pv wind battery.jpg', dpi = 300, bbox_inches='tight')
plt.show()
