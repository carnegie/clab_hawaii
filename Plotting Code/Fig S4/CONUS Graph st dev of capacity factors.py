import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import seaborn as sns
from pathlib import Path
import os
import math
import matplotlib.ticker as ticker

HI_wind_no_leap = Path("/Users/covel/OneDrive/Desktop/wind_cf_Dan_normalized_to_0.38_mean_United States - 2006 thru 2015 - no leap.csv")
HI_solar_no_leap = Path("/Users/covel/OneDrive/Desktop/solar_series_Shaner_unnormalized - 2006 onward - no leap.csv")
output_path = '/Users/covel/OneDrive/desktop/Oahu Results'

# Wind data processing
dff = pd.read_csv(HI_wind_no_leap, header=5, usecols=[4])
res_noleap = dff.groupby(np.arange(len(dff))//24).mean()

# Calculating the relative standard deviation for wind
df_rel_std_wind = pd.DataFrame()
for i in range(365):
    day_data = res_noleap.iloc[i::365]
    rel_std = (day_data.std(axis=0) / day_data.mean(axis=0)) * 100
    df_rel_std_wind = pd.concat([df_rel_std_wind, rel_std], axis=0, ignore_index=True)

# Solar data processing
dff_solar = pd.read_csv(HI_solar_no_leap, header=5, usecols=[4])
res_noleap_solar = dff_solar.groupby(np.arange(len(dff_solar))//24).mean()

# Calculating the relative standard deviation for solar
df_rel_std_solar = pd.DataFrame()
for i in range(365):
    day_data_solar = res_noleap_solar.iloc[i::365]
    rel_std_solar = (day_data_solar.std(axis=0) / day_data_solar.mean(axis=0)) * 100
    df_rel_std_solar = pd.concat([df_rel_std_solar, rel_std_solar], axis=0, ignore_index=True)

# Compute average relative standard deviations for the two generators
avg_rel_std_solar = df_rel_std_solar.mean(axis=0)
avg_rel_std_solar[0] = round(avg_rel_std_solar[0], 3)
print('Average relative standard deviation for solar:', avg_rel_std_solar[0], '%')

avg_rel_std_wind = df_rel_std_wind.mean(axis=0)
avg_rel_std_wind[0] = round(avg_rel_std_wind[0], 3)
print('Average relative standard deviation for wind:', avg_rel_std_wind[0], '%')

#============================================================================================================
# Plotting
#============================================================================================================
df_rel_std_wind['index'] = np.arange(0, 365)
df_rel_std_solar['index'] = np.arange(0, 365)

df_rel_std_wind.columns = ['w_cfs', 'index']
df_rel_std_solar.columns = ['s_cfs', 'index']

sns.set(style='ticks')
fig, ax1 = plt.subplots(figsize=(20, 6))
ax1 = plt.subplot2grid((1, 1), (0, 0), colspan=1, rowspan=1)
sns.scatterplot(data=df_rel_std_wind, x='index', y='w_cfs', color='blue', ax=ax1, s=200, marker='D')
sns.scatterplot(data=df_rel_std_solar, x='index', y='s_cfs', color='orange', ax=ax1, s=200, marker='o')

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ytick = np.arange(0, 160.1, 20)  # Update the ytick range based on your relative std data

ax1.set_yticks(ytick)
ax1.set_xticks(np.arange(0, 360, 31))
ax1.set_xticklabels(months, fontsize=28, rotation=45)
ax1.set_xlabel('Month of Year', fontsize=30, labelpad=10)
ax1.set_ylabel('Relative Standard Deviation (%)', fontsize=30, labelpad=10)
ax1.set_title('Relative Standard Deviation of Daily Wind\nand Solar Capacity Factors For CONUS', fontsize=36, pad=15)

y = ['Wind', 'Solar']
ax1.legend(y, loc='center right', bbox_to_anchor=(1.18, 0.5), fontsize=30)
ax1.tick_params(axis='y', labelsize=28)
plt.margins(x=0.01)
#plt.savefig(os.path.join(output_path, 'CONUS Relative Standard Deviation of Wind and Solar cfs.jpg'), dpi=300, bbox_inches='tight')
plt.show()