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

with open(pgp_above, 'rb') as f:
    data1 = pickle.load(f)
    time_results = data1['time results']
    #read in the column 'electrolysis dispatch' and use only rows 2015:2158
    electrolysis_dispatch = time_results['electrolysis dispatch']
    electrolysis_dispatch = electrolysis_dispatch[2015:2158]
    fuelcell_dispatch = time_results['fuel_cell dispatch']
    fuelcell_dispatch = fuelcell_dispatch[2015:2158]
    battery_dispatch = time_results['battery discharged']
    battery_dispatch = battery_dispatch[2015:2158]
    battery_charged = time_results['battery charged']
    battery_charged = battery_charged[2015:2158]
    demand = time_results['load load']
    demand = demand[2015:2158]
    solar = time_results['solar dispatch']
    solar = solar[2015:2158]
    wind = time_results['onwind dispatch']
    wind = wind[2015:2158]

#print(electrolysis_dispatch+battery_charged+demand-battery_dispatch-fuelcell_dispatch-solar-wind) #Should equal zero or inifitessimally close

#replace the index of each series with numbers 1 through 168
wind.index = range(1,144)
solar.index = range(1,144)
demand.index = range(1,144)
battery_dispatch.index = range(1,144)
battery_charged.index = range(1,144)
electrolysis_dispatch.index = range(1,144)
fuelcell_dispatch.index = range(1,144)


#==============================================================================
# Plotting
#==============================================================================

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(1, 144)
ax.set_ylim(-3800,4000)

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
x = range(1,144)
# Fill the area under each line with the corresponding color
p1 = ax.fill_between(x, -demand, alpha=1, color='black', label = 'Demand')
p2 = ax.fill_between(x, -battery_charged, alpha=1, color=batt_q, label='Battery')
p3 = ax.fill_between(x, -electrolysis_dispatch, alpha=1, color=pgp_q, label='Hydrogen')

p6 = ax.fill_between(x, solar, alpha=1, color=solar_q, label='Solar')
p5 = ax.fill_between(x, fuelcell_dispatch, alpha=1, color=pgp_q)
p4 = ax.fill_between(x, battery_dispatch, alpha=1, color=batt_q)
p7 = ax.fill_between(x, wind, alpha=0.9, color=wind_q, label='Wind')

# Set x-axis ticks
#set major ticks at x=12, 36, 60, 84, 108, 132, 156 and label them with 'Jan 24', 'Jan 25', 'Jan 26', 'Jan 27', 'Jan 28', 'Jan 29', 'Jan 30'
ax.xaxis.set_major_locator(ticker.FixedLocator([12, 36, 60, 84, 108, 132]))
ax.xaxis.set_major_formatter(ticker.FixedFormatter(['*Mar 26', 'Mar 27', '*Mar 28', '*Mar 29', '*Mar 30', '*Mar 31']))
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
#plt.title('Dispatch Curves 2006-03-26\nthrough 2006-03-31', fontsize='26')

'''
y = ['Demand', 'Battery', 'Hydrogen', 'Solar', 'Wind']
legend = plt.legend(reversed([p1, p2, p3, p6, p7]), reversed(y),bbox_to_anchor=(1.19, 0.65), fontsize='12', edgecolor='black')

for handle in legend.legendHandles:
    handle.set_edgecolor('black')
'''
# Display the plot
plt.savefig('C:\\Users\\Dominic\\desktop\\Oahu Results\\solar_drought_dispatch_curves.png', dpi=300, bbox_inches='tight')
plt.show()