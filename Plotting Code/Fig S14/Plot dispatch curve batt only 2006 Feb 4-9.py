'''This code will plot the dispatch curves over a period of drought for both the battery only and battery + HES cases.'''

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
import matplotlib.patches as patches


#Input Paths
no_pgp = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure 4 - Optimized System Capacity/Outputs/oahu_optimized_system_no_normal_no_PGP_output.pickle'
pgp_above = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure 4 - Optimized System Capacity/Outputs/oahu_optimized_system_no_normal_w_PGP_output.pickle'

solar_q = 'orange'
wind_q = 'blue'
pgp_q = 'pink'
batt_q = 'purple'

with open(no_pgp, 'rb') as f:
    data1 = pickle.load(f)
    time_results = data1['time results']
    battery_dispatch = time_results['battery discharged']
    battery_dispatch = battery_dispatch[815:959]
    battery_charged = time_results['battery charged']
    battery_charged = battery_charged[815:959]
    demand = time_results['load load']
    demand = demand[815:959]
    solar = time_results['solar dispatch']
    solar = solar[815:959]
    wind = time_results['onwind dispatch']
    wind = wind[815:959]

#print(electrolysis_dispatch+battery_charged+demand-battery_dispatch-fuelcell_dispatch-solar-wind) #Should equal zero or inifitessimally close

#replace the index of each series with numbers 1 through 168
wind.index = range(1,145)
solar.index = range(1,145)
demand.index = range(1,145)
battery_dispatch.index = range(1,145)
battery_charged.index = range(1,145)


#==============================================================================
# Plotting
#==============================================================================

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(1, 145)
ax.set_ylim(-3500, 4000)

# Set the color of the spines
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')
ax.spines['right'].set_color('black')
ax.spines['top'].set_color('black')

# Set the linewidth of the spines
ax.spines['left'].set_linewidth(1)
ax.spines['bottom'].set_linewidth(1)
ax.spines['right'].set_linewidth(1)
ax.spines['top'].set_linewidth(1)

# Plot dispatch curves
x = range(1,145)
# Fill the area under each line with the corresponding color
p1 = ax.fill_between(x, -demand, alpha=1, color='black', label = 'Demand')
p2 = ax.fill_between(x, -battery_charged, alpha=1, color=batt_q, label='Battery')

p6 = ax.fill_between(x, solar, alpha=1, color=solar_q, label='Solar')
p4 = ax.fill_between(x, battery_dispatch, alpha=1, color=batt_q)
p7 = ax.fill_between(x, wind, alpha=0.9, color=wind_q, label='Wind')

# Set x-axis ticks
#set major ticks at x=12, 36, 60, 84, 108, 132, 156 and label them with 'Jan 24', 'Jan 25', 'Jan 26', 'Jan 27', 'Jan 28', 'Jan 29', 'Jan 30'
ax.xaxis.set_major_locator(ticker.FixedLocator([12, 36, 60, 84, 108, 132]))
ax.xaxis.set_major_formatter(ticker.FixedFormatter(['Feb 4', 'Feb 5', 'Feb 6', 'Feb 7', 'Feb 8', 'Feb 9']))
ax.tick_params(axis='x', colors='black', labelsize='28',rotation=45)

# Set y-axis label and ticks
ax.set_ylabel('Electricity Dispatch (MW)', fontsize = '28')
ax.yaxis.set_major_locator(ticker.MultipleLocator(1000))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(500))
ax.tick_params(axis='y', colors='black', labelsize='28',length=10)
ax.tick_params(axis='x', colors='black', labelsize='28',length=8)
ax.tick_params(axis='y', which='major', left='on', direction='inout')

# Remove gridlines
ax.grid(False)

# Set title
#plt.title('Dispatch Curves 2006-02-04\nthrough 2006-02-09', fontsize='26')

'''
y = ['Demand', 'Battery', 'Solar', 'Wind']
legend = plt.legend(reversed([p1, p2, p6, p7]), reversed(y),bbox_to_anchor=(1.19, 0.65), fontsize='12', edgecolor='black')

for handle in legend.legendHandles:
    handle.set_edgecolor('black')
'''
# Display the plot
plt.savefig('C:\\Users\\Dominic\\desktop\\Oahu Results\\2006_02_04solar_drought_batt_only_dispatch_curves.png', dpi=300, bbox_inches='tight')
plt.show()