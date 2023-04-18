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

no_pgp = '/Users/Dominic/Desktop/fourteen_year_system_costs/fourteen_year_yes_normal_no_pgp.pickle'
pgp_above = '/Users/Dominic/Desktop/fourteen_year_system_costs/fourteen_year_above_storage_yes_normal_all_mw_e6.pickle'
pgp_under = '/Users/Dominic/Desktop/fourteen_year_system_costs/fourteen_year_yes_normal_below_H2.pickle'

with open(no_pgp, 'rb') as f:
      data = pickle.load(f)
      component_results = data['component results']
      #print(component_results)
      spending = component_results['Capital Expenditure']
      #print(spending)
      gen = spending['Generator']
      #print(gen)
      wind = gen['onwind']
      #print(wind)
      solar = gen['solar']
      #print(solar)
      batt = spending['StorageUnit']
      #print(batt)
      battery = batt['battery']

      wind_cost = wind / (122710*1000)
      solar_cost = solar / (122710*1000)
      battery_cost = battery / (122710*1000)

      wind_costs.append(wind_cost)
      solar_costs.append(solar_cost)
      batt_costs.append(battery_cost)
      pgp_costs.append(0.0)
with open(pgp_above, 'rb') as f:
      data1 = pickle.load(f)
      component_results = data1['component results']
      #print(component_results)
      spending = component_results['Capital Expenditure']
      #print(spending)
      gen = spending['Generator']
      #print(gen)
      wind = gen['onwind']
      #print(wind)
      solar = gen['solar']
      #print(solar)
      batt = spending['StorageUnit']
      #print(batt)
      battery = batt['battery']
      #print(battery)
      h2 = spending['Store']
      #print(h2)
      h2store = h2['h2_storage']
      #print(h2store)
      cell = spending['Link']
      #print(cell)
      fuelcell = cell['fuel_cell']
      #print(fuelcell)
      electrolysis = cell['electrolysis']

      wind_cost = wind / (122710*1000)
      solar_cost = solar / (122710*1000)
      battery_cost = battery / (122710*1000)
      pgp_price = ((h2store/(122710*1000)) + (fuelcell/(122710*1000)) + (electrolysis/(122710*1000)))
      
      wind_costs.append(wind_cost)
      solar_costs.append(solar_cost)
      batt_costs.append(battery_cost)
      pgp_costs.append(pgp_price)


with open(pgp_under, 'rb') as f:
      data2 = pickle.load(f)
      component_results = data2['component results']
      #print(component_results)
      spending = component_results['Capital Expenditure']
      #print(spending)
      gen = spending['Generator']
      #print(gen)
      wind = gen['onwind']
      #print(wind)
      solar = gen['solar']
      #print(solar)
      batt = spending['StorageUnit']
      #print(batt)
      battery = batt['battery']
      #print(battery)
      h2 = spending['Store']
      #print(h2)
      h2store = h2['h2_storage']
      #print(h2store)
      cell = spending['Link']
      #print(cell)
      fuelcell = cell['fuel_cell']
      #print(fuelcell)
      electrolysis = cell['electrolysis']    

      wind_cost = wind / (122710*1000)
      solar_cost = solar / (122710*1000)
      battery_cost = battery / (122710*1000)
      pgp_price = ((h2store/(122710*1000)) + (fuelcell/(122710*1000)) + (electrolysis/(122710*1000)))
      
      wind_costs.append(wind_cost)
      solar_costs.append(solar_cost)
      batt_costs.append(battery_cost)
      pgp_costs.append(pgp_price)
      
print(wind_costs)
print(solar_costs)
print(batt_costs)
print(pgp_costs)

#Prep for plotting    
N = 3
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


plt.ylabel('System Cost ($/kWh)')
plt.xticks(rotation=45, ha='right')

ax = plt.gca() 
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
#plt.grid(True, which = 'major', axis = 'y', c = 'lightgray')

ax.set_ylim(0, 0.2)
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.04))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax.set_title('Oahu Optimized Renewable System Cost', y=1.05)

#plt.xticks(ind, ('PV, Wind, Li-ion Battery', 'PV, Wind, Li-ion Battery, PGP (Above Ground Storage)', 'PV, Wind, Li-ion Battery, PGP (Below Ground Storage)'))
plt.xticks(ind, ('No PGP', 'PGP (Aboveground Storage)', 'PGP (Underground Storage)'))
y = ['Solar', 'Wind', 'Battery', 'PGP']
ax1.legend(y, loc="upper right")

#xlocs=[0,1]
#for i, v in enumerate(sys_costs):
   #plt.text(xlocs[i] - 0.35, v + 0.01, format(v, '.2f'))

##======================================================================================================
# Save plots as jpg
##======================================================================================================


plt.savefig('Oahu Optimized Renewable System Cost.jpg', dpi = 300, bbox_inches='tight')
plt.show()
