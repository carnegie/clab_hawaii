'''This code will make a stacked bar chart of the estimated current system cost, broken down by the 4 components we assessed'''

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

ecrf = 0.251507
fom = 0.001836
vom = 0.002792
investment = 0.001159

#Stacked bar chart
fig = plt.figure(figsize=(6,10))
ax1 = plt.subplot2grid((1, 1), (0, 0), colspan=1, rowspan=1)
index = np.arange(1)
bar_width = 0.35
opacity = 1
p1 = ax1.bar(index, ecrf, bar_width, alpha=opacity, color='blue', label='Energy Cost\n Recovery Factor')
p2 = ax1.bar(index, fom, bar_width, alpha=opacity, color='green', label='Fixed O&M', bottom=ecrf)
p3 = ax1.bar(index, vom, bar_width, alpha=opacity, color='red', label='Variable O&M', bottom=ecrf+fom)
p4 = ax1.bar(index, investment, bar_width, alpha=opacity, color='yellow', label='Payment on \nInvestment', bottom=ecrf+fom+vom)

#add a black border to the bars
for bar in p1 + p2 + p3 + p4:
    bar.set_linewidth(1)
    bar.set_edgecolor('black')

plt.xlabel('Current\nElectricity System', fontsize=14, labelpad=12)
plt.ylabel('Cost ($/kWh)', fontsize=14)
plt.title('Estimated Cost per kWh of\nCurrent Electricity System', fontsize=14, pad = 20)
plt.ylim(0, 0.30)
plt.xlim(-0.4,0.4)
plt.yticks(fontsize=12)
ax = plt.gca() 
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.xticks(index)
plt.setp(plt.gca().get_xticklabels(), visible=False) #make xticks invisible



#make x and y axis text fontsize 14
for item in ([ax.xaxis.label] + ax.get_xticklabels() + ax.get_yticklabels()):
    item.set_fontsize(24)
    
for item in (ax.get_xticklabels()):    
    item.set_rotation(45)
    
    
ax.yaxis.label.set_fontsize(26)

ax.title.set_fontsize(30)


y = ['Energy Cost\nRecovery Factor', 'Fixed O&M', 'Variable O&M', 'Payment on \nInvestment']
legend = plt.legend(reversed([p1, p2, p3, p4]), reversed(y),bbox_to_anchor=(0.9, 0.7),fontsize='24', edgecolor='black')

for handle in legend.legendHandles:
    handle.set_edgecolor('black')

for bar in p1 + p2 + p3 + p4:
    bar.set_linewidth(1)
    bar.set_edgecolor('black')
plt.grid(visible=False)


plt.savefig('C:\\Users\\Dominic\\desktop\\Oahu Results\\cost current system.png', dpi=300, bbox_inches='tight')
plt.show()
