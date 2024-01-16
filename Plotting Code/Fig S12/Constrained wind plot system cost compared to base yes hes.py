'''This code will plot the cost of electricity for systems with decreasing land use as a result of less wind being built'''

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
no_hes_0 = '/Users/covel/OneDrive/Desktop/13-6-23 Rerun/Figure S Something4 - Decreasing Land Use/No PGP/Outputs/dec_land_use_no_normal_no_PGP_0wind_output.pickle'
no_hes_25 = '/Users/covel/OneDrive/Desktop/13-6-23 Rerun/Figure S Something4 - Decreasing Land Use/No PGP/Outputs/dec_land_use_no_normal_no_PGP_25wind_output.pickle'
no_hes_50 = '/Users/covel/OneDrive/Desktop/13-6-23 Rerun/Figure S Something4 - Decreasing Land Use/No PGP/Outputs/dec_land_use_no_normal_no_PGP_50wind_output.pickle'
no_hes_75 = '/Users/covel/OneDrive/Desktop/13-6-23 Rerun/Figure S Something4 - Decreasing Land Use/No PGP/Outputs/dec_land_use_no_normal_no_PGP_75wind_output.pickle'
no_hes_100 = '/Users/covel/OneDrive/Desktop/13-6-23 Rerun/Figure S Something4 - Decreasing Land Use/No PGP/Outputs/dec_land_use_no_normal_no_PGP_100wind_output.pickle'

yes_hes_0 = '/Users/covel/OneDrive/Desktop/13-6-23 Rerun/Figure S Something4 - Decreasing Land Use/Yes PGP/Outputs/dec_land_use_no_normal_yes_PGP_0wind_output.pickle'
yes_hes_25 = '/Users/covel/OneDrive/Desktop/13-6-23 Rerun/Figure S Something4 - Decreasing Land Use/Yes PGP/Outputs/dec_land_use_no_normal_yes_PGP_25wind_output.pickle'
yes_hes_50 = '/Users/covel/OneDrive/Desktop/13-6-23 Rerun/Figure S Something4 - Decreasing Land Use/Yes PGP/Outputs/dec_land_use_no_normal_yes_PGP_50wind_output.pickle'
yes_hes_75 = '/Users/covel/OneDrive/Desktop/13-6-23 Rerun/Figure S Something4 - Decreasing Land Use/Yes PGP/Outputs/dec_land_use_no_normal_yes_PGP_75wind_output.pickle'
yes_hes_100 = '/Users/covel/OneDrive/Desktop/13-6-23 Rerun/Figure S Something4 - Decreasing Land Use/Yes PGP/Outputs/dec_land_use_no_normal_yes_PGP_100wind_output.pickle'


#Get costs
sys_costs_yes_HES = []
list2 = [yes_hes_0, yes_hes_25, yes_hes_50, yes_hes_75, yes_hes_100]
for path in list2:
    with open(path, 'rb') as f:
        data = pickle.load(f)
        case_results = data['case results']
        spending = case_results['system cost [$/h]']
        sys_costs_yes_HES = np.append(sys_costs_yes_HES, spending)

sys_costs_yes_HES = sys_costs_yes_HES/1000/646.834331165537 #convert to $/kWh
print(sys_costs_yes_HES)

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

with open(yes_hes_0, 'rb') as f:
    data = pickle.load(f)
    component_results = data['component results']
    spending = component_results['Capital Expenditure [$]']
    gen = spending['Generator']
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
    opex_storage_unit = opex['StorageUnit']
    opex_battery = opex_storage_unit['battery']

    wind_cost = 0
    solar_cost = ((solar / 122712 / 1000))/646.834331165537
    battery_cost = ((battery / 122712 / 1000) + opex_battery/1000)/646.834331165537
    h2_storage_cost = ((h2store / 122712 / 1000))/646.834331165537
    electrolyzer_cost = ((electrolysis / 122712 / 1000) + opex_electrolysis/1000)/646.834331165537
    fuelcell_cost = ((fuelcell / 122712 / 1000) + opex_fuelcell/1000)/646.834331165537

    wind_costs = np.append(wind_costs, wind_cost)
    solar_costs = np.append(solar_costs, solar_cost)
    batt_costs = np.append(batt_costs, battery_cost)
    h2_storage_costs = np.append(h2_storage_costs, h2_storage_cost)
    electrolyzer_costs = np.append(electrolyzer_costs, electrolyzer_cost)
    fuelcell_costs = np.append(fuelcell_costs, fuelcell_cost)
    
