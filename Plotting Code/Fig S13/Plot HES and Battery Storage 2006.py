'''This code will plot the amount of energy stored in the battery and HES over the year 2006.'''

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
    h2_stored = time_results['h2_storage state of charge']
    battery_also_stored = time_results['battery state of charge']
    battery_also_stored = battery_also_stored[0:8759]
    h2_stored = h2_stored[0:8759]

with open(no_pgp, 'rb') as f:
    data2 = pickle.load(f)
    time_results = data2['time results']
    battery_stored = time_results['battery state of charge']
    battery_stored = battery_stored[0:8759]

#replace the index of each series with numbers 1 through 8759
battery_stored.index = range(1,8760)
battery_also_stored.index = range(1,8760)
h2_stored.index = range(1,8760)

#==============================================================================
# Plotting PGP case
#==============================================================================

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

ax.set_xlim([0, 8759])
ax.set_ylim([0, 80000])

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
x = range(1,8760)
p1 = ax.fill_between(x, h2_stored, alpha=1, color=pgp_q, label = 'Hydrogen')
p2 = ax.fill_between(x, battery_also_stored, alpha=1, color=batt_q, label = 'Battery')

# Set x-axis ticks
ax.xaxis.set_major_locator(ticker.FixedLocator([0, 730, 1460, 2190, 2920, 3650, 4380, 5110, 5840, 6570, 7300, 8030, 8760]))
ax.xaxis.set_major_formatter(ticker.FixedFormatter(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov','Dec']))

ax.tick_params(axis='x', colors='black', labelsize='28', rotation=45)
# Set y-axis label and ticks
ax.set_ylabel('Stored Energy (MWh)', fontsize = '30')
ax.yaxis.set_major_locator(ticker.MultipleLocator(20000))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5000))
ax.tick_params(axis='y', colors='black', labelsize='28',length=10)
ax.tick_params(axis='y', which='major', left='on', direction='inout')

# Set title
plt.title('Stored Energy During 2006 for\nBattery + HES System', fontsize='34')

ax.legend(['HES', 'Battery'], loc='upper left', fontsize=24)
ax.grid(False)
plt.savefig('C:\\Users\\Dominic\\desktop\\Oahu Results\\2006_hes_energy_stored.png', dpi=300, bbox_inches='tight')
plt.show()

#==============================================================================
'''
#HES system but only plot the battery component
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

ax.set_xlim([0, 8759])
ax.set_ylim([0, 8000])

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
x = range(1,8760)
p2 = ax.fill_between(x, battery_also_stored, alpha=1, color=batt_q, label = 'Battery')

# Set x-axis ticks
#set major ticks at x=360, 1800, 3240, 4680, 6120, 7560 and label them with 'Jan', 'Mar', 'May', 'Jul', 'Sep', 'Nov'
ax.xaxis.set_major_locator(ticker.FixedLocator([360, 1800, 3240, 4680, 6120, 7560]))
ax.xaxis.set_major_formatter(ticker.FixedFormatter(['Jan', 'Mar', 'May', 'Jul', 'Sep', 'Nov']))
ax.tick_params(axis='x', colors='black', labelsize='14')

# Set y-axis label and ticks
ax.set_ylabel('Stored Energy (MWh)', fontsize = '14')
ax.yaxis.set_major_locator(ticker.MultipleLocator(2000))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1000))
ax.tick_params(axis='y', colors='black', labelsize='12',length=3)
ax.tick_params(axis='y', which='major', left='on', direction='inout')

# Set title
plt.title('Stored Energy During 2006 for\nBattery + Hydrogen Energy Storage System\n*Showing Only the Battery Component*', fontsize='16')

ax.legend(['Battery'], loc='upper left')
ax.grid(False)
plt.savefig('C:\\Users\\Dominic\\desktop\\Oahu Results\\2006_hes_only_battery_component_energy_stored.png', dpi=300, bbox_inches='tight')
plt.show()

#==============================================================================

#Battery only system
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

ax.set_xlim([0, 8759])
ax.set_ylim([0, 24000])

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
x = range(1,8760)
p2 = ax.fill_between(x, battery_stored, alpha=1, color=batt_q, label = 'Battery')

# Set x-axis ticks
#set major ticks at x=360, 1800, 3240, 4680, 6120, 7560 and label them with 'Jan', 'Mar', 'May', 'Jul', 'Sep', 'Nov'
#ax.xaxis.set_major_locator(ticker.FixedLocator([360, 1800, 3240, 4680, 6120, 7560]))
#ax.xaxis.set_major_formatter(ticker.FixedFormatter(['Jan', 'Mar', 'May', 'Jul', 'Sep', 'Nov']))

ax.xaxis.set_major_locator(ticker.FixedLocator([0, 730, 1460, 2190, 2920, 3650, 4380, 5110, 5840, 6570, 7300, 8030, 8760]))
ax.xaxis.set_major_formatter(ticker.FixedFormatter(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov','Dec']))

ax.tick_params(axis='x', colors='black', labelsize='22', rotation=45)

# Set y-axis label and ticks
ax.set_ylabel('Stored Energy (MWh)', fontsize = '22')
ax.yaxis.set_major_locator(ticker.MultipleLocator(4000))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1000))
ax.tick_params(axis='y', colors='black', labelsize='20', length=10)
ax.tick_params(axis='y', which='major', left='on', direction='inout')

# Set title
plt.title('Stored Energy During 2006 for\nBattery-Only System', fontsize='26')

ax.legend(['Battery'], loc='upper left')
ax.grid(False)
#plt.savefig('C:\\Users\\Dominic\\desktop\\Oahu Results\\2006_battery_only_system_energy_stored.png', dpi=300, bbox_inches='tight')
plt.show()
'''