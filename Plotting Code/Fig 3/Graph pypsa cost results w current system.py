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
h2_storage_q = 'pink'
batt_q = 'purple'
electrolysis_q = 'gray'
fuelcell_q = 'green'

sys_costs = []
wind_costs = []
solar_costs = []
batt_costs = []
h2_storage_costs = []
electrolyzer_costs = []
fuelcell_costs = []


no_pgp = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure 3 - Optimized system cost/Outputs/oahu_optimized_system_yes_normal_no_PGP_output.pickle'
pgp_above = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure 3 - Optimized system cost/Outputs/oahu_optimized_system_yes_normal_w_PGP_output.pickle'

#Add system components to the cost lists
with open(no_pgp, 'rb') as f:
    data = pickle.load(f)
    component_results = data['component results']
    spending = component_results['Capital Expenditure [$]']
    gen = spending['Generator']
    wind = gen['wind']
    solar = gen['solar']
    batt = spending['StorageUnit']
    battery = batt['battery']
    opex = component_results['Operational Expenditure [$]']
    opex_generator = opex['Generator']
    opex_wind = opex_generator['wind']
    opex_storage_unit = opex['StorageUnit']
    opex_battery = opex_storage_unit['battery']

    wind_cost = (wind / 122712 / 1000) + opex_wind/1000
    solar_cost = (solar / 122712 / 1000)
    battery_cost = (battery / 122712 / 1000) + opex_battery/1000
    h2_storage_cost = 0
    electrolyzer_cost = 0
    fuelcell_cost = 0

    wind_costs = np.append(wind_costs, wind_cost)
    solar_costs = np.append(solar_costs, solar_cost)
    batt_costs = np.append(batt_costs, battery_cost)
    h2_storage_costs = np.append(h2_storage_costs, h2_storage_cost)
    electrolyzer_costs = np.append(electrolyzer_costs, electrolyzer_cost)
    fuelcell_costs = np.append(fuelcell_costs, fuelcell_cost)
    
    
with open(pgp_above, 'rb') as f:
    data = pickle.load(f)
    component_results = data['component results']
    spending = component_results['Capital Expenditure [$]']
    gen = spending['Generator']
    wind = gen['wind']
    solar = gen['solar']
    batt = spending['StorageUnit']
    battery = batt['battery']
    h2 = spending['Store']
    h2store = h2['h2_storage']
    cell = spending['Link']
    fuelcell = cell['fuel_cell']
    electrolysis = cell['electrolysis']
    opex = component_results['Operational Expenditure [$]']
    opex_link = opex['Link']
    opex_electrolysis = opex_link['electrolysis']
    opex_fuelcell = opex_link['fuel_cell']
    opex_generator = opex['Generator']
    opex_wind = opex_generator['wind']
    opex_storage_unit = opex['StorageUnit']
    opex_battery = opex_storage_unit['battery']

    wind_cost = (wind / 122712 / 1000) + opex_wind/1000
    solar_cost = solar / 122712 / 1000
    battery_cost = (battery / 122712 / 1000) + opex_battery/1000
    h2_storage_cost = h2store / 122712 / 1000
    electrolyzer_cost = (electrolysis / 122712 / 1000) + opex_electrolysis /1000
    fuelcell_cost = (fuelcell / 122712 / 1000) + opex_fuelcell / 1000


    wind_costs = np.append(wind_costs, wind_cost)
    solar_costs = np.append(solar_costs, solar_cost)
    batt_costs = np.append(batt_costs, battery_cost)
    h2_storage_costs = np.append(h2_storage_costs, h2_storage_cost)
    electrolyzer_costs = np.append(electrolyzer_costs, electrolyzer_cost)
    fuelcell_costs = np.append(fuelcell_costs, fuelcell_cost)

#Add zero to the first index point of the cost lists
wind_costs = np.insert(wind_costs, 0, 0)
solar_costs = np.insert(solar_costs, 0, 0)
batt_costs = np.insert(batt_costs, 0, 0)
h2_storage_costs = np.insert(h2_storage_costs, 0, 0)
electrolyzer_costs = np.insert(electrolyzer_costs, 0, 0)
fuelcell_costs = np.insert(fuelcell_costs, 0, 0)

