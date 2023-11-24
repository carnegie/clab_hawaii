'''This code will plot the cost of electricity for systems in CONUS, WECC, CA, and Oahu with and without HES as
their reliability becomes more constrained'''

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

# Set Seaborn style
#sns.set_style("whitegrid")
sns.set(style='ticks') #Looks better

pickle1noHES = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something3 - Smaller Area Reliability/Lost load 1 10 100 series/Wind Only No HES/Outputs/CONUS_smaller_area_reliability_2006_1hr_no_pgp_output.pickle'
pickle2noHES = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something3 - Smaller Area Reliability/Lost load 1 10 100 series/Wind Only No HES/Outputs/CONUS_smaller_area_reliability_2006_10hr_no_pgp_output.pickle'
pickle3noHES = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something3 - Smaller Area Reliability/Lost load 1 10 100 series/Wind Only No HES/Outputs/CONUS_smaller_area_reliability_2006_100hr_no_pgp_output.pickle'
pickle4noHES = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something3 - Smaller Area Reliability/Lost load 1 10 100 series/Wind Only No HES/Outputs/WECC_smaller_area_reliability_2006_1hr_no_pgp_output.pickle'
pickle5noHES = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something3 - Smaller Area Reliability/Lost load 1 10 100 series/Wind Only No HES/Outputs/WECC_smaller_area_reliability_2006_10hr_no_pgp_output.pickle'
pickle6noHES = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something3 - Smaller Area Reliability/Lost load 1 10 100 series/Wind Only No HES/Outputs/WECC_smaller_area_reliability_2006_100hr_no_pgp_output.pickle'
pickle7noHES = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something3 - Smaller Area Reliability/Lost load 1 10 100 series/Wind Only No HES/Outputs/CA_smaller_area_reliability_2006_1hr_no_pgp_output.pickle'
pickle8noHES = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something3 - Smaller Area Reliability/Lost load 1 10 100 series/Wind Only No HES/Outputs/CA_smaller_area_reliability_2006_10hr_no_pgp_output.pickle'
pickle9noHES = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something3 - Smaller Area Reliability/Lost load 1 10 100 series/Wind Only No HES/Outputs/CA_smaller_area_reliability_2006_100hr_no_pgp_output.pickle'
pickle10noHES = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something3 - Smaller Area Reliability/Lost load 1 10 100 series/Wind Only No HES/Outputs/oahu_smaller_area_reliability_2006_1hr_no_pgp_output.pickle'
pickle11noHES = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something3 - Smaller Area Reliability/Lost load 1 10 100 series/Wind Only No HES/Outputs/oahu_smaller_area_reliability_2006_10hr_no_pgp_output.pickle'
pickle12noHES = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something3 - Smaller Area Reliability/Lost load 1 10 100 series/Wind Only No HES/Outputs/oahu_smaller_area_reliability_2006_100hr_no_pgp_output.pickle'
'''
pickle1yesHES = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something3 - Smaller Area Reliability/Lost load 1 10 100 series/Solar Only Yes HES/Outputs/CONUS_smaller_area_reliability_2006_1hr_yes_pgp_output.pickle'
pickle2yesHES = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something3 - Smaller Area Reliability/Lost load 1 10 100 series/Solar Only Yes HES/Outputs/CONUS_smaller_area_reliability_2006_10hr_yes_pgp_output.pickle'
pickle3yesHES = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something3 - Smaller Area Reliability/Lost load 1 10 100 series/Solar Only Yes HES/Outputs/CONUS_smaller_area_reliability_2006_100hr_yes_pgp_output.pickle'
pickle4yesHES = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something3 - Smaller Area Reliability/Lost load 1 10 100 series/Solar Only Yes HES/Outputs/WECC_smaller_area_reliability_2006_1hr_yes_pgp_output.pickle'
pickle5yesHES = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something3 - Smaller Area Reliability/Lost load 1 10 100 series/Solar Only Yes HES/Outputs/WECC_smaller_area_reliability_2006_10hr_yes_pgp_output.pickle'
pickle6yesHES = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something3 - Smaller Area Reliability/Lost load 1 10 100 series/Solar Only Yes HES/Outputs/WECC_smaller_area_reliability_2006_100hr_yes_pgp_output.pickle'
pickle7yesHES = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something3 - Smaller Area Reliability/Lost load 1 10 100 series/Solar Only Yes HES/Outputs/CA_smaller_area_reliability_2006_1hr_yes_pgp_output.pickle'
pickle8yesHES = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something3 - Smaller Area Reliability/Lost load 1 10 100 series/Solar Only Yes HES/Outputs/CA_smaller_area_reliability_2006_10hr_yes_pgp_output.pickle'
pickle9yesHES = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something3 - Smaller Area Reliability/Lost load 1 10 100 series/Solar Only Yes HES/Outputs/CA_smaller_area_reliability_2006_100hr_yes_pgp_output.pickle'
pickle10yesHES = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something3 - Smaller Area Reliability/Lost load 1 10 100 series/Solar Only Yes HES/Outputs/oahu_smaller_area_reliability_2006_1hr_yes_pgp_output.pickle'
pickle11yesHES = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something3 - Smaller Area Reliability/Lost load 1 10 100 series/Solar Only Yes HES/Outputs/oahu_smaller_area_reliability_2006_10hr_yes_pgp_output.pickle'
pickle12yesHES = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something3 - Smaller Area Reliability/Lost load 1 10 100 series/Solar Only Yes HES/Outputs/oahu_smaller_area_reliability_2006_100hr_yes_pgp_output.pickle'
'''
listnoHES = [pickle1noHES, pickle2noHES, pickle3noHES, pickle4noHES, pickle5noHES, pickle6noHES, pickle7noHES, pickle8noHES, pickle9noHES, pickle10noHES, pickle11noHES, pickle12noHES]
#listyesHES = [pickle1yesHES, pickle2yesHES, pickle3yesHES, pickle4yesHES, pickle5yesHES, pickle6yesHES, pickle7yesHES, pickle8yesHES, pickle9yesHES, pickle10yesHES, pickle11yesHES, pickle12yesHES]

