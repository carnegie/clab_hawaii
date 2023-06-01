'''
This code will plot the system cost of each scenario using increasing H2 storage cost
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

path0 = 'C:\\Users\\Dominic\\desktop\\fourteen_year_above_storage_jackie_price_yes_normal_all_mw_e6.pickle'
path1 = 'C:\\Users\\Dominic\\desktop\\run one increasing h2 storage cost yes normal.pickle'
path2 = 'C:\\Users\\Dominic\\desktop\\run two increasing h2 storage cost yes normal.pickle'
path3 = 'C:\\Users\\Dominic\\desktop\\run three increasing h2 storage cost yes normal.pickle'
path4 = 'C:\\Users\\Dominic\\desktop\\run four increasing h2 storage cost yes normal.pickle'
path5 = 'C:\\Users\\Dominic\\desktop\\run five increasing h2 storage cost yes normal.pickle'

sys_costs = []
wind_costs = []
solar_costs = []
batt_costs = []
pgp_costs = []

list1 = [path0, path1, path2, path3, path4, path5]
for path in list1:
    with open(path, 'rb') as f:
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
      #print(path)

#print(wind_costs)
#print(solar_costs)
#print(batt_costs)
#print(pgp_costs)

#Add the costs together to system cost
for i in range(len(wind_costs)):
    sys_costs.append(wind_costs[i] + solar_costs[i] + batt_costs[i] + pgp_costs[i])

print(sys_costs)

#Plot the values
x = [0.140060273, 0.240060273, 0.340060273, 0.440060273, 0.540060273, 0.640060273]
y = [sys_costs[0], sys_costs[1], sys_costs[2], sys_costs[3], sys_costs[4], sys_costs[5]]


fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)
fig, ax = plt.subplots(figsize=(6, 6)) #make square
ax.plot(x, y, 'o',color='blue', label='Data')


#Plot the exponential fit
x = np.array(x)
y = np.array(y)
from scipy.optimize import curve_fit
# Define the function to fit
def exp_func(x, a, b, c):
    return a * (1 - np.exp(-b * x)) + c
# Fit the curve to the function
popt, pcov = curve_fit(exp_func, x, y, p0=[0.148,0.311,0]) #p0 is initial guess. Used wolfram alpha widget to get good inital guess of function values
# Print the parameters of the fitted function
print(f"Parameters: a={popt[0]:.3f}, b={popt[1]:.3f}, c={popt[2]:.3f}")

from sklearn.metrics import r2_score
y_pred = exp_func(x, *popt)
r_squared = r2_score(y, y_pred)
print(f"R-squared: {r_squared:.6f}")


xfit = np.linspace(0, 4, 1000)
yfit = exp_func(xfit, *popt)
ax.plot(xfit, yfit, label=r'$y=0.063*(1-e^{-5.350x}) + 0.116$  |  $R^2 = 0.998$', color='black')

ax.set_xlabel('Cost of H2 Storage ($/kW/hour)', fontsize=14)
ax.set_ylabel('System Cost \n Compared to Base Case', fontsize=14)
ax.set_title('Optimal System Cost Compared\nto Case Using Costs from Hunter et al.', fontsize=16, pad = 10)
ax.set_ylim(0.14,0.19)
ax.set_xlim(0.13, 0.65)
ax.set_xticks([0.140060273, 0.240060273, 0.340060273, 0.440060273, 0.540060273, 0.640060273])
ax.set_xticklabels(['0.14', '0.24', '0.34', '0.44', '0.54', '0.64']) #Shortened values to 2 decimals
ax.tick_params(axis='both', which='major', labelsize=14)

plt.legend(fontsize=12)
plt.savefig('C:\\Users\\Dominic\\desktop\\Oahu Results\\Costs with increasing H2 storage cost.png', dpi=300, bbox_inches='tight')
plt.show()