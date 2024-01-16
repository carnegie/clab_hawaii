from __future__ import division
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns  # Import Seaborn
import datetime

# Set Seaborn style
#sns.set_style("whitegrid")
sns.set(style='ticks') #Looks better

pickle3 = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S9 - Load Shifting/Full 14 yr/Outputs/oahu_load_shifting_improved_no_pgp_output.pickle'
pickle4 = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S9 - Load Shifting/Full 14 yr/Outputs/oahu_load_shifting_improved_yes_pgp_output.pickle'

#NO PGP
# read in the load shift state of charge time series
with open(pickle3, 'rb') as f:
#with open(pickle4, 'rb') as f:
    data = pickle.load(f)
    time_results = data['time results']
    load_shift = time_results['load_shift state of charge']

load_shift_values = load_shift.values
#print(load_shift_values)
#print(load_shift)

# Separate the load shift time series into 24 hours
load_shift_24 = []
for i in range(24):
    load_shift_24.append(load_shift_values[i::24])
#print(load_shift_24)

# Create a list of the average load shift for each hour of the day
load_shift_24_avg = [np.mean(load_shift_24[i]) for i in range(24)]
#print(load_shift_24_avg)

# Calculate the standard deviation of the load shift for each hour of the day
load_shift_24_std = [np.std(load_shift_24[i]) for i in range(24)]
#print(load_shift_24_std)

#YES PGP
# read in the load shift state of charge time series
with open(pickle4, 'rb') as f:
#with open(pickle4, 'rb') as f:
    data = pickle.load(f)
    time_results = data['time results']
    load_shift = time_results['load_shift state of charge']

load_shift_values = load_shift.values
#print(load_shift_values)
#print(load_shift)

# Separate the load shift time series into 24 hours
load_shift_yhes_24 = []
for i in range(24):
    load_shift_yhes_24.append(load_shift_values[i::24])
#print(load_shift_24)

# Create a list of the average load shift for each hour of the day
load_shift_yhes_24_avg = [np.mean(load_shift_yhes_24[i]) for i in range(24)]
#print(load_shift_24_avg)

# Calculate the standard deviation of the load shift for each hour of the day
#load_shift_24_std = [np.std(load_shift_24[i]) for i in range(24)]
#print(load_shift_24_std)


#Plot
fig, ax = plt.subplots(figsize=(11, 6))

sns.lineplot(x=np.arange(1,25), y=load_shift_24_avg, marker="o", label="With HES", color='black')
sns.lineplot(x=np.arange(1,25), y=load_shift_yhes_24_avg, marker="o", label="Without HES", color='black', linestyle='dashed')
#plt.errorbar(np.arange(1,25), load_shift_24_avg, yerr=load_shift_24_std, fmt='o', capsize=5, color='royalblue')  # Adding error bars
ax.set_xlabel('Hour of the Day', fontsize=22)
ax.set_ylabel('Average Load Shift\nState of Charge', fontsize=22)
ax.set_title('Average Load Shift State of Charge\nOver the Day', fontsize=26, pad=10)
ax.tick_params(axis='both', which='major', labelsize=20)

plt.xticks(np.arange(1,25))  # Set x-axis ticks to hours

plt.legend(loc='upper right',fontsize=20)
plt.tight_layout()
plt.savefig('C:\\Users\\Dominic\\desktop\\Oahu Results\\Avg Daily Load Shift No HES.jpg', dpi = 300, bbox_inches='tight')
plt.show()