'''
I apologize for how long this code is. My iterations sometimes did not alter the dataframes, 
and my troubleshooting wasn't going anywhere fast, so I just copy and pasted for each year. 
'''

'''
This code will determine how many wind droughts there are in the data set. It will read the wind data into a dataframe, then calculate the 
average wind capacity for each day. It will then average the wind capacity for each date in the 14 years. It will then determine how many
consecutive days there are with wind capacity below 50% of the average. It will then plot the number of consecutive days with wind capacity
below 50% of the average for each date of each year
'''

import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pylab as pylab
import datetime
import seaborn as sns
from pathlib import Path
import os
import statistics
import matplotlib.ticker as ticker

HI_wind = Path("/Users/Dominic/Desktop/WIND weighted average Oahu wind cfs 2006-2019.csv")
HI_wind_no_leap = Path("/Users/Dominic/Desktop/WIND weighted average Oahu wind cfs 2006-2019 no leap.csv")
output_path = '/Users/Dominic/desktop/Oahu Results'

"""
For Solar
HI_wind = Path("/Users/Dominic/Desktop/NSRDB weighted average Oahu solar cfs 2006-2019.csv")
HI_wind_no_leap = Path("/Users/Dominic/Desktop/NSRDB weighted average Oahu solar cfs 2006-2019 no leap.csv")
output_path = '/Users/Dominic/desktop/Oahu Results'
"""

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
#print(df_2006)
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

#determine how many values of 1 are in each year
df_2006['w_cfs'].value_counts()
df_2007['w_cfs'].value_counts()
df_2008['w_cfs'].value_counts()
df_2009['w_cfs'].value_counts()
df_2010['w_cfs'].value_counts()
df_2011['w_cfs'].value_counts()
df_2012['w_cfs'].value_counts()
df_2013['w_cfs'].value_counts()
df_2014['w_cfs'].value_counts()
df_2015['w_cfs'].value_counts()
df_2016['w_cfs'].value_counts()
df_2017['w_cfs'].value_counts()
df_2018['w_cfs'].value_counts()
df_2019['w_cfs'].value_counts()

#print the number of wind droughts in each year
print('2006:  ', df_2006['w_cfs'].value_counts()[1])
print('2007:  ', df_2007['w_cfs'].value_counts()[1])
print('2008:  ', df_2008['w_cfs'].value_counts()[1])
print('2009:  ', df_2009['w_cfs'].value_counts()[1])
print('2010:  ', df_2010['w_cfs'].value_counts()[1])
print('2011:  ', df_2011['w_cfs'].value_counts()[1])
print('2012:  ', df_2012['w_cfs'].value_counts()[1])
print('2013:  ', df_2013['w_cfs'].value_counts()[1])
print('2014:  ', df_2014['w_cfs'].value_counts()[1])
print('2015:  ', df_2015['w_cfs'].value_counts()[1])
print('2016:  ', df_2016['w_cfs'].value_counts()[1])
print('2017:  ', df_2017['w_cfs'].value_counts()[1])
print('2018:  ', df_2018['w_cfs'].value_counts()[1])
print('2019:  ', df_2019['w_cfs'].value_counts()[1])

#print the median number of wind droughts
print('median:  ', statistics.median([df_2006['w_cfs'].value_counts()[1], df_2007['w_cfs'].value_counts()[1], df_2008['w_cfs'].value_counts()[1], df_2009['w_cfs'].value_counts()[1], df_2010['w_cfs'].value_counts()[1], df_2011['w_cfs'].value_counts()[1], df_2012['w_cfs'].value_counts()[1], df_2013['w_cfs'].value_counts()[1], df_2014['w_cfs'].value_counts()[1], df_2015['w_cfs'].value_counts()[1], df_2016['w_cfs'].value_counts()[1], df_2017['w_cfs'].value_counts()[1], df_2018['w_cfs'].value_counts()[1], df_2019['w_cfs'].value_counts()[1]]))

#print the mean number of wind droughts
print('mean:  ', statistics.mean([df_2006['w_cfs'].value_counts()[1], df_2007['w_cfs'].value_counts()[1], df_2008['w_cfs'].value_counts()[1], df_2009['w_cfs'].value_counts()[1], df_2010['w_cfs'].value_counts()[1], df_2011['w_cfs'].value_counts()[1], df_2012['w_cfs'].value_counts()[1], df_2013['w_cfs'].value_counts()[1], df_2014['w_cfs'].value_counts()[1], df_2015['w_cfs'].value_counts()[1], df_2016['w_cfs'].value_counts()[1], df_2017['w_cfs'].value_counts()[1], df_2018['w_cfs'].value_counts()[1], df_2019['w_cfs'].value_counts()[1]]))