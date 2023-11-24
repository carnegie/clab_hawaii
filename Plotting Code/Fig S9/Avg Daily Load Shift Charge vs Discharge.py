from __future__ import division
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns  # Import Seaborn
import datetime

# Set Seaborn style
#sns.set_style("whitegrid")
sns.set(style='ticks') #Looks better

pickle3 = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something2 - Load Shifting/Full 14 yr/Outputs/oahu_load_shifting_improved_no_pgp_output.pickle'
pickle4 = '/Users/Dominic/Desktop/13-6-23 Rerun/Figure S Something2 - Load Shifting/Full 14 yr/Outputs/oahu_load_shifting_improved_yes_pgp_output.pickle'

# read in the load shift state of charge time series
with open(pickle3, 'rb') as f:
#with open(pickle4, 'rb') as f:
    data = pickle.load(f)
    time_results = data['time results']
    load_shift_charged = time_results['load_shift charged']
    load_shift_discharged = time_results['load_shift discharged']

load_shift_charged_values = load_shift_charged.values
load_shift_discharged_values = load_shift_discharged.values
#print(load_shift_charged_values)
#print(load_shift_discharged_values)

combo = load_shift_charged_values - load_shift_discharged_values
#print(combo)

#Separate the combo time series into 24 hours
combo_24 = []
for i in range(24):
    combo_24.append(combo[i::24])
#print(combo_24[0])

# Create a list of the average load shift for each hour of the day
combo_24_avg = [np.mean(combo_24[i]) for i in range(24)]
#print(combo_24_avg)

# Calculate the standard deviation of the load shift for each hour of the day
combo_24_std = [np.std(combo_24[i]) for i in range(24)]
#print(combo_24_std)

#Plot
fig, ax = plt.subplots(figsize=(10, 6))

sns.lineplot(x=np.arange(1,25), y=combo_24_avg, marker="o", label="Average Load Shift Charge", color='black')
plt.errorbar(np.arange(1,25), combo_24_avg, yerr=combo_24_std, fmt='o', capsize=5, color='royalblue')  # Adding error bars
ax.set_xlabel('Hour of the Day', fontsize=16)
ax.set_ylabel('Average Load Shift Charge', fontsize=16)
ax.set_title('Average Load Shift Charging\n or Discharging over the Day', fontsize=18, pad=10)
ax.tick_params(axis='both', which='major', labelsize=12)

plt.xticks(np.arange(1,25))  # Set x-axis ticks to hours

#add a horizontal line at y=0
plt.axhline(y=0, color='black', linestyle='--')

plt.ylim(-.15, .15)

plt.legend(loc='upper center',fontsize=16)
plt.tight_layout()
plt.savefig('C:\\Users\\Dominic\\desktop\\Oahu Results\\Avg Load Shift Charge or Discharge No HES.jpg', dpi = 300, bbox_inches='tight')
plt.show()