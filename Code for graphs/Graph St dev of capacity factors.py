import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import seaborn as sns
from pathlib import Path
import os
import math

HI_wind = Path("/Users/Dominic/Desktop/Oahu wind toolkit means.csv")
HI_wind_no_leap = Path("/Users/Dominic/Desktop/Oahu wind toolkit means - no leap.csv")
HI_solar = Path("/Users/Dominic/Desktop/Oahu nsrdb means 2006 - 2019.csv")
HI_solar_no_leap = Path("/Users/Dominic/Desktop/Oahu nsrdb means 2006 - 2019 - no leap.csv")
output_path = '/Users/Dominic/desktop/'

#import data from column 4 starting at row 7 into a pandas dataframe
df = pd.DataFrame()
df = pd.read_csv(HI_wind, header=5, usecols=[4])



#generate average daily wind capacity factors for df
#take the mean of every 24 rows (every day) of df
res = df.groupby(np.arange(len(df))//24).mean()



#Create dataframes with average daily wind cfs for each year
df_2008 = pd.DataFrame()
df_2008 = pd.concat([df_2008, res.iloc[730:1096]], axis=0, ignore_index = True)
df_2012 = pd.DataFrame()
df_2012 = pd.concat([df_2012, res.iloc[2191:2557]], axis=0, ignore_index = True)
df_2016 = pd.DataFrame()
df_2016 = pd.concat([df_2016, res.iloc[3652:4018]], axis=0, ignore_index = True)

#determine average daily wind capacity factor for each date of the year over the 14 year period without leap years, then add calculate leap
#years separately and add to the correct position in the dataframe
dff = pd.read_csv(HI_wind_no_leap, header=5, usecols=[4])
res_noleap = dff.groupby(np.arange(len(dff))//24).mean()



#Take mean of every 365 rows (every day) of res_noleap
df_avg = pd.DataFrame()
for i in range(365):
    df_avg = pd.concat([df_avg, res_noleap.iloc[i::365].mean(axis=0)], axis=0, ignore_index = True)


df_avg_noleap_list = df_avg[0].tolist()


#add leap years to the correct position in the df_avg dataframe
feb29 = (df_2008.loc[59, 'w_cfs'] + df_2012.loc[59, 'w_cfs'] + df_2016.loc[59, 'w_cfs'])/3
df_avg.loc[58.5] = feb29
df_avg = df_avg.sort_index().reset_index(drop=True)
#print(df_avg)

df_avg_list = df_avg[0].tolist()



#Add every 365th value of dff to the dataframe df_days
df_days = pd.DataFrame()
for i in range(365):
    df_days = pd.concat([df_days, res_noleap.iloc[i::365]], axis=0, ignore_index = True)
    #the first 14 values of df_days are the 14 values for January 1st, the next 14 values are the 14 values for January 2nd, etc.

#Calculate the standard deviation of every 14 values in df_days
df_std = pd.DataFrame()
for i in range(365):
    df_std = pd.concat([df_std, df_days.iloc[i::365].std(axis=0)], axis=0, ignore_index = True)
    #the first 14 values of df_std are the 14 standard deviations for January 1st, the next 14 values are the 14 standard deviations for January 2nd, etc.

#Calculate the standard deviation of February 29th
f29 = pd.DataFrame()
f29 = pd.concat([f29, df_2008.iloc[59], df_2012.iloc[59], df_2016.iloc[59]], axis=0, ignore_index = True)
f29_std = f29.std(axis=0)

#Add the standard deviation of February 29th to the correct position in the df_std dataframe
df_std.loc[58.5] = f29_std
df_std = df_std.sort_index().reset_index(drop=True)

#============================================================================================================
#Now do solar
#============================================================================================================

#import data from column 4 starting at row 7 into a pandas dataframe
df_solar = pd.DataFrame()
df_solar= pd.read_csv(HI_solar, header=5, usecols=[4])



#generate average daily wind capacity factors for df
#take the mean of every 24 rows (every day) of df
res_solar = df.groupby(np.arange(len(df))//24).mean()



#Create dataframes with average daily wind cfs for each year
df_2008_solar = pd.DataFrame()
df_2008_solar = pd.concat([df_2008_solar, res_solar.iloc[730:1096]], axis=0, ignore_index = True)
df_2012_solar = pd.DataFrame()
df_2012_solar = pd.concat([df_2012_solar, res_solar.iloc[2191:2557]], axis=0, ignore_index = True)
df_2016_solar = pd.DataFrame()
df_2016_solar = pd.concat([df_2016_solar, res_solar.iloc[3652:4018]], axis=0, ignore_index = True)



#determine average daily wind capacity factor for each date of the year over the 14 year period without leap years, then add calculate leap
#years separately and add to the correct position in the dataframe
dff_solar = pd.read_csv(HI_solar_no_leap, header=5, usecols=[4])
res_noleap_solar = dff_solar.groupby(np.arange(len(dff_solar))//24).mean()



#Take mean of every 365 rows (every day) of res_noleap
df_avg_solar = pd.DataFrame()
for i in range(365):
    df_avg_solar = pd.concat([df_avg_solar, res_noleap_solar.iloc[i::365].mean(axis=0)], axis=0, ignore_index = True)


df_avg_noleap_list_solar = df_avg_solar[0].tolist()


#add leap years to the correct position in the df_avg dataframe
feb29_solar = (df_2008_solar.loc[59, 'w_cfs'] + df_2012_solar.loc[59, 'w_cfs'] + df_2016_solar.loc[59, 'w_cfs'])/3
df_avg_solar.loc[58.5] = feb29_solar
df_avg_solar = df_avg_solar.sort_index().reset_index(drop=True)
#print(df_avg)

df_avg_list_solar = df_avg_solar[0].tolist()


#Add every 365th value of dff to the dataframe df_days
df_days_solar = pd.DataFrame()
for i in range(365):
    df_days_solar = pd.concat([df_days_solar, res_noleap_solar.iloc[i::365]], axis=0, ignore_index = True)
    #the first 14 values of df_days are the 14 values for January 1st, the next 14 values are the 14 values for January 2nd, etc.

#Calculate the standard deviation of every 14 values in df_days
df_std_solar = pd.DataFrame()
for i in range(365):
    df_std_solar = pd.concat([df_std_solar, df_days_solar.iloc[i::365].std(axis=0)], axis=0, ignore_index = True)
    #the first 14 values of df_std are the 14 standard deviations for January 1st, the next 14 values are the 14 standard deviations for January 2nd, etc.


#Calculate the standard deviation of February 29th
f29_solar = pd.DataFrame()
f29_solar = pd.concat([f29_solar, df_2008_solar.iloc[59], df_2012_solar.iloc[59], df_2016_solar.iloc[59]], axis=0, ignore_index = True)
f29_std_solar = f29_solar.std(axis=0)


#Add the standard deviation of February 29th to the correct position in the df_std dataframe
df_std_solar.loc[58.5] = f29_std_solar
df_std_solar = df_std_solar.sort_index().reset_index(drop=True)

#Compute average st devs for the two generators
avg_std_solar = df_std_solar.mean(axis=0)
avg_std_solar[0] = round(avg_std_solar[0],3)
print(avg_std_solar[0])
avg_std_wind = df_std.mean(axis=0)
avg_std_wind[0] = round(avg_std_wind[0],3)
print(avg_std_wind[0])



#============================================================================================================
#Plotting
#============================================================================================================
#Add a column to df_std with values from 0 to 365
df_std['index'] = np.arange(0, 366)
df_std_solar['index'] = np.arange(0, 366)


df_std.columns = ['w_cfs', 'index']
df_std_solar.columns = ['s_cfs', 'index']


#Make a scatter plot of the standard deviation values from df_std for each day of the year
ax1 = df_std.plot.scatter(x='index', y='w_cfs', color='blue', figsize=(20,10), s=250, marker='1')
ax2 = df_std_solar.plot.scatter(x='index', y='s_cfs', color='orange', ax=ax1, s=60, marker='*')


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ytick = np.arange(0, 0.351, 0.05)
ax1.set_yticklabels(np.round(ytick, 2),fontsize = 20)
ax1.set_xticks(np.arange(0, 360, 31))
ax1.set_xticklabels(months, fontsize = 20)
ax1.set_xlabel('Month of year', fontsize=26, labelpad=10)
ax1.set_ylabel('Standard Deviation', fontsize=26, labelpad = 10)
ax1.set_title('Standard Deviation of Daily Wind and Solar Capacity Factors', fontsize=30, pad=15)

y = ['Wind','Solar']
ax1.legend(y, loc="best", fontsize = 25)

ax1.text(90, 0.116, 'Avg. Solar St. Dev. = ' + str(avg_std_solar[0])+ '          Avg. Wind St. Dev. = ' + str(avg_std_wind[0]), fontsize = 17)

plt.savefig(output_path + 'Standard Deviation of Wind and Solar Cfs.png')
plt.show()