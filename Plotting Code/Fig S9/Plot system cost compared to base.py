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

path0 = '/Users/covel/OneDrive/Desktop/13-6-23 Rerun/Figure S7 - Sensitivity Analysis/Outputs/run_one_increasing_h2_storage_cost_yes_normal_output.pickle'
path1 = '/Users/covel/OneDrive/Desktop/13-6-23 Rerun/Figure S7 - Sensitivity Analysis/Outputs/run_two_increasing_h2_storage_cost_yes_normal_output.pickle'
path2 = '/Users/covel/OneDrive/Desktop/13-6-23 Rerun/Figure S7 - Sensitivity Analysis/Outputs/run_three_increasing_h2_storage_cost_yes_normal_output.pickle'
path3 = '/Users/covel/OneDrive/Desktop/13-6-23 Rerun/Figure S7 - Sensitivity Analysis/Outputs/run_four_increasing_h2_storage_cost_yes_normal_output.pickle'
path4 = '/Users/covel/OneDrive/Desktop/13-6-23 Rerun/Figure S7 - Sensitivity Analysis/Outputs/run_five_increasing_h2_storage_cost_yes_normal_output.pickle'
path5 = '/Users/covel/OneDrive/Desktop/13-6-23 Rerun/Figure S7 - Sensitivity Analysis/Outputs/run_six_increasing_h2_storage_cost_yes_normal_output.pickle'
path6 = '/Users/covel/OneDrive/Desktop/13-6-23 Rerun/Figure S7 - Sensitivity Analysis/Outputs/run_seven_increasing_h2_storage_cost_yes_normal_output.pickle'
path7 = '/Users/covel/OneDrive/Desktop/13-6-23 Rerun/Figure S7 - Sensitivity Analysis/Outputs/run_eight_increasing_h2_storage_cost_yes_normal_output.pickle'

sys_costs = []

list1 = [path0, path1, path2, path3, path4, path5, path6, path7]
for path in list1:
    with open(path, 'rb') as f:
        data = pickle.load(f)
        case_results = data['case results']
        spending = case_results['system cost [$/h]']
        sys_costs = np.append(sys_costs, spending)

sys_costs = sys_costs/1000

#Plot the values
x = [0.132497018, 0.232497018, 0.332497018, 0.432497018, 0.532497018, 0.632497018, 0.732497018, 0.832497018]
y = [sys_costs[0], sys_costs[1], sys_costs[2], sys_costs[3], sys_costs[4], sys_costs[5], sys_costs[6], sys_costs[7]]
print(y)

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)
fig, ax = plt.subplots(figsize=(6, 6)) #make square
ax.plot(x, y, 'o',color='blue', markeredgecolor='black', markersize=11)


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
ax.plot(xfit, yfit, label=r'$y=0.069*(1-e^{-2.009x}) + 0.151$  |  $R^2 = 0.998}$', color='black') #manually update should inputs change. I couldn't figure out how to use f notation while starting text with Latex

ax.set_xlabel('Cost of H$_2$ Storage (\$/kWh/hour)', fontsize=20)
ax.set_ylabel('System Cost ($/kWh)', fontsize=22)
#ax.set_title('Optimal System Cost vs\nHydrogen Storage Cost', fontsize=24, pad = 12)
ax.set_ylim(0.16,0.22)
ax.set_xlim(0.13, 0.85)
ax.set_xticks([0.132497018, 0.232497018, 0.332497018, 0.432497018, 0.532497018, 0.632497018, 0.732497018, 0.832497018])
ax.set_xticklabels(['0.1325', '0.2325', '0.3325', '0.4325', '0.5325', '0.6325', '0.7325', '0.8325']) #Shortened values to 4 decimals
ax.set_xticklabels(ax.get_xticklabels(), rotation=-45, ha='left')
ax.tick_params(axis='both', which='major', labelsize=20)


#plt.legend(fontsize=12, loc='upper right')
plt.savefig('C:\\Users\\covel\\OneDrive\\desktop\\Oahu Results\\Costs with increasing H2 storage cost.png', dpi=300, bbox_inches='tight')
plt.show()