list3 = [yes_hes_25, yes_hes_50, yes_hes_75, yes_hes_100]
for list in list3:
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
        solar_cost = ((solar / 122712 / 1000))/646.834331165537
        battery_cost = ((battery / 122712 / 1000) + opex_battery/1000)/646.834331165537
        h2_storage_cost = ((h2store / 122712 / 1000))/646.834331165537
        electrolyzer_cost = ((electrolysis / 122712 / 1000) + opex_electrolysis/1000)/646.834331165537
        fuelcell_cost = ((fuelcell / 122712 / 1000) + opex_fuelcell/1000)/646.834331165537

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

#Plot the values
x = [0, 25,50,75,100]
y = [sys_costs_yes_HES[0], sys_costs_yes_HES[1], sys_costs_yes_HES[2], sys_costs_yes_HES[3], sys_costs_yes_HES[4]]
print(y)

fig = plt.figure(figsize=(10,10))
ax = plt.subplot2grid((1,1), (0, 0), colspan=1, rowspan=1)
fig, ax = plt.subplots(figsize=(6, 7)) #make square
#ax.plot(x, y, 'o',color='black', markeredgecolor='black', markersize=11)

#Plot stacked bars
data1 = np.array(solar_costs) #pv
data2 = np.array(wind_costs) #wind
data3 = np.array(batt_costs) #batt
data4 = np.array(h2_storage_costs) #h2 storage
data5 = np.array(electrolyzer_costs) #electrolyzer
data6 = np.array(fuelcell_costs) #fuelcell

width = 12
p1 = ax.bar([0, 25,50,75,100], data1, width, color=solar_q)
p2 = ax.bar([0, 25,50,75,100], data2, width, bottom=data1, color=wind_q)
p3 = ax.bar([0, 25,50,75,100], data3, width, bottom=data1+data2, color=batt_q)
p4 = ax.bar([0, 25,50,75,100], data4, width, bottom=data1+data2+data3, color=h2_storage_q)
p5 = ax.bar([0, 25,50,75,100], data5, width, bottom=data1+data2+data3+data4, color=h2_storage_q, hatch='//')
p6 = ax.bar([0, 25,50,75,100], data6, width, bottom=data1+data2+data3+data4+data5, color=h2_storage_q, hatch='\\\\')

'''   
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
ax.plot(xfit, yfit, label=r'$y=0.134*(1+e^{-0.007x}) + 0.047$  |  $R^2 = 0.9989}$', color='black') #manually update should inputs change. I couldn't figure out how to use f notation while starting text with Latex
ax.plot
'''

ax.set_xlabel('Percent of Wind Capacity\nCompared to Base Case', fontsize=22)
ax.set_ylabel('System Cost ($/kWh)', fontsize=24)
#ax.set_title('System Cost vs\nWind Capacity', fontsize=26, pad = 12)
ax.set_ylim(0,0.35)
ax.set_xlim(-10, 110)
ax.set_xticks([0, 25, 50, 75, 100])
ax.set_xticklabels(['0%', '25%', '50%', '75%', '100%'])
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
ax.tick_params(axis='both', which='major', labelsize=22)

# Set the color of the spines
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Set the linewidth of the spines
ax.spines['left'].set_linewidth(1)
ax.spines['bottom'].set_linewidth(1)

y = ['Solar', 'Wind', 'Battery', 'H$_2$ Storage', 'Electrolyzer', 'Fuel Cell']
#y = ['Solar', 'Wind', 'Battery']
legend = plt.legend(reversed([p1, p2, p3, p4, p5, p6]), reversed(y), loc="best", bbox_to_anchor=(1, 0.7), fontsize='22', edgecolor='black')


for handle in legend.legendHandles:
    handle.set_edgecolor('black')

for bar in p1 + p2 + p3 + p4 + p5 + p6:
    bar.set_linewidth(1)
    bar.set_edgecolor('black')

plt.savefig('C:\\Users\\covel\\OneDrive\\desktop\\Oahu Results\\Costs with constrained wind generation yes hes.png', dpi=300, bbox_inches='tight')
plt.show()
