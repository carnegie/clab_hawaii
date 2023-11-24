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


HI_wind_no_leap = Path("/Users/Dominic/Desktop/WIND weighted average Oahu wind cfs 2006-2019 no leap.csv")
HI_solar_no_leap = Path("/Users/Dominic/Desktop/NSRDB weighted average Oahu solar cfs 2006-2019 no leap.csv")
#HI_demand = Path("/Users/Dominic/Desktop/2006_2019_Hawaii_State_Hourly_Demand_Weighted_just_Oahu.csv")
#HI_demand_no_leap = Path("/Users/Dominic/Desktop/2006_2019_Hawaii_State_Hourly_Demand_Weighted_just_Oahu_no_leap.csv")
output_path = '/Users/Dominic/desktop/Oahu Results'

#determine average daily wind capacity factor for each date of the year over the 14 year period without leap years, then add calculate leap
#years separately and add to the correct position in the dataframe
dff = pd.read_csv(HI_wind_no_leap, header=5, usecols=[4])
res_noleap = dff.groupby(np.arange(len(dff))//24).mean()



#Calculate the standard deviation of every 14 values in df_days
df_std = pd.DataFrame()
for i in range(365):
    df_std = pd.concat([df_std, res_noleap.iloc[i::365].std(axis=0)], axis=0, ignore_index = True)
    #the first 14 values of df_std are the 14 standard deviations for January 1st, the next 14 values are the 14 standard deviations for January 2nd, etc.


#============================================================================================================
#Now do solar
#============================================================================================================

#determine average daily wind capacity factor for each date of the year over the 14 year period without leap years, then add calculate leap
#years separately and add to the correct position in the dataframe
dff_solar = pd.read_csv(HI_solar_no_leap, header=5, usecols=[4])
res_noleap_solar = dff_solar.groupby(np.arange(len(dff_solar))//24).mean()
print(res_noleap_solar)


#Calculate the standard deviation of every 14 values in df_days
df_std_solar = pd.DataFrame()
for i in range(365):
    df_std_solar = pd.concat([df_std_solar, res_noleap_solar.iloc[i::365].std(axis=0)], axis=0, ignore_index = True)
    #the first 14 values of df_std are the 14 standard deviations for January 1st, the next 14 values are the 14 standard deviations for January 2nd, etc.


#Compute average st devs for the two generators
avg_std_solar = df_std_solar.mean(axis=0)
avg_std_solar[0] = round(avg_std_solar[0],3)
print(avg_std_solar[0])
avg_std_wind = df_std.mean(axis=0)
avg_std_wind[0] = round(avg_std_wind[0],3)
print(avg_std_wind[0])
print(df_std_solar)
print(df_std)



#============================================================================================================
#Plotting
#============================================================================================================
df_std['index'] = np.arange(0, 365)
df_std_solar['index'] = np.arange(0, 365)

df_std.columns = ['w_cfs', 'index']
df_std_solar.columns = ['s_cfs', 'index']

sns.set(style='ticks')
fig, ax1 = plt.subplots(figsize=(20, 6))
ax1 = plt.subplot2grid((1, 1), (0, 0), colspan=1, rowspan=1)
sns.scatterplot(data=df_std, x='index', y='w_cfs', color='blue', ax=ax1, s=200, marker='D')
sns.scatterplot(data=df_std_solar, x='index', y='s_cfs', color='orange', ax=ax1, s=200, marker='o')

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ytick = np.arange(0, 0.351, 0.05)

ax1.set_yticks(np.arange(0, 0.351, 0.05))
ax1.set_xticks(np.arange(0, 365, 31))
ax1.set_xticklabels(months, fontsize=28, rotation=45)
ax1.set_xlabel('Month of Year', fontsize=30, labelpad=10)
ax1.set_ylabel('Standard Deviation', fontsize=30, labelpad=10)
ax1.set_title('Standard Deviation of Daily Wind\nand Solar Capacity Factors For Oahu', fontsize=36, pad=15)

y = ['Wind', 'Solar']
ax1.legend(y, loc='center right', bbox_to_anchor=(1.18, 0.5), fontsize=30)
ax1.tick_params(axis='y', labelsize=28)
plt.margins(x=0.01)
plt.savefig(os.path.join(output_path, 'Oahu Standard Deviation of Wind and Solar cfs.jpg'), dpi=300, bbox_inches='tight')
plt.show()