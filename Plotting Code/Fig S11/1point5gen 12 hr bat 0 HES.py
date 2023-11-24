'''this code will plot the size vs reliability for each area'''

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
import seaborn as sns

oahu_size=[1550]
oahu_hours=[((113951-20645.109)/113951)*100]

CA_size=[423971]
CA_hours=[((113951-19579.16)/113951)*100]

WECC_size=[4661978]
WECC_hours=[((113951-13611.75)/113951)*100]

CONUS_size=[9834000]
CONUS_hours=[((113951-11390.079)/113951)*100]

#Plot
sns.set(style='ticks') #Looks better
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(oahu_size, oahu_hours, 'o', color='magenta', label='Oahu', markersize=10)
ax.plot(CA_size, CA_hours, 'o', color='royalblue', label='CA', markersize=10)
ax.plot(WECC_size, WECC_hours, 'o', color='purple', label='WECC', markersize=10)
ax.plot(CONUS_size, CONUS_hours, 'o', color='black', label='CONUS', markersize=10)
ax.set_ylabel('Hours of Lost Load [h]')

y = ['Oahu','CA', 'WECC', 'CONUS']
legend = plt.legend(y, loc='best',fontsize=16)

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

ax.set_xlabel('Land Area (km$^2$)', fontsize=16)
ax.set_ylabel('Reliability (share of demand\nmet by solar, wind, and battery)', fontsize=16)
ax.set_title('Land Area vs Reliability\n1.5x Generation, 12 Hours Storage', fontsize=18, pad=10)

plt.savefig('C:\\Users\\Dominic\\desktop\\Oahu Results\\land ara vs reliability.jpg', dpi = 300, bbox_inches='tight')
plt.show()
