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

##==========================================
# System Cost Calculations
##==========================================

def get_cost_contributions(base):
    input_tech = base[0][1] # list of dictionaries
    results_case = base[1][0]
    results_tech = base[1][1]
    results_time = base[1][2]
    
    # Nameplate costs
    try:
        dicw = next((sub for sub in input_tech if sub['tech_name'] == 'node_1_wind1'), None)
        wind_t = ((np.multiply(dicw["fixed_cost"], results_tech["node_1_wind1 capacity"])))
    except:
        wind_t = 0
    
    try:
        dics = next((sub for sub in input_tech if sub['tech_name'] == 'node_1_solar1'), None)
        solar_t = ((np.multiply(dics["fixed_cost"], results_tech["node_1_solar1 capacity"])))
    except:
        solar_t = 0
    
    try:
        dicb = next((sub for sub in input_tech if sub['tech_name'] == 'li_ion_battery_storage'), None)
        batt_t = (np.multiply(dicb["fixed_cost"], results_tech["li_ion_battery_storage capacity"]))
    except:
        batt_t = 0
        
    try:
        dic4 = next((sub for sub in input_tech if sub['tech_name'] == 'to_PGP'), None)
        dic5 = next((sub for sub in input_tech if sub['tech_name'] == 'PGP_storage'), None)
        dic6 = next((sub for sub in input_tech if sub['tech_name'] == 'from_PGP'), None)
        pgp_t = ((np.multiply(dic4["fixed_cost"], results_tech["to_PGP capacity"])) +
                 (np.multiply(dic5["fixed_cost"], results_tech["PGP_storage capacity"])) +
                 (np.multiply(dic6["fixed_cost"], results_tech["from_PGP capacity"])))
    except:
        pgp_t = 0 

    calc_sys_cost = wind_t + solar_t + batt_t + pgp_t

    return wind_t, solar_t , batt_t, pgp_t

#====================================================================
# Read data from each pickle file
##===================================================================

sys_costs = []
wind_costs = []
solar_costs = []
batt_costs = []
pgp_costs = []

cases = listdir('/Users/Dominic/Desktop/MEM-master/Output_Data/plotting/')
print(cases)

for case in cases:
    pickle_in = open('/Users/Dominic/Desktop/MEM-master/Output_Data/plotting/' + case, 'rb')
    base = pickle.load(pickle_in)
    results_case = base[1][0]
    sys_costs.append(results_case['system_cost'])
    wind_c, solar_c, batt_c, pgp_c = get_cost_contributions(base)
    wind_costs.append(wind_c)
    solar_costs.append(solar_c)
    batt_costs.append(batt_c)
    pgp_costs.append(pgp_c)
    
print(wind_costs)

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
ax.set_title('MEM - Oahu Using Means from NSRDB and WIND', y=1.05)

plt.xticks(ind, ('PV, Wind, Li-ion Battery', 'PV, Wind, Li-ion Battery, PGP'))

#xlocs=[0,1]
#for i, v in enumerate(sys_costs):
   #plt.text(xlocs[i] - 0.35, v + 0.01, format(v, '.2f'))

##======================================================================================================
# Save plots as jpg
##======================================================================================================


plt.savefig('Oahu MEM pv wind battery.jpg', dpi = 300, bbox_inches='tight')
plt.show()
