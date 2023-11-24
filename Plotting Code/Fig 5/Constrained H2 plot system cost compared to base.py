'''
This code will plot the system cost of each scenario using constrained H2 storage values
'''
from __future__ import division
import numpy as np
from os import listdir
import os
import pickle
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.ticker as ticker
from scipy.stats import linregress
import datetime
from matplotlib.dates import drange
from matplotlib.ticker import FormatStrFormatter
import pandas as pd

path0 = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure 4 - Optimized System Capacity/Outputs/oahu_optimized_system_no_normal_w_PGP_output.pickle'
path1 = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure 5 - H2 Storage Constraints/Outputs/eighty_percent_h2_storage_constrained.pickle'
path2 = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure 5 - H2 Storage Constraints/Outputs/sixty_percent_h2_storage_constrained.pickle'
path3 = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure 5 - H2 Storage Constraints/Outputs/fourty_percent_h2_storage_constrained.pickle'
path4 = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure 5 - H2 Storage Constraints/Outputs/twenty_percent_h2_storage_constrained.pickle'
path5 = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure 4 - Optimized System Capacity/Outputs/oahu_optimized_system_no_normal_no_PGP_output.pickle'

sys_costs = []

list1 = [path0, path1, path2, path3, path4, path5]
for path in list1:
    with open(path, 'rb') as f:
        data = pickle.load(f)
        case_results = data['case results']
        spending = case_results['system cost [$/h]']
        sys_costs = np.append(sys_costs, spending)

sys_costs = sys_costs/1000/646.834331165537 #convert to $/kWh
print(sys_costs)

#=============================================================================
#Make stacked bar charts

solar_q = 'orange'
wind_q = 'blue'
h2_storage_q = 'pink'
batt_q = 'purple'
electrolysis_q = 'gray'
fuelcell_q = 'green'

wind_costs = []
solar_costs = []
batt_costs = []
h2_storage_costs = []
electrolyzer_costs = []
fuelcell_costs = []

with open(path5, 'rb') as f:
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

    wind_cost = ((wind / 122712 / 1000) + opex_wind/1000)/646.834331165537
    solar_cost = ((solar / 122712 / 1000))/646.834331165537
    battery_cost = ((battery / 122712 / 1000) + opex_battery/1000)/646.834331165537
    h2_storage_cost = 0
    electrolyzer_cost = 0
    fuelcell_cost = 0

    wind_costs = np.append(wind_costs, wind_cost)
    solar_costs = np.append(solar_costs, solar_cost)
    batt_costs = np.append(batt_costs, battery_cost)
    h2_storage_costs = np.append(h2_storage_costs, h2_storage_cost)
    electrolyzer_costs = np.append(electrolyzer_costs, electrolyzer_cost)
    fuelcell_costs = np.append(fuelcell_costs, fuelcell_cost)

list2 = [path4, path3, path2, path1, path0]
for list in list2:
    with open(list, 'rb') as f:
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

        wind_cost = ((wind / 122712 / 1000) + opex_wind/1000)/646.834331165537
        solar_cost =( solar / 122712 / 1000)/646.834331165537
        battery_cost = ((battery / 122712 / 1000) + opex_battery/1000)/646.834331165537
        h2_storage_cost =( h2store / 122712 / 1000)/646.834331165537
        electrolyzer_cost = ((electrolysis / 122712 / 1000) + opex_electrolysis /1000)/646.834331165537
        fuelcell_cost = ((fuelcell / 122712 / 1000) + opex_fuelcell / 1000)/646.834331165537


        wind_costs = np.append(wind_costs, wind_cost)
        solar_costs = np.append(solar_costs, solar_cost)
        batt_costs = np.append(batt_costs, battery_cost)
        h2_storage_costs = np.append(h2_storage_costs, h2_storage_cost)
        electrolyzer_costs = np.append(electrolyzer_costs, electrolyzer_cost)
        fuelcell_costs = np.append(fuelcell_costs, fuelcell_cost)
        
        print('wind',wind_costs)
        print('solar',solar_costs)
        print('battery',batt_costs)
        print('h2 storage', h2_storage_costs)
        print('electrolyzer', electrolyzer_costs)
        print('fuelcell', fuelcell_costs,'\n')
        print('total', wind_costs+solar_costs+batt_costs+h2_storage_costs+electrolyzer_costs+fuelcell_costs)

#=============================================================================

