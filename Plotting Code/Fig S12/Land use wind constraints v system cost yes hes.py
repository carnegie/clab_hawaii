'''This code will plot land use vs cost of electricity for systems with and without HES as wind capacity is constrained'''

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
yes_hes_0 = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something4 - Decreasing Land Use/Yes PGP/Outputs/dec_land_use_no_normal_yes_PGP_0wind_output.pickle'
yes_hes_25 = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something4 - Decreasing Land Use/Yes PGP/Outputs/dec_land_use_no_normal_yes_PGP_25wind_output.pickle'
yes_hes_50 = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something4 - Decreasing Land Use/Yes PGP/Outputs/dec_land_use_no_normal_yes_PGP_50wind_output.pickle'
yes_hes_75 = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something4 - Decreasing Land Use/Yes PGP/Outputs/dec_land_use_no_normal_yes_PGP_75wind_output.pickle'
yes_hes_100 = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something4 - Decreasing Land Use/Yes PGP/Outputs/dec_land_use_no_normal_yes_PGP_100wind_output.pickle'

#Get land use

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

#Get land use
combo_wind_solar_yes_HES = np.array([])
wind_arr_yes_HES = np.array([])
battery_arr_yes_HES = np.array([])
h2store_arr_yes_HES = np.array([])
fuelcell_arr_yes_HES = np.array([])
electrolyzer_arr_yes_HES = np.array([])


with open(yes_hes_0, 'rb') as f:
    data1 = pickle.load(f)
    component_results = data1['component results']
    capacity = component_results['Optimal Capacity [MW]']
    generator = capacity['Generator']
    solar = generator['solar']
    batt = capacity['StorageUnit']
    battery = batt['battery']
    h2 = capacity['Store']
    h2store = h2['h2_storage']
    cell = capacity['Link']
    fuelcell = cell['fuel_cell']
    electrolyzer = cell['electrolysis']
    wind = 0
     

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
    combo_wind_solar_yes_HES = np.append(combo_wind_solar_yes_HES, solar)
    wind_arr_yes_HES = np.append(wind_arr_yes_HES, wind)
    battery_arr_yes_HES = np.append(battery_arr_yes_HES, battery)
    h2store_arr_yes_HES = np.append(h2store_arr_yes_HES, h2store)
    fuelcell_arr_yes_HES = np.append(fuelcell_arr_yes_HES, fuelcell)
    electrolyzer_arr_yes_HES = np.append(electrolyzer_arr_yes_HES, electrolyzer)
    

yesHES = [yes_hes_25, yes_hes_50, yes_hes_75, yes_hes_100]
for yes_pgp in yesHES:
    with open(yes_pgp, 'rb') as f:
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
        electrolyzer = cell['electrolysis']

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
        combo_wind_solar_yes_HES = np.append(combo_wind_solar_yes_HES, solar)
        wind_arr_yes_HES = np.append(wind_arr_yes_HES, wind)
        battery_arr_yes_HES = np.append(battery_arr_yes_HES, battery)
        h2store_arr_yes_HES = np.append(h2store_arr_yes_HES, h2store)
        fuelcell_arr_yes_HES = np.append(fuelcell_arr_yes_HES, fuelcell)
        electrolyzer_arr_yes_HES = np.append(electrolyzer_arr_yes_HES, electrolyzer)

full_wind_space_yes_HES = np.array([])
full_wind_space_yes_HES = (wind_arr_yes_HES*(0.1809))
print('full wind space needed',full_wind_space_yes_HES)
    #Append the value of sys_land to sys_land_use
    #sys_land_use = np.append(sys_land_use, sys_land)
wind_arr_yes_HES = (wind_arr_yes_HES*(0.1809*0.02))
combo_wind_solar_yes_HES = (combo_wind_solar_yes_HES*0.0223)
battery_arr_yes_HES = (battery_arr_yes_HES*0.0000249)
h2store_arr_yes_HES = (h2store_arr_yes_HES*0.0000267)
electrolyzer_arr_yes_HES = (electrolyzer_arr_yes_HES*0.0000250)
fuelcell_arr_yes_HES = (fuelcell_arr_yes_HES*0.0000198)

total_land_yes_HES = np.array([])
total_land_yes_HES = full_wind_space_yes_HES + combo_wind_solar_yes_HES + battery_arr_yes_HES + h2store_arr_yes_HES + electrolyzer_arr_yes_HES + fuelcell_arr_yes_HES
print('total land yes HES',total_land_yes_HES)

#==============================================================================
#Plot
#==============================================================================

fig, ax = plt.subplots(figsize=(6, 6))
#ax.plot(total_land, sys_costs, 'o', color='black', label='No HES', markersize=10)


#Plot the exponential fit
x = np.array(total_land_yes_HES)
y = np.array(sys_costs_yes_HES)
from scipy.optimize import curve_fit
# Define the function to fit
def exp_func(x, a, b, c):
    return a * (1 + np.exp(-b * x)) + c
# Fit the curve to the function
popt, pcov = curve_fit(exp_func, x, y, p0=[0.148,0.002,0]) #p0 is initial guess. Used wolfram alpha widget to get good inital guess of function values
# Print the parameters of the fitted function
print(f"Parameters: a={popt[0]:.3f}, b={popt[1]:.3f}, c={popt[2]:.3f}")

from sklearn.metrics import r2_score
y_pred = exp_func(x, *popt)
r_squared = r2_score(y, y_pred)
print(f"R-squared: {r_squared:.6f}")

xfit = np.linspace(121, 266, 5000)
yfit = exp_func(xfit, *popt)
ax.plot(xfit, yfit, label=r'$y=0.105*(1+e^{-0.002x}) - 0.001$  |  $R^2 = 0.9979}$', color='magenta') #manually update should inputs change. I couldn't figure out how to use f notation while starting text with Latex

ax.plot(total_land_yes_HES, sys_costs_yes_HES, 'o', color='black',markersize=10)


plt.ylabel('System Cost ($/kWh)',labelpad = 6)

plt.xlabel(r'System Land Use (km$^2$)',labelpad = 6)

ax.yaxis.label.set_fontsize(24)
ax.xaxis.label.set_fontsize(22)

#make x and y axis text fontsize 14
for item in (ax.get_xticklabels() + ax.get_yticklabels()):
    item.set_fontsize(22)
plt.xticks(rotation=45)    

#plt.legend(fontsize=12, loc='upper right')
ax.yaxis.set_major_formatter(FormatStrFormatter('%.3f'))
plt.tick_params(axis='y', which='both', left='on', labelleft='on')
ax.set_title('System Cost vs Land Use', y=1)
ax.title.set_fontsize(26)

plt.savefig('C:\\Users\\Dominic\\desktop\\Oahu Results\\Land use wind constraints v system cost yes hes.png', dpi=300, bbox_inches='tight')
plt.show()
