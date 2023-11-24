
'''
This code will determine the days for each year on which there is a solar drought. It will then use those index points to determine
the wind capacity factors on those days.It will then determine the wind capacity factor for those days divided by the average 
wind capacity factor for that day of the year over the 14 year period. It will divide the single year wind capacity factor by the
average wind capacity factor for that day of the year over the 14 year period. Finally, it will plot the solar drought days on the 
x axis and wind factor divided by 14 year average wind factor on the y axis.
'''


import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import seaborn as sns
from pathlib import Path
import os
from scipy.stats import linregress

HI_wind = Path("/Users/Dominic/Desktop/NSRDB weighted average Oahu solar cfs 2006-2019.csv")
HI_wind_no_leap = Path("/Users/Dominic/Desktop/NSRDB weighted average Oahu solar cfs 2006-2019 no leap.csv")
output_path = '/Users/Dominic/desktop/Oahu Results'


#import data from column 4 starting at row 7 into a pandas dataframe
df = pd.DataFrame()
df = pd.read_csv(HI_wind, header=5, usecols=[4])


#generate average daily wind capacity factors for df
#take the mean of every 24 rows (every day) of df
res = df.groupby(np.arange(len(df))//24).mean()


#Create dataframes with average daily wind cfs for each year
df_2006 = pd.DataFrame()
df_2006 = pd.concat([df_2006, res.iloc[0:365]], axis=0, ignore_index = True)
df_2007 = pd.DataFrame()
df_2007= pd.concat([df_2007, res.iloc[365:730]], axis=0, ignore_index = True)
df_2008 = pd.DataFrame()
df_2008 = pd.concat([df_2008, res.iloc[730:1096]], axis=0, ignore_index = True)
df_2009 = pd.DataFrame()
df_2009 = pd.concat([df_2009, res.iloc[1096:1461]], axis=0, ignore_index = True)
df_2010 = pd.DataFrame()
df_2010 = pd.concat([df_2010, res.iloc[1461:1826]], axis=0, ignore_index = True)
df_2011 = pd.DataFrame()
df_2011 = pd.concat([df_2011, res.iloc[1826:2191]], axis=0, ignore_index = True)
df_2012 = pd.DataFrame()
df_2012 = pd.concat([df_2012, res.iloc[2191:2557]], axis=0, ignore_index = True)
df_2013 = pd.DataFrame()
df_2013 = pd.concat([df_2013, res.iloc[2557:2922]], axis=0, ignore_index = True)
df_2014 = pd.DataFrame()
df_2014 = pd.concat([df_2014, res.iloc[2922:3287]], axis=0, ignore_index = True)
df_2015 = pd.DataFrame()
df_2015 = pd.concat([df_2015, res.iloc[3287:3652]], axis=0, ignore_index = True)
df_2016 = pd.DataFrame()
df_2016 = pd.concat([df_2016, res.iloc[3652:4018]], axis=0, ignore_index = True)
df_2017 = pd.DataFrame()
df_2017 = pd.concat([df_2017, res.iloc[4018:4383]], axis=0, ignore_index = True)
df_2018 = pd.DataFrame()
df_2018 = pd.concat([df_2018, res.iloc[4383:4748]], axis=0, ignore_index = True)
df_2019 = pd.DataFrame()
df_2019 = pd.concat([df_2019, res.iloc[4748:5113]], axis=0, ignore_index = True)

df_list = [df_2006, df_2007, df_2008, df_2009, df_2010, df_2011, df_2012, df_2013, df_2014, df_2015, df_2016, df_2017, df_2018, df_2019]


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


#determine how many consecutive days there are with wind capacity below 50% of the average
cutoff = 0.5
    
for i in range(365):
    if df_2006.loc[i, 'w_cfs'] < (df_avg_noleap_list[i]*cutoff):
        df_2006.loc[i, 'w_cfs'] = 1
    else:
        df_2006.loc[i, 'w_cfs'] = 0
print(df_2006)
for i in range(365):
    if df_2007.loc[i, 'w_cfs'] < (df_avg_noleap_list[i]*cutoff):
        df_2007.loc[i, 'w_cfs'] = 1
    else:
        df_2007.loc[i, 'w_cfs'] = 0
for i in range(366):
    if df_2008.loc[i, 'w_cfs'] < (df_avg_list[i]*cutoff):
        df_2008.loc[i, 'w_cfs'] = 1
    else:
        df_2008.loc[i, 'w_cfs'] = 0
for i in range(365):
    if df_2009.loc[i, 'w_cfs'] < (df_avg_noleap_list[i]*cutoff):
        df_2009.loc[i, 'w_cfs'] = 1
    else:
        df_2009.loc[i, 'w_cfs'] = 0
for i in range(365):
    if df_2010.loc[i, 'w_cfs'] < (df_avg_noleap_list[i]*cutoff):
        df_2010.loc[i, 'w_cfs'] = 1
    else:
        df_2010.loc[i, 'w_cfs'] = 0
for i in range(365):
    if df_2011.loc[i, 'w_cfs'] < (df_avg_noleap_list[i]*cutoff):
        df_2011.loc[i, 'w_cfs'] = 1
    else:
        df_2011.loc[i, 'w_cfs'] = 0
for i in range(366):
    if df_2012.loc[i, 'w_cfs'] < (df_avg_list[i]*cutoff):
        df_2012.loc[i, 'w_cfs'] = 1
    else:
        df_2012.loc[i, 'w_cfs'] = 0
for i in range(365):
    if df_2013.loc[i, 'w_cfs'] < (df_avg_noleap_list[i]*cutoff):
        df_2013.loc[i, 'w_cfs'] = 1
    else:
        df_2013.loc[i, 'w_cfs'] = 0
for i in range(365):
    if df_2014.loc[i, 'w_cfs'] < (df_avg_noleap_list[i]*cutoff):
        df_2014.loc[i, 'w_cfs'] = 1
    else:
        df_2014.loc[i, 'w_cfs'] = 0
for i in range(365):
    if df_2015.loc[i, 'w_cfs'] < (df_avg_noleap_list[i]*cutoff):
        df_2015.loc[i, 'w_cfs'] = 1
    else:
        df_2015.loc[i, 'w_cfs'] = 0
for i in range(366):
    if df_2016.loc[i, 'w_cfs'] < (df_avg_list[i]*cutoff):
        df_2016.loc[i, 'w_cfs'] = 1
    else:
        df_2016.loc[i, 'w_cfs'] = 0
for i in range(365):
    if df_2017.loc[i, 'w_cfs'] < (df_avg_noleap_list[i]*cutoff):
        df_2017.loc[i, 'w_cfs'] = 1
    else:
        df_2017.loc[i, 'w_cfs'] = 0
for i in range(365):
    if df_2018.loc[i, 'w_cfs'] < (df_avg_noleap_list[i]*cutoff):
        df_2018.loc[i, 'w_cfs'] = 1
    else:
        df_2018.loc[i, 'w_cfs'] = 0
for i in range(365):
    if df_2019.loc[i, 'w_cfs'] < (df_avg_noleap_list[i]*cutoff):
        df_2019.loc[i, 'w_cfs'] = 1
    else:
        df_2019.loc[i, 'w_cfs'] = 0

#add the index numbers of the days with values of 1 to a list
solar_2006 = df_2006[df_2006['w_cfs'] == 1].index.tolist()
solar_2007 = df_2007[df_2007['w_cfs'] == 1].index.tolist()
solar_2008 = df_2008[df_2008['w_cfs'] == 1].index.tolist()
solar_2009 = df_2009[df_2009['w_cfs'] == 1].index.tolist()
solar_2010 = df_2010[df_2010['w_cfs'] == 1].index.tolist()
solar_2011 = df_2011[df_2011['w_cfs'] == 1].index.tolist()
solar_2012 = df_2012[df_2012['w_cfs'] == 1].index.tolist()
solar_2013 = df_2013[df_2013['w_cfs'] == 1].index.tolist()
solar_2014 = df_2014[df_2014['w_cfs'] == 1].index.tolist()
solar_2015 = df_2015[df_2015['w_cfs'] == 1].index.tolist()
solar_2016 = df_2016[df_2016['w_cfs'] == 1].index.tolist()
solar_2017 = df_2017[df_2017['w_cfs'] == 1].index.tolist()
solar_2018 = df_2018[df_2018['w_cfs'] == 1].index.tolist()
solar_2019 = df_2019[df_2019['w_cfs'] == 1].index.tolist()

#==================================================================================================
#Determine value at indexed days
#==================================================================================================

#add the values of the solar capacity factor for each of the indexed days to a list for the year
#import data from column 4 starting at row 7 into a pandas dataframe
df = pd.DataFrame()
df = pd.read_csv(HI_wind, header=5, usecols=[4])


#generate average daily wind capacity factors for df
#take the mean of every 24 rows (every day) of df
res = df.groupby(np.arange(len(df))//24).mean()

#Create dataframes with average daily wind cfs for each year
df_2006 = pd.DataFrame()
df_2006 = pd.concat([df_2006, res.iloc[0:365]], axis=0, ignore_index = True)
df_2007 = pd.DataFrame()
df_2007= pd.concat([df_2007, res.iloc[365:730]], axis=0, ignore_index = True)
df_2008 = pd.DataFrame()
df_2008 = pd.concat([df_2008, res.iloc[730:1096]], axis=0, ignore_index = True)
df_2009 = pd.DataFrame()
df_2009 = pd.concat([df_2009, res.iloc[1096:1461]], axis=0, ignore_index = True)
df_2010 = pd.DataFrame()
df_2010 = pd.concat([df_2010, res.iloc[1461:1826]], axis=0, ignore_index = True)
df_2011 = pd.DataFrame()
df_2011 = pd.concat([df_2011, res.iloc[1826:2191]], axis=0, ignore_index = True)
df_2012 = pd.DataFrame()
df_2012 = pd.concat([df_2012, res.iloc[2191:2557]], axis=0, ignore_index = True)
df_2013 = pd.DataFrame()
df_2013 = pd.concat([df_2013, res.iloc[2557:2922]], axis=0, ignore_index = True)
df_2014 = pd.DataFrame()
df_2014 = pd.concat([df_2014, res.iloc[2922:3287]], axis=0, ignore_index = True)
df_2015 = pd.DataFrame()
df_2015 = pd.concat([df_2015, res.iloc[3287:3652]], axis=0, ignore_index = True)
df_2016 = pd.DataFrame()
df_2016 = pd.concat([df_2016, res.iloc[3652:4018]], axis=0, ignore_index = True)
df_2017 = pd.DataFrame()
df_2017 = pd.concat([df_2017, res.iloc[4018:4383]], axis=0, ignore_index = True)
df_2018 = pd.DataFrame()
df_2018 = pd.concat([df_2018, res.iloc[4383:4748]], axis=0, ignore_index = True)
df_2019 = pd.DataFrame()
df_2019 = pd.concat([df_2019, res.iloc[4748:5113]], axis=0, ignore_index = True)

solar_2006_value = pd.DataFrame()
solar_2006_value = df_2006.iloc[solar_2006]
solar_2007_value = pd.DataFrame()
solar_2007_value = df_2007.iloc[solar_2007]
solar_2008_value = pd.DataFrame()
solar_2008_value = df_2008.iloc[solar_2008]
solar_2009_value = pd.DataFrame()
solar_2009_value = df_2009.iloc[solar_2009]
solar_2010_value = pd.DataFrame()
solar_2010_value = df_2010.iloc[solar_2010]
solar_2011_value = pd.DataFrame()
solar_2011_value = df_2011.iloc[solar_2011]
solar_2012_value = pd.DataFrame()
solar_2012_value = df_2012.iloc[solar_2012]
solar_2013_value = pd.DataFrame()
solar_2013_value = df_2013.iloc[solar_2013]
solar_2014_value = pd.DataFrame()
solar_2014_value = df_2014.iloc[solar_2014]
solar_2015_value = pd.DataFrame()
solar_2015_value = df_2015.iloc[solar_2015]
solar_2016_value = pd.DataFrame()
solar_2016_value = df_2016.iloc[solar_2016]
solar_2017_value = pd.DataFrame()
solar_2017_value = df_2017.iloc[solar_2017]
solar_2018_value = pd.DataFrame()
solar_2018_value = df_2018.iloc[solar_2018]
solar_2019_value = pd.DataFrame()
solar_2019_value = df_2019.iloc[solar_2019]

#add the values from all the value dataframes to a list without the 'w_cfs' header
solar_value_list = []
solar_value_list.append(solar_2006_value.values.tolist())
solar_value_list.append(solar_2007_value.values.tolist())
solar_value_list.append(solar_2008_value.values.tolist())
solar_value_list.append(solar_2009_value.values.tolist())
solar_value_list.append(solar_2010_value.values.tolist())
solar_value_list.append(solar_2011_value.values.tolist())
solar_value_list.append(solar_2012_value.values.tolist())
solar_value_list.append(solar_2013_value.values.tolist())
solar_value_list.append(solar_2014_value.values.tolist())
solar_value_list.append(solar_2015_value.values.tolist())
solar_value_list.append(solar_2016_value.values.tolist())
solar_value_list.append(solar_2017_value.values.tolist())
solar_value_list.append(solar_2018_value.values.tolist())
solar_value_list.append(solar_2019_value.values.tolist())

#turn solar_value_list into a list without the brackets
solar_value_list = [item for sublist in solar_value_list for item in sublist]
solar_value_list = [item for sublist in solar_value_list for item in sublist]
print(solar_value_list)


#====================================================================================================
#Input the wind data and get them into yearly dataframes
#====================================================================================================

HI_wind = Path("/Users/Dominic/Desktop/WIND weighted average Oahu wind cfs 2006-2019.csv")
HI_wind_no_leap = Path("/Users/Dominic/Desktop/WIND weighted average Oahu wind cfs 2006-2019 no leap.csv")
output_path = '/Users/Dominic/desktop/'


#import data from column 4 starting at row 7 into a pandas dataframe
df = pd.DataFrame()
df = pd.read_csv(HI_wind, header=5, usecols=[4])



#generate average daily wind capacity factors for df
#take the mean of every 24 rows (every day) of df
res = df.groupby(np.arange(len(df))//24).mean()



#Create dataframes with average daily wind cfs for each year
df_2006 = pd.DataFrame()
df_2006 = pd.concat([df_2006, res.iloc[0:365]], axis=0, ignore_index = True)
df_2007 = pd.DataFrame()
df_2007= pd.concat([df_2007, res.iloc[365:730]], axis=0, ignore_index = True)
df_2008 = pd.DataFrame()
df_2008 = pd.concat([df_2008, res.iloc[730:1096]], axis=0, ignore_index = True)
df_2009 = pd.DataFrame()
df_2009 = pd.concat([df_2009, res.iloc[1096:1461]], axis=0, ignore_index = True)
df_2010 = pd.DataFrame()
df_2010 = pd.concat([df_2010, res.iloc[1461:1826]], axis=0, ignore_index = True)
df_2011 = pd.DataFrame()
df_2011 = pd.concat([df_2011, res.iloc[1826:2191]], axis=0, ignore_index = True)
df_2012 = pd.DataFrame()
df_2012 = pd.concat([df_2012, res.iloc[2191:2557]], axis=0, ignore_index = True)
df_2013 = pd.DataFrame()
df_2013 = pd.concat([df_2013, res.iloc[2557:2922]], axis=0, ignore_index = True)
df_2014 = pd.DataFrame()
df_2014 = pd.concat([df_2014, res.iloc[2922:3287]], axis=0, ignore_index = True)
df_2015 = pd.DataFrame()
df_2015 = pd.concat([df_2015, res.iloc[3287:3652]], axis=0, ignore_index = True)
df_2016 = pd.DataFrame()
df_2016 = pd.concat([df_2016, res.iloc[3652:4018]], axis=0, ignore_index = True)
df_2017 = pd.DataFrame()
df_2017 = pd.concat([df_2017, res.iloc[4018:4383]], axis=0, ignore_index = True)
df_2018 = pd.DataFrame()
df_2018 = pd.concat([df_2018, res.iloc[4383:4748]], axis=0, ignore_index = True)
df_2019 = pd.DataFrame()
df_2019 = pd.concat([df_2019, res.iloc[4748:5113]], axis=0, ignore_index = True)

df_list = [df_2006, df_2007, df_2008, df_2009, df_2010, df_2011, df_2012, df_2013, df_2014, df_2015, df_2016, df_2017, df_2018, df_2019]

#Determine the values of each dataframe according to the index for that year based on solar_2006 through solar_2019 index
wind_2006_value = pd.DataFrame()
wind_2006_value = df_2006.iloc[solar_2006]
wind_2007_value = pd.DataFrame()
wind_2007_value = df_2007.iloc[solar_2007]
wind_2008_value = pd.DataFrame()
wind_2008_value = df_2008.iloc[solar_2008]
wind_2009_value = pd.DataFrame()
wind_2009_value = df_2009.iloc[solar_2009]
wind_2010_value = pd.DataFrame()
wind_2010_value = df_2010.iloc[solar_2010]
wind_2011_value = pd.DataFrame()
wind_2011_value = df_2011.iloc[solar_2011]
wind_2012_value = pd.DataFrame()
wind_2012_value = df_2012.iloc[solar_2012]
wind_2013_value = pd.DataFrame()
wind_2013_value = df_2013.iloc[solar_2013]
wind_2014_value = pd.DataFrame()
wind_2014_value = df_2014.iloc[solar_2014]
wind_2015_value = pd.DataFrame()
wind_2015_value = df_2015.iloc[solar_2015]
wind_2016_value = pd.DataFrame()
wind_2016_value = df_2016.iloc[solar_2016]
wind_2017_value = pd.DataFrame()
wind_2017_value = df_2017.iloc[solar_2017]
wind_2018_value = pd.DataFrame()
wind_2018_value = df_2018.iloc[solar_2018]
wind_2019_value = pd.DataFrame()
wind_2019_value = df_2019.iloc[solar_2019]

#add the values from all the value dataframes to a list without the 'w_cfs' header
wind_value_list = []
wind_value_list.append(wind_2006_value.values.tolist())
wind_value_list.append(wind_2007_value.values.tolist())
wind_value_list.append(wind_2008_value.values.tolist())
wind_value_list.append(wind_2009_value.values.tolist())
wind_value_list.append(wind_2010_value.values.tolist())
wind_value_list.append(wind_2011_value.values.tolist())
wind_value_list.append(wind_2012_value.values.tolist())
wind_value_list.append(wind_2013_value.values.tolist())
wind_value_list.append(wind_2014_value.values.tolist())
wind_value_list.append(wind_2015_value.values.tolist())
wind_value_list.append(wind_2016_value.values.tolist())
wind_value_list.append(wind_2017_value.values.tolist())
wind_value_list.append(wind_2018_value.values.tolist())
wind_value_list.append(wind_2019_value.values.tolist())

#turn solar_value_list into a list without the brackets
wind_value_list = [item for sublist in wind_value_list for item in sublist]
wind_value_list = [item for sublist in wind_value_list for item in sublist]
print(wind_value_list)

# Calculate the regression line
slope, intercept, r_value, p_value, std_err = linregress(solar_value_list, wind_value_list)
#turn solar_value_list into an array
solar_value_list = np.array(solar_value_list)
fit = slope * solar_value_list + intercept

# Calculate the R-squared value
r_squared = r_value**2

sns.set(style='ticks')

# Make a scatterplot with solar_value_list as the x-axis and wind_value_list as the y-axis
fig, ax = plt.subplots(figsize=(8, 8))
ax = plt.subplot2grid((1, 1), (0, 0), colspan=1, rowspan=1)
# Plot the scatterplot of data points
sns.scatterplot(x=solar_value_list, y=wind_value_list, ax=ax, color='royalblue', s=80)

ax.set_ylim(-0.04, 1.2)
ax.set_yticks(np.arange(0, 1.25, 0.2))

# Plot the regression line
ax.plot(solar_value_list, fit, color='black', label=f'y = {slope:.2f}x + {intercept:.2f}  |  $R^2$ = {r_squared:.4f}')

ax.set_xlabel('Solar Capacity Factor',fontsize=26, labelpad=10)
ax.set_ylabel('Wind Capacity Factor',fontsize=26, labelpad=12)
ax.set_title('Capacity Factors on\nSolar Drought Days', fontsize=28, pad=15)
ax.tick_params(axis='both', which='major', labelsize=24)
ax.tick_params(axis='x', rotation=45)
plt.legend(loc='upper right',fontsize=20)

plt.tight_layout()
plt.savefig('C:\\Users\\Dominic\\desktop\\Oahu Results\\Correlation solar droughts to wind cfs.png', dpi=300, bbox_inches='tight')
plt.show()