#Plot the values
x = [0, 20, 40, 60, 80, 100]
y = [sys_costs[5], sys_costs[4], sys_costs[3], sys_costs[2], sys_costs[1], sys_costs[0]]
print(y)

fig = plt.figure(figsize=(10,10))
ax = plt.subplot2grid((1,1), (0, 0), colspan=1, rowspan=1)
fig, ax = plt.subplots(figsize=(6, 7)) #make square
ax.plot(x, y, 'o',color='black', markeredgecolor='black', markersize=11)

#Plot stacked bars
data1 = np.array(solar_costs) #pv
data2 = np.array(wind_costs) #wind
data3 = np.array(batt_costs) #batt
data4 = np.array(h2_storage_costs) #h2 storage
data5 = np.array(electrolyzer_costs) #electrolyzer
data6 = np.array(fuelcell_costs) #fuelcell

width = 12
p1 = ax.bar([0,20,40,60,80,100], data1, width, color=solar_q)
p2 = ax.bar([0,20,40,60,80,100], data2, width, bottom=data1, color=wind_q)
p3 = ax.bar([0,20,40,60,80,100], data3, width, bottom=data1+data2, color=batt_q)
p4 = ax.bar([0,20,40,60,80,100], data4, width, bottom=data1+data2+data3, color=h2_storage_q)
p5 = ax.bar([0,20,40,60,80,100], data5, width, bottom=data1+data2+data3+data4, color=h2_storage_q, hatch='//')
p6 = ax.bar([0,20,40,60,80,100], data6, width, bottom=data1+data2+data3+data4+data5, color=h2_storage_q, hatch='\\\\')

legend = plt.legend(reversed([p1, p2, p3, p4, p5, p6]), reversed(y), loc="best", bbox_to_anchor=(1, 0.6), fontsize='16', edgecolor='black')

for handle in legend.legendHandles:
    handle.set_edgecolor('black')

for bar in p1 + p2 + p3 + p4 + p5 + p6:
    bar.set_linewidth(1)
    bar.set_edgecolor('black')
    


#Plot the exponential fit
x = np.array(x)
y = np.array(y)
from scipy.optimize import curve_fit
# Define the function to fit
def exp_func(x, a, b, c):
    return a * (1 + np.exp(-b * x)) + c
# Fit the curve to the function
popt, pcov = curve_fit(exp_func, x, y, p0=[0.148,0.311,0]) #p0 is initial guess. Used wolfram alpha widget to get good inital guess of function values
# Print the parameters of the fitted function
print(f"Parameters: a={popt[0]:.3f}, b={popt[1]:.3f}, c={popt[2]:.3f}")

from sklearn.metrics import r2_score
y_pred = exp_func(x, *popt)
r_squared = r2_score(y, y_pred)
print(f"R-squared: {r_squared:.6f}")

xfit = np.linspace(0, 100, 5000)
yfit = exp_func(xfit, *popt)
ax.plot(xfit, yfit, label=r'$y=0.078*(1+e^{-0.049x}) + 0.089$  |  $R^2 = 0.9996}$', color='black') #manually update should inputs change. I couldn't figure out how to use f notation while starting text with Latex
ax.plot

ax.set_xlabel('Percent of H$_2$ Storage\nCompared to Maximum Case', fontsize=14)
ax.set_ylabel('System Cost ($/kWh)', fontsize=14)
ax.set_title('System Cost As Hydrogen\nStorage Capacity is Expanded', fontsize=16, pad = 30)
ax.set_ylim(0,0.25)
ax.set_xlim(-6, 107)
ax.set_xticks([0, 20, 40, 60, 80, 100])
ax.set_xticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
ax.set_xticklabels(ax.get_xticklabels(), rotation=-45, ha='left')
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the color of the spines
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Set the linewidth of the spines
ax.spines['left'].set_linewidth(1)
ax.spines['bottom'].set_linewidth(1)

#make x and y axis text fontsize 14
for item in ([ax.xaxis.label] + ax.get_xticklabels() + ax.get_yticklabels()):
    item.set_fontsize(24)
    
plt.xticks(rotation=45, ha='center')
    
    
ax.yaxis.label.set_fontsize(26)

ax.title.set_fontsize(30)

plt.legend(fontsize=12, loc='upper right')
ax.get_legend().remove()
plt.savefig('C:\\Users\\Dominic\\desktop\\Oahu Results\\Costs with constrained H2 storage.png', dpi=300, bbox_inches='tight')
plt.show()