#Add current system data
current_cost = [0.24572+0.001836+0.002792+0.001159,0,0]
current_cost = np.array(current_cost)
    

print('wind',wind_costs)
print('solar',solar_costs)
print('battery',batt_costs)
print('h2 storage', h2_storage_costs)
print('electrolyzer', electrolyzer_costs)
print('fuelcell', fuelcell_costs,'\n')
print('current system', current_cost,'\n')
print('total cost no HES',wind_costs[1]+solar_costs[1]+batt_costs[1]+h2_storage_costs[1]+electrolyzer_costs[1]+fuelcell_costs[1])
print('total cost yes HES', wind_costs[2]+solar_costs[2]+batt_costs[2]+h2_storage_costs[2]+electrolyzer_costs[2]+fuelcell_costs[2])
#Prep for plotting    
N = 3
ind = np.arange(N)    # the x locations for the groups
width = 0.7       # the width of the bars: can also be len(x) sequence

data1 = np.array(solar_costs) #pv
data2 = np.array(wind_costs) #wind
data3 = np.array(batt_costs) #batt
data4 = np.array(h2_storage_costs) #h2 storage
data5 = np.array(electrolyzer_costs) #electrolyzer
data6 = np.array(fuelcell_costs) #fuelcell

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
ax1 = plt.subplot2grid((1,1), (0, 0), colspan=1, rowspan=1)
p0 = ax1.bar(ind, current_cost, width, color='gray')
p1 = ax1.bar(ind, data1, width, color=solar_q)
p2 = ax1.bar(ind, data2, width, bottom=data1, color=wind_q)
p3 = ax1.bar(ind, data3, width, bottom=data1+data2, color=batt_q)
p4 = ax1.bar(ind, data4, width, bottom=data1+data2+data3, color=h2_storage_q)
p5 = ax1.bar(ind, data5, width, bottom=data1+data2+data3+data4, color=h2_storage_q, hatch='//')
p6 = ax1.bar(ind, data6, width, bottom=data1+data2+data3+data4+data5, color=h2_storage_q, hatch='\\\\')


plt.ylabel('System Cost ($/kWh)')
plt.xticks(rotation=0, ha='center')

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

ax.set_ylim(0, 0.26)
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.05))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
plt.tick_params(axis='y', which='major', left='on', labelleft='on')
ax.set_title('Oahu Renewable\nSystem Cost', y=1.01)


#make x and y axis text fontsize 14
for item in ([ax.xaxis.label] + ax.get_xticklabels() + ax.get_yticklabels()):
    item.set_fontsize(24)
    
for item in ([ax.xaxis.label] + ax.get_xticklabels()):    
    item.set_rotation(45)
    
    
ax.yaxis.label.set_fontsize(26)

ax.title.set_fontsize(30)


#plt.xticks(ind, ('PV, Wind, Li-ion Battery', 'PV, Wind, Li-ion Battery, PGP (Above Ground Storage)', 'PV, Wind, Li-ion Battery, PGP (Below Ground Storage)'))
plt.xticks(ind, ('Current\nSystem', 'Modeled\nWithout HES', 'Modeled\nWith HES'))
y = ['Current System', 'Solar', 'Wind', 'Battery', 'H2 Storage', 'Electrolyzer', 'Fuel Cell']
legend = plt.legend(reversed([p0, p1, p2, p3, p4, p5, p6]), reversed(y), loc="best", bbox_to_anchor=(1, 0.7), fontsize='24', edgecolor='black')

for handle in legend.legendHandles:
    handle.set_edgecolor('black')

for bar in p0 + p1 + p2 + p3 + p4 + p5 + p6:
    bar.set_linewidth(1)
    bar.set_edgecolor('black')


plt.savefig('C:\\Users\\Dominic\\desktop\\Oahu Results\\Oahu Optimized Renewable System Cost.jpg', dpi = 300, bbox_inches='tight')
plt.show()