#Read the cost of electricity from each pickle
noHES_cost = []
for pickles in listnoHES:
    with open(pickles, 'rb') as f:
        data = pickle.load(f)
        cost = data['case results']['system cost [$/h]'] / 1000
        noHES_cost.extend(cost.values) #Use extend vs append to add just the values
#print(noHES_cost)

#Split noHES_cost into 4 lists, one for each area
noHES_cost_CONUS = noHES_cost[0:3]
noHES_cost_WECC = noHES_cost[3:6]
noHES_cost_CA = noHES_cost[6:9]
noHES_cost_Oahu = noHES_cost[9:12]

print(noHES_cost_CONUS)
print(noHES_cost_WECC)
print(noHES_cost_CA)
print(noHES_cost_Oahu)

#Alter each list so that the values in each list are subtracted by the third value in the list
noHES_cost_CONUS = [i - noHES_cost_CONUS[2] for i in noHES_cost_CONUS]
noHES_cost_WECC = [i - noHES_cost_WECC[2] for i in noHES_cost_WECC]
noHES_cost_CA = [i - noHES_cost_CA[2] for i in noHES_cost_CA]
noHES_cost_Oahu = [i - noHES_cost_Oahu[2] for i in noHES_cost_Oahu]

print(noHES_cost_CONUS)
print(noHES_cost_WECC)
print(noHES_cost_CA)
print(noHES_cost_Oahu)
'''
#Read the cost of electricity from each yesHES pickle
yesHES_cost = []
for pickles in listyesHES:
    with open(pickles, 'rb') as f:
        data = pickle.load(f)
        cost = data['case results']['system cost [$/h]'] / 1000
        yesHES_cost.extend(cost.values) #Use extend vs append to add just the values
#print(yesHES_cost)

#Split yesHES_cost into 4 lists, one for each area
yesHES_cost_CONUS = yesHES_cost[0:3]
yesHES_cost_WECC = yesHES_cost[3:6]
yesHES_cost_CA = yesHES_cost[6:9]
yesHES_cost_Oahu = yesHES_cost[9:12]

print(yesHES_cost_CONUS)
print(yesHES_cost_WECC)
print(yesHES_cost_CA)
print(yesHES_cost_Oahu)

#Alter each list so that the values in each list are subtracted by the third value in the list
yesHES_cost_CONUS = [i - yesHES_cost_CONUS[2] for i in yesHES_cost_CONUS]
yesHES_cost_WECC = [i - yesHES_cost_WECC[2] for i in yesHES_cost_WECC]
yesHES_cost_CA = [i - yesHES_cost_CA[2] for i in yesHES_cost_CA]
yesHES_cost_Oahu = [i - yesHES_cost_Oahu[2] for i in yesHES_cost_Oahu]


print(yesHES_cost_CONUS)
print(yesHES_cost_WECC)
print(yesHES_cost_CA)
print(yesHES_cost_Oahu)
'''
#Plot
fig, ax = plt.subplots(figsize=(10, 6))

#Plot the noHES data
sns.lineplot(x=[1,10,100], y=noHES_cost_CONUS, marker="o", label="CONUS", color='black')
sns.lineplot(x=[1,10,100], y=noHES_cost_WECC, marker="o", label="WECC", color='purple')
sns.lineplot(x=[1,10,100], y=noHES_cost_CA, marker="o", label="CA", color='royalblue')
sns.lineplot(x=[1,10,100], y=noHES_cost_Oahu, marker="o", label="Oahu", color='magenta')
'''
#Plot the yesHES data
sns.lineplot(x=[1,10,100], y=yesHES_cost_CONUS, marker="o", label="CONUS", color='black', linestyle='dashed')
sns.lineplot(x=[1,10,100], y=yesHES_cost_WECC, marker="o", label="WECC", color='purple', linestyle='dashed')
sns.lineplot(x=[1,10,100], y=yesHES_cost_CA, marker="o", label="CA", color='royalblue', linestyle='dashed')
sns.lineplot(x=[1,10,100], y=yesHES_cost_Oahu, marker="o", label="Oahu", color='magenta', linestyle='dashed')
'''
y = ['CONUS', 'WECC', 'CA', 'Oahu']
legend = plt.legend(y, loc='upper right',fontsize=16)


#plt.ylim(0, 0.2)

ax.set_xlabel('Allowed Hours of Lost Load', fontsize=16)
ax.set_ylabel('Increase in Electricity Cost [$/kWh]', fontsize=16)
ax.set_title('Decrease in Electricity Price with\nIncreased Lost Load Allowed\nOnly Wind and Battery\nNo HES', fontsize=18, pad=10)

plt.savefig('C:\\Users\\Dominic\\desktop\\Oahu Results\\lost load series no hes wind only price decrease.jpg', dpi = 300, bbox_inches='tight')
plt.show()
