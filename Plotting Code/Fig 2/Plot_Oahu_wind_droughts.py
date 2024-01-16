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
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    #print(df_2006)
#print the greatest number of consecutive days with wind capacity below 50% of the average


#determine if any year has 8 consecutive days with wind capacity below 50% of the average
for list in df_list:
    for i in range(362):
        if (list.loc[i,'w_cfs'] == 1) and (list.loc[i+1,'w_cfs'] == 1) and (list.loc[i+2,'w_cfs'] == 1) and (list.loc[i+3,'w_cfs'] == 1) and (list.loc[i+4,'w_cfs'] == 1) and (list.loc[i+5,'w_cfs'] == 1) and (list.loc[i+6,'w_cfs'] == 1) and (list.loc[i+7,'w_cfs'] == 1) and (list.loc[i+8,'w_cfs'] == 1) and (list.loc[i+9,'w_cfs'] == 1) and (list.loc[i+10,'w_cfs']==1) and (list.loc[i+11,'w_cfs']==1) and (list.loc[i+12,'w_cfs']==1)and (list.loc[i+13,'w_cfs']==1)and (list.loc[i+14,'w_cfs']==1)and (list.loc[i+15,'w_cfs']==1):
            print(list.mean())
print(df_2009.mean())

#Determine how many drought days df_2006 has. Sort by 1 consecutive day, 2 consecutive days, 3-6 consecutive days, and 7+ consecutive days
#Add the number of times the value 1 occurs with the value 0 occurring before and after it
for i in range(365):
    if (df_2006.loc[i, 'w_cfs'] == 1) and (df_2006.loc[i-1, 'w_cfs'] != 1):
        #Create a new column called drought_days and add the value 1 to that index position
        df_2006.loc[i, 'drought_starts'] = i
    else:
        df_2006.loc[i, 'drought_starts'] = 0
#add all nonzero values in the drought_starts column to a list called list2006
list2006 = df_2006['drought_starts'].tolist()
list2006 = [i for i in list2006 if i != 0]
#create columns in df_2006 named one_day_drought, two_day_drought, three_day_drought, four_day_drought, five_day_drought, six_day_drought, and seven_day_drought
df_2006['one_day_drought'] = 0
df_2006['two_day_drought'] = 0
df_2006['three_day_drought'] = 0
df_2006['four_day_drought'] = 0
df_2006['five_day_drought'] = 0
df_2006['six_day_drought'] = 0
df_2006['seven_day_drought'] = 0
for i in list2006:
    if (df_2006.loc[i, 'w_cfs'] == 1) and (df_2006.loc[i+1, 'w_cfs'] != 1):
        df_2006.loc[i, 'one_day_drought'] = 1
    elif (df_2006.loc[i, 'w_cfs'] == 1) and (df_2006.loc[i+1, 'w_cfs'] == 1) and (df_2006.loc[i+2, 'w_cfs'] != 1):
        df_2006.loc[i, 'two_day_drought'] = 1
    elif (df_2006.loc[i, 'w_cfs'] == 1) and (df_2006.loc[i+1, 'w_cfs'] == 1) and (df_2006.loc[i+2, 'w_cfs'] == 1) and (df_2006.loc[i+3, 'w_cfs'] != 1):
        df_2006.loc[i, 'three_day_drought'] = 1
    elif (df_2006.loc[i, 'w_cfs'] == 1) and (df_2006.loc[i+1, 'w_cfs'] == 1) and (df_2006.loc[i+2, 'w_cfs'] == 1) and (df_2006.loc[i+3, 'w_cfs'] == 1) and (df_2006.loc[i+4, 'w_cfs'] != 1):
        df_2006.loc[i, 'four_day_drought'] = 1
    elif (df_2006.loc[i, 'w_cfs'] == 1) and (df_2006.loc[i+1, 'w_cfs'] == 1) and (df_2006.loc[i+2, 'w_cfs'] == 1) and (df_2006.loc[i+3, 'w_cfs'] == 1) and (df_2006.loc[i+4, 'w_cfs'] == 1) and (df_2006.loc[i+5, 'w_cfs'] != 1):
        df_2006.loc[i, 'five_day_drought'] = 1
    elif (df_2006.loc[i, 'w_cfs'] == 1) and (df_2006.loc[i+1, 'w_cfs'] == 1) and (df_2006.loc[i+2, 'w_cfs'] == 1) and (df_2006.loc[i+3, 'w_cfs'] == 1) and (df_2006.loc[i+4, 'w_cfs'] == 1) and (df_2006.loc[i+5, 'w_cfs'] == 1) and (df_2006.loc[i+6, 'w_cfs'] != 1):
        df_2006.loc[i, 'six_day_drought'] = 1
    else:
        df_2006.loc[i, 'seven_day_drought'] = 1

list_1day2006 = df_2006['one_day_drought'].tolist()
list_2day2006 = df_2006['two_day_drought'].tolist()
list_3day2006 = df_2006['three_day_drought'].tolist()
list_4day2006 = df_2006['four_day_drought'].tolist()
list_5day2006 = df_2006['five_day_drought'].tolist()
list_6day2006 = df_2006['six_day_drought'].tolist()
list_7day2006 = df_2006['seven_day_drought'].tolist()

#count the number of times the value 1 occurs in the list
list_1day2006 = list_1day2006.count(1)
list_2day2006 = list_2day2006.count(1)
list_3day2006 = list_3day2006.count(1)
list_4day2006 = list_4day2006.count(1)
list_5day2006 = list_5day2006.count(1)
list_6day2006 = list_6day2006.count(1)
list_7day2006 = list_7day2006.count(1)

#2007
for i in range(365):
    if (df_2007.loc[i, 'w_cfs'] == 1) and (df_2007.loc[i-1, 'w_cfs'] != 1):
        #Create a new column called drought_days and add the value 1 to that index position
        df_2007.loc[i, 'drought_starts'] = i
    else:
        df_2007.loc[i, 'drought_starts'] = 0
list2007 = df_2007['drought_starts'].tolist()
list2007 = [i for i in list2007 if i != 0]
#create columns in df_2007 named one_day_drought, two_day_drought, three_day_drought, four_day_drought, five_day_drought, six_day_drought, seven_day_drought
df_2007['one_day_drought'] = 0
df_2007['two_day_drought'] = 0
df_2007['three_day_drought'] = 0
df_2007['four_day_drought'] = 0
df_2007['five_day_drought'] = 0
df_2007['six_day_drought'] = 0
df_2007['seven_day_drought'] = 0

for i in list2007:
    if (df_2007.loc[i, 'w_cfs'] == 1) and (df_2007.loc[i+1, 'w_cfs'] != 1):
        df_2007.loc[i, 'one_day_drought'] = 1
    elif (df_2007.loc[i, 'w_cfs'] == 1) and (df_2007.loc[i+1, 'w_cfs'] == 1) and (df_2007.loc[i+2, 'w_cfs'] != 1):
        df_2007.loc[i, 'two_day_drought'] = 1
    elif (df_2007.loc[i, 'w_cfs'] == 1) and (df_2007.loc[i+1, 'w_cfs'] == 1) and (df_2007.loc[i+2, 'w_cfs'] == 1) and (df_2007.loc[i+3, 'w_cfs'] != 1):
        df_2007.loc[i, 'three_day_drought'] = 1
    elif (df_2007.loc[i, 'w_cfs'] == 1) and (df_2007.loc[i+1, 'w_cfs'] == 1) and (df_2007.loc[i+2, 'w_cfs'] == 1) and (df_2007.loc[i+3, 'w_cfs'] == 1) and (df_2007.loc[i+4, 'w_cfs'] != 1):
        df_2007.loc[i, 'four_day_drought'] = 1
    elif (df_2007.loc[i, 'w_cfs'] == 1) and (df_2007.loc[i+1, 'w_cfs'] == 1) and (df_2007.loc[i+2, 'w_cfs'] == 1) and (df_2007.loc[i+3, 'w_cfs'] == 1) and (df_2007.loc[i+4, 'w_cfs'] == 1) and (df_2007.loc[i+5, 'w_cfs'] != 1):
        df_2007.loc[i, 'five_day_drought'] = 1
    elif (df_2007.loc[i, 'w_cfs'] == 1) and (df_2007.loc[i+1, 'w_cfs'] == 1) and (df_2007.loc[i+2, 'w_cfs'] == 1) and (df_2007.loc[i+3, 'w_cfs'] == 1) and (df_2007.loc[i+4, 'w_cfs'] == 1) and (df_2007.loc[i+5, 'w_cfs'] == 1) and (df_2007.loc[i+6, 'w_cfs'] != 1):
        df_2007.loc[i, 'six_day_drought'] = 1
    else:
        df_2007.loc[i, 'seven_day_drought'] = 1

list_1day2007 = df_2007['one_day_drought'].tolist()
list_2day2007 = df_2007['two_day_drought'].tolist()
list_3day2007 = df_2007['three_day_drought'].tolist()
list_4day2007 = df_2007['four_day_drought'].tolist()
list_5day2007 = df_2007['five_day_drought'].tolist()
list_6day2007 = df_2007['six_day_drought'].tolist()
list_7day2007 = df_2007['seven_day_drought'].tolist()

#count the number of times the value 1 occurs in the list
list_1day2007 = list_1day2007.count(1)
list_2day2007 = list_2day2007.count(1)
list_3day2007 = list_3day2007.count(1)
list_4day2007 = list_4day2007.count(1)
list_5day2007 = list_5day2007.count(1)
list_6day2007 = list_6day2007.count(1)
list_7day2007 = list_7day2007.count(1)

#2008
for i in range(366):
    if (df_2008.loc[i, 'w_cfs'] == 1) and (df_2008.loc[i-1, 'w_cfs'] != 1):
        #Create a new column called drought_days and add the value 1 to that index position
        df_2008.loc[i, 'drought_starts'] = i
    else:
        df_2008.loc[i, 'drought_starts'] = 0
list2008 = df_2008['drought_starts'].tolist()
list2008 = [i for i in list2008 if i != 0]
#create columns in df_2008 named one_day_drought, two_day_drought, three_day_drought, four_day_drought, five_day_drought, six_day_drought, seven_day_drought
df_2008['one_day_drought'] = 0
df_2008['two_day_drought'] = 0
df_2008['three_day_drought'] = 0
df_2008['four_day_drought'] = 0
df_2008['five_day_drought'] = 0
df_2008['six_day_drought'] = 0
df_2008['seven_day_drought'] = 0
for i in list2008:
    if (df_2008.loc[i, 'w_cfs'] == 1) and (df_2008.loc[i+1, 'w_cfs'] != 1):
        df_2008.loc[i, 'one_day_drought'] = 1
    elif (df_2008.loc[i, 'w_cfs'] == 1) and (df_2008.loc[i+1, 'w_cfs'] == 1) and (df_2008.loc[i+2, 'w_cfs'] != 1):
        df_2008.loc[i, 'two_day_drought'] = 1
    elif (df_2008.loc[i, 'w_cfs'] == 1) and (df_2008.loc[i+1, 'w_cfs'] == 1) and (df_2008.loc[i+2, 'w_cfs'] == 1) and (df_2008.loc[i+3, 'w_cfs'] != 1):
        df_2008.loc[i, 'three_day_drought'] = 1
    elif (df_2008.loc[i, 'w_cfs'] == 1) and (df_2008.loc[i+1, 'w_cfs'] == 1) and (df_2008.loc[i+2, 'w_cfs'] == 1) and (df_2008.loc[i+3, 'w_cfs'] == 1) and (df_2008.loc[i+4, 'w_cfs'] != 1):
        df_2008.loc[i, 'four_day_drought'] = 1
    elif (df_2008.loc[i, 'w_cfs'] == 1) and (df_2008.loc[i+1, 'w_cfs'] == 1) and (df_2008.loc[i+2, 'w_cfs'] == 1) and (df_2008.loc[i+3, 'w_cfs'] == 1) and (df_2008.loc[i+4, 'w_cfs'] == 1) and (df_2008.loc[i+5, 'w_cfs'] != 1):
        df_2008.loc[i, 'five_day_drought'] = 1
    elif (df_2008.loc[i, 'w_cfs'] == 1) and (df_2008.loc[i+1, 'w_cfs'] == 1) and (df_2008.loc[i+2, 'w_cfs'] == 1) and (df_2008.loc[i+3, 'w_cfs'] == 1) and (df_2008.loc[i+4, 'w_cfs'] == 1) and (df_2008.loc[i+5, 'w_cfs'] == 1) and (df_2008.loc[i+6, 'w_cfs'] != 1):
        df_2008.loc[i, 'six_day_drought'] = 1
    else:
        df_2008.loc[i, 'seven_day_drought'] = 1

list_1day2008 = df_2008['one_day_drought'].tolist()
list_2day2008 = df_2008['two_day_drought'].tolist()
list_3day2008 = df_2008['three_day_drought'].tolist()
list_4day2008 = df_2008['four_day_drought'].tolist()
list_5day2008 = df_2008['five_day_drought'].tolist()
list_6day2008 = df_2008['six_day_drought'].tolist()
list_7day2008 = df_2008['seven_day_drought'].tolist()

#count the number of times the value 1 occurs in the list
list_1day2008 = list_1day2008.count(1)
list_2day2008 = list_2day2008.count(1)
list_3day2008 = list_3day2008.count(1)
list_4day2008 = list_4day2008.count(1)
list_5day2008 = list_5day2008.count(1)
list_6day2008 = list_6day2008.count(1)
list_7day2008 = list_7day2008.count(1)

#2009
df_2009.loc[-1] = 0  # adding a row
df_2009 = df_2009.sort_index()  # sorting by index
df_2009 = df_2009.reset_index(drop=True)
df_2009.loc[366] = 0 #added extra day with 0 drought to end of df_2012 because code can't handle final day ending on drought
df_2009 = df_2009.sort_index()

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df_2009)
for i in range(367):
    if (df_2009.loc[i, 'w_cfs'] == 1) and (df_2009.loc[i-1, 'w_cfs'] != 1):
        #Create a new column called drought_days and add the value 1 to that index position
        df_2009.loc[i, 'drought_starts'] = i
    else:
        df_2009.loc[i, 'drought_starts'] = 0
list2009 = df_2009['drought_starts'].tolist()
list2009 = [i for i in list2009 if i != 0]
#create columns in df_2009 named one_day_drought, two_day_drought, three_day_drought, four_day_drought, five_day_drought, six_day_drought, seven_day_drought
df_2009['one_day_drought'] = 0
df_2009['two_day_drought'] = 0
df_2009['three_day_drought'] = 0
df_2009['four_day_drought'] = 0
df_2009['five_day_drought'] = 0
df_2009['six_day_drought'] = 0
df_2009['seven_day_drought'] = 0
for i in list2009:
    if (df_2009.loc[i, 'w_cfs'] == 1) and (df_2009.loc[i+1, 'w_cfs'] != 1):
        df_2009.loc[i, 'one_day_drought'] = 1
    elif (df_2009.loc[i, 'w_cfs'] == 1) and (df_2009.loc[i+1, 'w_cfs'] == 1) and (df_2009.loc[i+2, 'w_cfs'] != 1):
        df_2009.loc[i, 'two_day_drought'] = 1
    elif (df_2009.loc[i, 'w_cfs'] == 1) and (df_2009.loc[i+1, 'w_cfs'] == 1) and (df_2009.loc[i+2, 'w_cfs'] == 1) and (df_2009.loc[i+3, 'w_cfs'] != 1):
        df_2009.loc[i, 'three_day_drought'] = 1
    elif (df_2009.loc[i, 'w_cfs'] == 1) and (df_2009.loc[i+1, 'w_cfs'] == 1) and (df_2009.loc[i+2, 'w_cfs'] == 1) and (df_2009.loc[i+3, 'w_cfs'] == 1) and (df_2009.loc[i+4, 'w_cfs'] != 1):
        df_2009.loc[i, 'four_day_drought'] = 1
    elif (df_2009.loc[i, 'w_cfs'] == 1) and (df_2009.loc[i+1, 'w_cfs'] == 1) and (df_2009.loc[i+2, 'w_cfs'] == 1) and (df_2009.loc[i+3, 'w_cfs'] == 1) and (df_2009.loc[i+4, 'w_cfs'] == 1) and (df_2009.loc[i+5, 'w_cfs'] != 1):
        df_2009.loc[i, 'five_day_drought'] = 1
    elif (df_2009.loc[i, 'w_cfs'] == 1) and (df_2009.loc[i+1, 'w_cfs'] == 1) and (df_2009.loc[i+2, 'w_cfs'] == 1) and (df_2009.loc[i+3, 'w_cfs'] == 1) and (df_2009.loc[i+4, 'w_cfs'] == 1) and (df_2009.loc[i+5, 'w_cfs'] == 1) and (df_2009.loc[i+6, 'w_cfs'] != 1):
        df_2009.loc[i, 'six_day_drought'] = 1
    else:
        df_2009.loc[i, 'seven_day_drought'] = 1

list_1day2009 = df_2009['one_day_drought'].tolist()
list_2day2009 = df_2009['two_day_drought'].tolist()
list_3day2009 = df_2009['three_day_drought'].tolist()
list_4day2009 = df_2009['four_day_drought'].tolist()
list_5day2009 = df_2009['five_day_drought'].tolist()
list_6day2009 = df_2009['six_day_drought'].tolist()
list_7day2009 = df_2009['seven_day_drought'].tolist()

#count the number of times the value 1 occurs in the list
list_1day2009 = list_1day2009.count(1)
list_2day2009 = list_2day2009.count(1)
list_3day2009 = list_3day2009.count(1)
list_4day2009 = list_4day2009.count(1)
list_5day2009 = list_5day2009.count(1)
list_6day2009 = list_6day2009.count(1)
list_7day2009 = list_7day2009.count(1)

#2010
for i in range (365):
    if (df_2010.loc[i, 'w_cfs'] == 1) and (df_2010.loc[i-1, 'w_cfs'] != 1):
        #Create a new column called drought_days and add the value 1 to that index position
        df_2010.loc[i, 'drought_starts'] = i
    else:
        df_2010.loc[i, 'drought_starts'] = 0
list2010 = df_2010['drought_starts'].tolist()
list2010 = [i for i in list2010 if i != 0]
#create columns in df_2010 named one_day_drought, two_day_drought, three_day_drought, four_day_drought, five_day_drought, six_day_drought, seven_day_drought
df_2010['one_day_drought'] = 0
df_2010['two_day_drought'] = 0
df_2010['three_day_drought'] = 0
df_2010['four_day_drought'] = 0
df_2010['five_day_drought'] = 0
df_2010['six_day_drought'] = 0
df_2010['seven_day_drought'] = 0
for i in list2010:
    if (df_2010.loc[i, 'w_cfs'] == 1) and (df_2010.loc[i+1, 'w_cfs'] != 1):
        df_2010.loc[i, 'one_day_drought'] = 1
    elif (df_2010.loc[i, 'w_cfs'] == 1) and (df_2010.loc[i+1, 'w_cfs'] == 1) and (df_2010.loc[i+2, 'w_cfs'] != 1):
        df_2010.loc[i, 'two_day_drought'] = 1
    elif (df_2010.loc[i, 'w_cfs'] == 1) and (df_2010.loc[i+1, 'w_cfs'] == 1) and (df_2010.loc[i+2, 'w_cfs'] == 1) and (df_2010.loc[i+3, 'w_cfs'] != 1):
        df_2010.loc[i, 'three_day_drought'] = 1
    elif (df_2010.loc[i, 'w_cfs'] == 1) and (df_2010.loc[i+1, 'w_cfs'] == 1) and (df_2010.loc[i+2, 'w_cfs'] == 1) and (df_2010.loc[i+3, 'w_cfs'] == 1) and (df_2010.loc[i+4, 'w_cfs'] != 1):
        df_2010.loc[i, 'four_day_drought'] = 1
    elif (df_2010.loc[i, 'w_cfs'] == 1) and (df_2010.loc[i+1, 'w_cfs'] == 1) and (df_2010.loc[i+2, 'w_cfs'] == 1) and (df_2010.loc[i+3, 'w_cfs'] == 1) and (df_2010.loc[i+4, 'w_cfs'] == 1) and (df_2010.loc[i+5, 'w_cfs'] != 1):
        df_2010.loc[i, 'five_day_drought'] = 1
    elif (df_2010.loc[i, 'w_cfs'] == 1) and (df_2010.loc[i+1, 'w_cfs'] == 1) and (df_2010.loc[i+2, 'w_cfs'] == 1) and (df_2010.loc[i+3, 'w_cfs'] == 1) and (df_2010.loc[i+4, 'w_cfs'] == 1) and (df_2010.loc[i+5, 'w_cfs'] == 1) and (df_2010.loc[i+6, 'w_cfs'] != 1):
        df_2010.loc[i, 'six_day_drought'] = 1
    else:
        df_2010.loc[i, 'seven_day_drought'] = 1

list_1day2010 = df_2010['one_day_drought'].tolist()
list_2day2010 = df_2010['two_day_drought'].tolist()
list_3day2010 = df_2010['three_day_drought'].tolist()
list_4day2010 = df_2010['four_day_drought'].tolist()
list_5day2010 = df_2010['five_day_drought'].tolist()
list_6day2010 = df_2010['six_day_drought'].tolist()
list_7day2010 = df_2010['seven_day_drought'].tolist()

#count the number of times the value 1 occurs in the list
list_1day2010 = list_1day2010.count(1)
list_2day2010 = list_2day2010.count(1)
list_3day2010 = list_3day2010.count(1)
list_4day2010 = list_4day2010.count(1)
list_5day2010 = list_5day2010.count(1)
list_6day2010 = list_6day2010.count(1)
list_7day2010 = list_7day2010.count(1)

''' Adding a row with zero drought at the start and end of 2011 since the code cant handle 1 at the start or end'''
df_2011.loc[-1] = 0  # adding a row
df_2011 = df_2011.sort_index()  # sorting by index
#re-index the dataframe to start at 0
df_2011 = df_2011.reset_index(drop=True)

df_2011.loc[366] = 0 #added extra day with 0 drought to end of df_2012 because code can't handle final day ending on drought
df_2011 = df_2011.sort_index()
for i in range (367):
    if (df_2011.loc[i, 'w_cfs'] == 1) and (df_2011.loc[i-1, 'w_cfs'] != 1):
        #Create a new column called drought_days and add the value 1 to that index position
        df_2011.loc[i, 'drought_starts'] = i
    else:
        df_2011.loc[i, 'drought_starts'] = 0
list2011 = df_2011['drought_starts'].tolist()
list2011 = [i for i in list2011 if i != 0]

#create columns in df_2011 named one_day_drought, two_day_drought, three_day_drought, four_day_drought, five_day_drought, six_day_drought, seven_day_drought
df_2011['one_day_drought'] = 0
df_2011['two_day_drought'] = 0
df_2011['three_day_drought'] = 0
df_2011['four_day_drought'] = 0
df_2011['five_day_drought'] = 0
df_2011['six_day_drought'] = 0
df_2011['seven_day_drought'] = 0
for i in list2011:
    if (df_2011.loc[i, 'w_cfs'] == 1) and (df_2011.loc[i+1, 'w_cfs'] != 1):
        df_2011.loc[i, 'one_day_drought'] = 1
    elif (df_2011.loc[i, 'w_cfs'] == 1) and (df_2011.loc[i+1, 'w_cfs'] == 1) and (df_2011.loc[i+2, 'w_cfs'] != 1):
        df_2011.loc[i, 'two_day_drought'] = 1
    elif (df_2011.loc[i, 'w_cfs'] == 1) and (df_2011.loc[i+1, 'w_cfs'] == 1) and (df_2011.loc[i+2, 'w_cfs'] == 1) and (df_2011.loc[i+3, 'w_cfs'] != 1):
        df_2011.loc[i, 'three_day_drought'] = 1
    elif (df_2011.loc[i, 'w_cfs'] == 1) and (df_2011.loc[i+1, 'w_cfs'] == 1) and (df_2011.loc[i+2, 'w_cfs'] == 1) and (df_2011.loc[i+3, 'w_cfs'] == 1) and (df_2011.loc[i+4, 'w_cfs'] != 1):
        df_2011.loc[i, 'four_day_drought'] = 1
    elif (df_2011.loc[i, 'w_cfs'] == 1) and (df_2011.loc[i+1, 'w_cfs'] == 1) and (df_2011.loc[i+2, 'w_cfs'] == 1) and (df_2011.loc[i+3, 'w_cfs'] == 1) and (df_2011.loc[i+4, 'w_cfs'] == 1) and (df_2011.loc[i+5, 'w_cfs'] != 1):
        df_2011.loc[i, 'five_day_drought'] = 1
    elif (df_2011.loc[i, 'w_cfs'] == 1) and (df_2011.loc[i+1, 'w_cfs'] == 1) and (df_2011.loc[i+2, 'w_cfs'] == 1) and (df_2011.loc[i+3, 'w_cfs'] == 1) and (df_2011.loc[i+4, 'w_cfs'] == 1) and (df_2011.loc[i+5, 'w_cfs'] == 1) and (df_2011.loc[i+6, 'w_cfs'] != 1):
        df_2011.loc[i, 'six_day_drought'] = 1
    else:
        df_2011.loc[i, 'seven_day_drought'] = 1

list_1day2011 = df_2011['one_day_drought'].tolist()
list_2day2011 = df_2011['two_day_drought'].tolist()
list_3day2011 = df_2011['three_day_drought'].tolist()
list_4day2011 = df_2011['four_day_drought'].tolist()
list_5day2011 = df_2011['five_day_drought'].tolist()
list_6day2011 = df_2011['six_day_drought'].tolist()
list_7day2011 = df_2011['seven_day_drought'].tolist()

#count the number of times the value 1 occurs in the list
list_1day2011 = list_1day2011.count(1)
list_2day2011 = list_2day2011.count(1)
list_3day2011 = list_3day2011.count(1)
list_4day2011 = list_4day2011.count(1)
list_5day2011 = list_5day2011.count(1)
list_6day2011 = list_6day2011.count(1)
list_7day2011 = list_7day2011.count(1)


#2012
df_2012.loc[366] = 0 #added extra day with 0 drought to end of df_2012 because code can't handle final day ending on drought
df_2012 = df_2012.sort_index()

for i in range (367):
    if (df_2012.loc[i, 'w_cfs'] == 1) and (df_2012.loc[i-1, 'w_cfs'] != 1):
        #Create a new column called drought_days and add the value 1 to that index position
        df_2012.loc[i, 'drought_starts'] = i
    else:
        df_2012.loc[i, 'drought_starts'] = 0
list2012 = df_2012['drought_starts'].tolist()
list2012 = [i for i in list2012 if i != 0]
#create columns in df_2012 named one_day_drought, two_day_drought, three_day_drought, four_day_drought, five_day_drought, six_day_drought, seven_day_drought
df_2012['one_day_drought'] = 0
df_2012['two_day_drought'] = 0
df_2012['three_day_drought'] = 0
df_2012['four_day_drought'] = 0
df_2012['five_day_drought'] = 0
df_2012['six_day_drought'] = 0
df_2012['seven_day_drought'] = 0
for i in list2012:
    if (df_2012.loc[i, 'w_cfs'] == 1) and (df_2012.loc[i+1, 'w_cfs'] != 1):
        df_2012.loc[i, 'one_day_drought'] = 1
    elif (df_2012.loc[i, 'w_cfs'] == 1) and (df_2012.loc[i+1, 'w_cfs'] == 1) and (df_2012.loc[i+2, 'w_cfs'] != 1):
        df_2012.loc[i, 'two_day_drought'] = 1
    elif (df_2012.loc[i, 'w_cfs'] == 1) and (df_2012.loc[i+1, 'w_cfs'] == 1) and (df_2012.loc[i+2, 'w_cfs'] == 1) and (df_2012.loc[i+3, 'w_cfs'] != 1):
        df_2012.loc[i, 'three_day_drought'] = 1
    elif (df_2012.loc[i, 'w_cfs'] == 1) and (df_2012.loc[i+1, 'w_cfs'] == 1) and (df_2012.loc[i+2, 'w_cfs'] == 1) and (df_2012.loc[i+3, 'w_cfs'] == 1) and (df_2012.loc[i+4, 'w_cfs'] != 1):
        df_2012.loc[i, 'four_day_drought'] = 1
    elif (df_2012.loc[i, 'w_cfs'] == 1) and (df_2012.loc[i+1, 'w_cfs'] == 1) and (df_2012.loc[i+2, 'w_cfs'] == 1) and (df_2012.loc[i+3, 'w_cfs'] == 1) and (df_2012.loc[i+4, 'w_cfs'] == 1) and (df_2012.loc[i+5, 'w_cfs'] != 1):
        df_2012.loc[i, 'five_day_drought'] = 1
    elif (df_2012.loc[i, 'w_cfs'] == 1) and (df_2012.loc[i+1, 'w_cfs'] == 1) and (df_2012.loc[i+2, 'w_cfs'] == 1) and (df_2012.loc[i+3, 'w_cfs'] == 1) and (df_2012.loc[i+4, 'w_cfs'] == 1) and (df_2012.loc[i+5, 'w_cfs'] == 1) and (df_2012.loc[i+6, 'w_cfs'] != 1):
        df_2012.loc[i, 'six_day_drought'] = 1
    else:
        df_2012.loc[i, 'seven_day_drought'] = 1

list_1day2012 = df_2012['one_day_drought'].tolist()
list_2day2012 = df_2012['two_day_drought'].tolist()
list_3day2012 = df_2012['three_day_drought'].tolist()
list_4day2012 = df_2012['four_day_drought'].tolist()
list_5day2012 = df_2012['five_day_drought'].tolist()
list_6day2012 = df_2012['six_day_drought'].tolist()
list_7day2012 = df_2012['seven_day_drought'].tolist()

#count the number of times the value 1 occurs in the list
list_1day2012 = list_1day2012.count(1)
list_2day2012 = list_2day2012.count(1)
list_3day2012 = list_3day2012.count(1)
list_4day2012 = list_4day2012.count(1)
list_5day2012 = list_5day2012.count(1)
list_6day2012 = list_6day2012.count(1)
list_7day2012 = list_7day2012.count(1)

#2013
for i in range (365):
    if (df_2013.loc[i, 'w_cfs'] == 1) and (df_2013.loc[i-1, 'w_cfs'] != 1):
        #Create a new column called drought_days and add the value 1 to that index position
        df_2013.loc[i, 'drought_starts'] = i
    else:
        df_2013.loc[i, 'drought_starts'] = 0
list2013 = df_2013['drought_starts'].tolist()
list2013 = [i for i in list2013 if i != 0]
#create columns in df_2013 named one_day_drought, two_day_drought, three_day_drought, four_day_drought, five_day_drought, six_day_drought, seven_day_drought
df_2013['one_day_drought'] = 0
df_2013['two_day_drought'] = 0
df_2013['three_day_drought'] = 0
df_2013['four_day_drought'] = 0
df_2013['five_day_drought'] = 0
df_2013['six_day_drought'] = 0
df_2013['seven_day_drought'] = 0

for i in list2013:
    if (df_2013.loc[i, 'w_cfs'] == 1) and (df_2013.loc[i+1, 'w_cfs'] != 1):
        df_2013.loc[i, 'one_day_drought'] = 1
    elif (df_2013.loc[i, 'w_cfs'] == 1) and (df_2013.loc[i+1, 'w_cfs'] == 1) and (df_2013.loc[i+2, 'w_cfs'] != 1):
        df_2013.loc[i, 'two_day_drought'] = 1
    elif (df_2013.loc[i, 'w_cfs'] == 1) and (df_2013.loc[i+1, 'w_cfs'] == 1) and (df_2013.loc[i+2, 'w_cfs'] == 1) and (df_2013.loc[i+3, 'w_cfs'] != 1):
        df_2013.loc[i, 'three_day_drought'] = 1
    elif (df_2013.loc[i, 'w_cfs'] == 1) and (df_2013.loc[i+1, 'w_cfs'] == 1) and (df_2013.loc[i+2, 'w_cfs'] == 1) and (df_2013.loc[i+3, 'w_cfs'] == 1) and (df_2013.loc[i+4, 'w_cfs'] != 1):
        df_2013.loc[i, 'four_day_drought'] = 1
    elif (df_2013.loc[i, 'w_cfs'] == 1) and (df_2013.loc[i+1, 'w_cfs'] == 1) and (df_2013.loc[i+2, 'w_cfs'] == 1) and (df_2013.loc[i+3, 'w_cfs'] == 1) and (df_2013.loc[i+4, 'w_cfs'] == 1) and (df_2013.loc[i+5, 'w_cfs'] != 1):
        df_2013.loc[i, 'five_day_drought'] = 1
    elif (df_2013.loc[i, 'w_cfs'] == 1) and (df_2013.loc[i+1, 'w_cfs'] == 1) and (df_2013.loc[i+2, 'w_cfs'] == 1) and (df_2013.loc[i+3, 'w_cfs'] == 1) and (df_2013.loc[i+4, 'w_cfs'] == 1) and (df_2013.loc[i+5, 'w_cfs'] == 1) and (df_2013.loc[i+6, 'w_cfs'] != 1):
        df_2013.loc[i, 'six_day_drought'] = 1
    else:
        df_2013.loc[i, 'seven_day_drought'] = 1

list_1day2013 = df_2013['one_day_drought'].tolist()
list_2day2013 = df_2013['two_day_drought'].tolist()
list_3day2013 = df_2013['three_day_drought'].tolist()
list_4day2013 = df_2013['four_day_drought'].tolist()
list_5day2013 = df_2013['five_day_drought'].tolist()
list_6day2013 = df_2013['six_day_drought'].tolist()
list_7day2013 = df_2013['seven_day_drought'].tolist()

#count the number of times the value 1 occurs in the list
list_1day2013 = list_1day2013.count(1)
list_2day2013 = list_2day2013.count(1)
list_3day2013 = list_3day2013.count(1)
list_4day2013 = list_4day2013.count(1)
list_5day2013 = list_5day2013.count(1)
list_6day2013 = list_6day2013.count(1)
list_7day2013 = list_7day2013.count(1)

#2014
df_2014.loc[-1] = 0  # adding a row
df_2014 = df_2014.sort_index()  # sorting by index
#re-index the dataframe to start at 0
df_2014 = df_2014.reset_index(drop=True)
for i in range (366):
    if (df_2014.loc[i, 'w_cfs'] == 1) and (df_2014.loc[i-1, 'w_cfs'] != 1):
        #Create a new column called drought_days and add the value 1 to that index position
        df_2014.loc[i, 'drought_starts'] = i
    else:
        df_2014.loc[i, 'drought_starts'] = 0
list2014 = df_2014['drought_starts'].tolist()
list2014 = [i for i in list2014 if i != 0]
#create columns in df_2014 named one_day_drought, two_day_drought, three_day_drought, four_day_drought, five_day_drought, six_day_drought, seven_day_drought
df_2014['one_day_drought'] = 0
df_2014['two_day_drought'] = 0
df_2014['three_day_drought'] = 0
df_2014['four_day_drought'] = 0
df_2014['five_day_drought'] = 0
df_2014['six_day_drought'] = 0
df_2014['seven_day_drought'] = 0

for i in list2014:
    if (df_2014.loc[i, 'w_cfs'] == 1) and (df_2014.loc[i+1, 'w_cfs'] != 1):
        df_2014.loc[i, 'one_day_drought'] = 1
    elif (df_2014.loc[i, 'w_cfs'] == 1) and (df_2014.loc[i+1, 'w_cfs'] == 1) and (df_2014.loc[i+2, 'w_cfs'] != 1):
        df_2014.loc[i, 'two_day_drought'] = 1
    elif (df_2014.loc[i, 'w_cfs'] == 1) and (df_2014.loc[i+1, 'w_cfs'] == 1) and (df_2014.loc[i+2, 'w_cfs'] == 1) and (df_2014.loc[i+3, 'w_cfs'] != 1):
        df_2014.loc[i, 'three_day_drought'] = 1
    elif (df_2014.loc[i, 'w_cfs'] == 1) and (df_2014.loc[i+1, 'w_cfs'] == 1) and (df_2014.loc[i+2, 'w_cfs'] == 1) and (df_2014.loc[i+3, 'w_cfs'] == 1) and (df_2014.loc[i+4, 'w_cfs'] != 1):
        df_2014.loc[i, 'four_day_drought'] = 1
    elif (df_2014.loc[i, 'w_cfs'] == 1) and (df_2014.loc[i+1, 'w_cfs'] == 1) and (df_2014.loc[i+2, 'w_cfs'] == 1) and (df_2014.loc[i+3, 'w_cfs'] == 1) and (df_2014.loc[i+4, 'w_cfs'] == 1) and (df_2014.loc[i+5, 'w_cfs'] != 1):
        df_2014.loc[i, 'five_day_drought'] = 1
    elif (df_2014.loc[i, 'w_cfs'] == 1) and (df_2014.loc[i+1, 'w_cfs'] == 1) and (df_2014.loc[i+2, 'w_cfs'] == 1) and (df_2014.loc[i+3, 'w_cfs'] == 1) and (df_2014.loc[i+4, 'w_cfs'] == 1) and (df_2014.loc[i+5, 'w_cfs'] == 1) and (df_2013.loc[i+6, 'w_cfs'] != 1):
        df_2014.loc[i, 'six_day_drought'] = 1
    else:
        df_2014.loc[i, 'seven_day_drought'] = 1

list_1day2014 = df_2014['one_day_drought'].tolist()
list_2day2014 = df_2014['two_day_drought'].tolist()
list_3day2014 = df_2014['three_day_drought'].tolist()
list_4day2014 = df_2014['four_day_drought'].tolist()
list_5day2014 = df_2014['five_day_drought'].tolist()
list_6day2014 = df_2014['six_day_drought'].tolist()
list_7day2014 = df_2014['seven_day_drought'].tolist()

#count the number of times the value 1 occurs in the list
list_1day2014 = list_1day2014.count(1)
list_2day2014 = list_2day2014.count(1)
list_3day2014 = list_3day2014.count(1)
list_4day2014 = list_4day2014.count(1)
list_5day2014 = list_5day2014.count(1)
list_6day2014 = list_6day2014.count(1)
list_7day2014 = list_7day2014.count(1)


#2015
for i in range (365):
    if (df_2015.loc[i, 'w_cfs'] == 1) and (df_2015.loc[i-1, 'w_cfs'] != 1):
        #Create a new column called drought_days and add the value 1 to that index position
        df_2015.loc[i, 'drought_starts'] = i
    else:
        df_2015.loc[i, 'drought_starts'] = 0
list2015 = df_2015['drought_starts'].tolist()
list2015 = [i for i in list2015 if i != 0]
#create columns in df_2015 named one_day_drought, two_day_drought, three_day_drought, four_day_drought, five_day_drought, six_day_drought, seven_day_drought
df_2015['one_day_drought'] = 0
df_2015['two_day_drought'] = 0
df_2015['three_day_drought'] = 0
df_2015['four_day_drought'] = 0
df_2015['five_day_drought'] = 0
df_2015['six_day_drought'] = 0
df_2015['seven_day_drought'] = 0

for i in list2015:
    if (df_2015.loc[i, 'w_cfs'] == 1) and (df_2015.loc[i+1, 'w_cfs'] != 1):
        df_2015.loc[i, 'one_day_drought'] = 1
    elif (df_2015.loc[i, 'w_cfs'] == 1) and (df_2015.loc[i+1, 'w_cfs'] == 1) and (df_2015.loc[i+2, 'w_cfs'] != 1):
        df_2015.loc[i, 'two_day_drought'] = 1
    elif (df_2015.loc[i, 'w_cfs'] == 1) and (df_2015.loc[i+1, 'w_cfs'] == 1) and (df_2015.loc[i+2, 'w_cfs'] == 1) and (df_2015.loc[i+3, 'w_cfs'] != 1):
        df_2015.loc[i, 'three_day_drought'] = 1
    elif (df_2015.loc[i, 'w_cfs'] == 1) and (df_2015.loc[i+1, 'w_cfs'] == 1) and (df_2015.loc[i+2, 'w_cfs'] == 1) and (df_2015.loc[i+3, 'w_cfs'] == 1) and (df_2015.loc[i+4, 'w_cfs'] != 1):
        df_2015.loc[i, 'four_day_drought'] = 1
    elif (df_2015.loc[i, 'w_cfs'] == 1) and (df_2015.loc[i+1, 'w_cfs'] == 1) and (df_2015.loc[i+2, 'w_cfs'] == 1) and (df_2015.loc[i+3, 'w_cfs'] == 1) and (df_2015.loc[i+4, 'w_cfs'] == 1) and (df_2015.loc[i+5, 'w_cfs'] != 1):
        df_2015.loc[i, 'five_day_drought'] = 1
    elif (df_2015.loc[i, 'w_cfs'] == 1) and (df_2015.loc[i+1, 'w_cfs'] == 1) and (df_2015.loc[i+2, 'w_cfs'] == 1) and (df_2015.loc[i+3, 'w_cfs'] == 1) and (df_2015.loc[i+4, 'w_cfs'] == 1) and (df_2015.loc[i+5, 'w_cfs'] == 1) and (df_2015.loc[i+6, 'w_cfs'] != 1):
        df_2015.loc[i, 'six_day_drought'] = 1
    else:
        df_2015.loc[i, 'seven_day_drought'] = 1

list_1day2015 = df_2015['one_day_drought'].tolist()
list_2day2015 = df_2015['two_day_drought'].tolist()
list_3day2015 = df_2015['three_day_drought'].tolist()
list_4day2015 = df_2015['four_day_drought'].tolist()
list_5day2015 = df_2015['five_day_drought'].tolist()
list_6day2015 = df_2015['six_day_drought'].tolist()
list_7day2015 = df_2015['seven_day_drought'].tolist()

#count the number of times the value 1 occurs in the list
list_1day2015 = list_1day2015.count(1)
list_2day2015 = list_2day2015.count(1)
list_3day2015 = list_3day2015.count(1)
list_4day2015 = list_4day2015.count(1)
list_5day2015 = list_5day2015.count(1)
list_6day2015 = list_6day2015.count(1)
list_7day2015 = list_7day2015.count(1)


#2016
df_2016.loc[-1] = 0  # adding a row
df_2016 = df_2016.sort_index()  # sorting by index
#re-index the dataframe to start at 0
df_2016 = df_2016.reset_index(drop=True)
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    #print(df_2016)
for i in range (367):
    if (df_2016.loc[i, 'w_cfs'] == 1) and (df_2016.loc[i-1, 'w_cfs'] != 1):
        #Create a new column called drought_days and add the value 1 to that index position
        df_2016.loc[i, 'drought_starts'] = i
    else:
        df_2016.loc[i, 'drought_starts'] = 0
list2016 = df_2016['drought_starts'].tolist()
list2016 = [i for i in list2016 if i != 0]
#create columns in df_2016 named one_day_drought, two_day_drought, three_day_drought, four_day_drought, five_day_drought, six_day_drought, seven_day_drought
df_2016['one_day_drought'] = 0
df_2016['two_day_drought'] = 0
df_2016['three_day_drought'] = 0
df_2016['four_day_drought'] = 0
df_2016['five_day_drought'] = 0
df_2016['six_day_drought'] = 0
df_2016['seven_day_drought'] = 0

for i in list2016:
    if (df_2016.loc[i, 'w_cfs'] == 1) and (df_2016.loc[i+1, 'w_cfs'] != 1):
        df_2016.loc[i, 'one_day_drought'] = 1
    elif (df_2016.loc[i, 'w_cfs'] == 1) and (df_2016.loc[i+1, 'w_cfs'] == 1) and (df_2016.loc[i+2, 'w_cfs'] != 1):
        df_2016.loc[i, 'two_day_drought'] = 1
    elif (df_2016.loc[i, 'w_cfs'] == 1) and (df_2016.loc[i+1, 'w_cfs'] == 1) and (df_2016.loc[i+2, 'w_cfs'] == 1) and (df_2016.loc[i+3, 'w_cfs'] != 1):
        df_2016.loc[i, 'three_day_drought'] = 1
    elif (df_2016.loc[i, 'w_cfs'] == 1) and (df_2016.loc[i+1, 'w_cfs'] == 1) and (df_2016.loc[i+2, 'w_cfs'] == 1) and (df_2016.loc[i+3, 'w_cfs'] == 1) and (df_2016.loc[i+4, 'w_cfs'] != 1):
        df_2016.loc[i, 'four_day_drought'] = 1
    elif (df_2016.loc[i, 'w_cfs'] == 1) and (df_2016.loc[i+1, 'w_cfs'] == 1) and (df_2016.loc[i+2, 'w_cfs'] == 1) and (df_2016.loc[i+3, 'w_cfs'] == 1) and (df_2016.loc[i+4, 'w_cfs'] == 1) and (df_2016.loc[i+5, 'w_cfs'] != 1):
        df_2016.loc[i, 'five_day_drought'] = 1
    elif (df_2016.loc[i, 'w_cfs'] == 1) and (df_2016.loc[i+1, 'w_cfs'] == 1) and (df_2016.loc[i+2, 'w_cfs'] == 1) and (df_2016.loc[i+3, 'w_cfs'] == 1) and (df_2016.loc[i+4, 'w_cfs'] == 1) and (df_2016.loc[i+5, 'w_cfs'] == 1) and (df_2016.loc[i+6, 'w_cfs'] != 1):
        df_2016.loc[i, 'six_day_drought'] = 1
    else:
        df_2016.loc[i, 'seven_day_drought'] = 1

list_1day2016 = df_2016['one_day_drought'].tolist()
list_2day2016 = df_2016['two_day_drought'].tolist()
list_3day2016 = df_2016['three_day_drought'].tolist()
list_4day2016 = df_2016['four_day_drought'].tolist()
list_5day2016 = df_2016['five_day_drought'].tolist()
list_6day2016 = df_2016['six_day_drought'].tolist()
list_7day2016 = df_2016['seven_day_drought'].tolist()

#count the number of times the value 1 occurs in the list
list_1day2016 = list_1day2016.count(1)
list_2day2016 = list_2day2016.count(1)
list_3day2016 = list_3day2016.count(1)
list_4day2016 = list_4day2016.count(1)
list_5day2016 = list_5day2016.count(1)
list_6day2016 = list_6day2016.count(1)
list_7day2016 = list_7day2016.count(1)

#2017
for i in range (365):
    if (df_2017.loc[i, 'w_cfs'] == 1) and (df_2017.loc[i-1, 'w_cfs'] != 1):
        #Create a new column called drought_days and add the value 1 to that index position
        df_2017.loc[i, 'drought_starts'] = i
    else:
        df_2017.loc[i, 'drought_starts'] = 0
list2017 = df_2017['drought_starts'].tolist()
list2017 = [i for i in list2017 if i != 0]
#create columns in df_2017 named one_day_drought, two_day_drought, three_day_drought, four_day_drought, five_day_drought, six_day_drought, seven_day_drought
df_2017['one_day_drought'] = 0
df_2017['two_day_drought'] = 0
df_2017['three_day_drought'] = 0
df_2017['four_day_drought'] = 0
df_2017['five_day_drought'] = 0
df_2017['six_day_drought'] = 0
df_2017['seven_day_drought'] = 0

for i in list2017:
    if (df_2017.loc[i, 'w_cfs'] == 1) and (df_2017.loc[i+1, 'w_cfs'] != 1):
        df_2017.loc[i, 'one_day_drought'] = 1
    elif (df_2017.loc[i, 'w_cfs'] == 1) and (df_2017.loc[i+1, 'w_cfs'] == 1) and (df_2017.loc[i+2, 'w_cfs'] != 1):
        df_2017.loc[i, 'two_day_drought'] = 1
    elif (df_2017.loc[i, 'w_cfs'] == 1) and (df_2017.loc[i+1, 'w_cfs'] == 1) and (df_2017.loc[i+2, 'w_cfs'] == 1) and (df_2017.loc[i+3, 'w_cfs'] != 1):
        df_2017.loc[i, 'three_day_drought'] = 1
    elif (df_2017.loc[i, 'w_cfs'] == 1) and (df_2017.loc[i+1, 'w_cfs'] == 1) and (df_2017.loc[i+2, 'w_cfs'] == 1) and (df_2017.loc[i+3, 'w_cfs'] == 1) and (df_2017.loc[i+4, 'w_cfs'] != 1):
        df_2017.loc[i, 'four_day_drought'] = 1
    elif (df_2017.loc[i, 'w_cfs'] == 1) and (df_2017.loc[i+1, 'w_cfs'] == 1) and (df_2017.loc[i+2, 'w_cfs'] == 1) and (df_2017.loc[i+3, 'w_cfs'] == 1) and (df_2017.loc[i+4, 'w_cfs'] == 1) and (df_2017.loc[i+5, 'w_cfs'] != 1):
        df_2017.loc[i, 'five_day_drought'] = 1
    elif (df_2017.loc[i, 'w_cfs'] == 1) and (df_2017.loc[i+1, 'w_cfs'] == 1) and (df_2017.loc[i+2, 'w_cfs'] == 1) and (df_2017.loc[i+3, 'w_cfs'] == 1) and (df_2017.loc[i+4, 'w_cfs'] == 1) and (df_2017.loc[i+5, 'w_cfs'] == 1) and (df_2017.loc[i+6, 'w_cfs'] != 1):
        df_2017.loc[i, 'six_day_drought'] = 1
    else:
        df_2017.loc[i, 'seven_day_drought'] = 1

list_1day2017 = df_2017['one_day_drought'].tolist()
list_2day2017 = df_2017['two_day_drought'].tolist()
list_3day2017 = df_2017['three_day_drought'].tolist()
list_4day2017 = df_2017['four_day_drought'].tolist()
list_5day2017 = df_2017['five_day_drought'].tolist()
list_6day2017 = df_2017['six_day_drought'].tolist()
list_7day2017 = df_2017['seven_day_drought'].tolist()

#count the number of times the value 1 occurs in the list
list_1day2017 = list_1day2017.count(1)
list_2day2017 = list_2day2017.count(1)
list_3day2017 = list_3day2017.count(1)
list_4day2017 = list_4day2017.count(1)
list_5day2017 = list_5day2017.count(1)
list_6day2017 = list_6day2017.count(1)
list_7day2017 = list_7day2017.count(1)

#2018
for i in range (365):
    if (df_2018.loc[i, 'w_cfs'] == 1) and (df_2018.loc[i-1, 'w_cfs'] != 1):
        #Create a new column called drought_days and add the value 1 to that index position
        df_2018.loc[i, 'drought_starts'] = i
    else:
        df_2018.loc[i, 'drought_starts'] = 0
list2018 = df_2018['drought_starts'].tolist()
list2018 = [i for i in list2018 if i != 0]
#create columns in df_2018 named one_day_drought, two_day_drought, three_day_drought, four_day_drought, five_day_drought, six_day_drought, seven_day_drought
df_2018['one_day_drought'] = 0
df_2018['two_day_drought'] = 0
df_2018['three_day_drought'] = 0
df_2018['four_day_drought'] = 0
df_2018['five_day_drought'] = 0
df_2018['six_day_drought'] = 0
df_2018['seven_day_drought'] = 0

for i in list2018:
    if (df_2018.loc[i, 'w_cfs'] == 1) and (df_2018.loc[i+1, 'w_cfs'] != 1):
        df_2018.loc[i, 'one_day_drought'] = 1
    elif (df_2018.loc[i, 'w_cfs'] == 1) and (df_2018.loc[i+1, 'w_cfs'] == 1) and (df_2018.loc[i+2, 'w_cfs'] != 1):
        df_2018.loc[i, 'two_day_drought'] = 1
    elif (df_2018.loc[i, 'w_cfs'] == 1) and (df_2018.loc[i+1, 'w_cfs'] == 1) and (df_2018.loc[i+2, 'w_cfs'] == 1) and (df_2018.loc[i+3, 'w_cfs'] != 1):
        df_2018.loc[i, 'three_day_drought'] = 1
    elif (df_2018.loc[i, 'w_cfs'] == 1) and (df_2018.loc[i+1, 'w_cfs'] == 1) and (df_2018.loc[i+2, 'w_cfs'] == 1) and (df_2018.loc[i+3, 'w_cfs'] == 1) and (df_2018.loc[i+4, 'w_cfs'] != 1):
        df_2018.loc[i, 'four_day_drought'] = 1
    elif (df_2018.loc[i, 'w_cfs'] == 1) and (df_2018.loc[i+1, 'w_cfs'] == 1) and (df_2018.loc[i+2, 'w_cfs'] == 1) and (df_2018.loc[i+3, 'w_cfs'] == 1) and (df_2018.loc[i+4, 'w_cfs'] == 1) and (df_2018.loc[i+5, 'w_cfs'] != 1):
        df_2018.loc[i, 'five_day_drought'] = 1
    elif (df_2018.loc[i, 'w_cfs'] == 1) and (df_2018.loc[i+1, 'w_cfs'] == 1) and (df_2018.loc[i+2, 'w_cfs'] == 1) and (df_2018.loc[i+3, 'w_cfs'] == 1) and (df_2018.loc[i+4, 'w_cfs'] == 1) and (df_2018.loc[i+5, 'w_cfs'] == 1) and (df_2018.loc[i+6, 'w_cfs'] != 1):
        df_2018.loc[i, 'six_day_drought'] = 1
    else:
        df_2018.loc[i, 'seven_day_drought'] = 1

list_1day2018 = df_2018['one_day_drought'].tolist()
list_2day2018 = df_2018['two_day_drought'].tolist()
list_3day2018 = df_2018['three_day_drought'].tolist()
list_4day2018 = df_2018['four_day_drought'].tolist()
list_5day2018 = df_2018['five_day_drought'].tolist()
list_6day2018 = df_2018['six_day_drought'].tolist()
list_7day2018 = df_2018['seven_day_drought'].tolist()

#count the number of times the value 1 occurs in the list
list_1day2018 = list_1day2018.count(1)
list_2day2018 = list_2day2018.count(1)
list_3day2018 = list_3day2018.count(1)
list_4day2018 = list_4day2018.count(1)
list_5day2018 = list_5day2018.count(1)
list_6day2018 = list_6day2018.count(1)
list_7day2018 = list_7day2018.count(1)

#2019
for i in range (365):
    if (df_2019.loc[i, 'w_cfs'] == 1) and (df_2019.loc[i-1, 'w_cfs'] != 1):
        #Create a new column called drought_days and add the value 1 to that index position
        df_2019.loc[i, 'drought_starts'] = i
    else:
        df_2019.loc[i, 'drought_starts'] = 0
list2019 = df_2019['drought_starts'].tolist()
list2019 = [i for i in list2019 if i != 0]
#create columns in df_2019 named one_day_drought, two_day_drought, three_day_drought, four_day_drought, five_day_drought, six_day_drought, seven_day_drought
df_2019['one_day_drought'] = 0
df_2019['two_day_drought'] = 0
df_2019['three_day_drought'] = 0
df_2019['four_day_drought'] = 0
df_2019['five_day_drought'] = 0
df_2019['six_day_drought'] = 0
df_2019['seven_day_drought'] = 0

for i in list2019:
    if (df_2019.loc[i, 'w_cfs'] == 1) and (df_2019.loc[i+1, 'w_cfs'] != 1):
        df_2019.loc[i, 'one_day_drought'] = 1
    elif (df_2019.loc[i, 'w_cfs'] == 1) and (df_2019.loc[i+1, 'w_cfs'] == 1) and (df_2019.loc[i+2, 'w_cfs'] != 1):
        df_2019.loc[i, 'two_day_drought'] = 1
    elif (df_2019.loc[i, 'w_cfs'] == 1) and (df_2019.loc[i+1, 'w_cfs'] == 1) and (df_2019.loc[i+2, 'w_cfs'] == 1) and (df_2019.loc[i+3, 'w_cfs'] != 1):
        df_2019.loc[i, 'three_day_drought'] = 1
    elif (df_2019.loc[i, 'w_cfs'] == 1) and (df_2019.loc[i+1, 'w_cfs'] == 1) and (df_2019.loc[i+2, 'w_cfs'] == 1) and (df_2019.loc[i+3, 'w_cfs'] == 1) and (df_2019.loc[i+4, 'w_cfs'] != 1):
        df_2019.loc[i, 'four_day_drought'] = 1
    elif (df_2019.loc[i, 'w_cfs'] == 1) and (df_2019.loc[i+1, 'w_cfs'] == 1) and (df_2019.loc[i+2, 'w_cfs'] == 1) and (df_2019.loc[i+3, 'w_cfs'] == 1) and (df_2019.loc[i+4, 'w_cfs'] == 1) and (df_2019.loc[i+5, 'w_cfs'] != 1):
        df_2019.loc[i, 'five_day_drought'] = 1
    elif (df_2019.loc[i, 'w_cfs'] == 1) and (df_2019.loc[i+1, 'w_cfs'] == 1) and (df_2019.loc[i+2, 'w_cfs'] == 1) and (df_2019.loc[i+3, 'w_cfs'] == 1) and (df_2019.loc[i+4, 'w_cfs'] == 1) and (df_2019.loc[i+5, 'w_cfs'] == 1) and (df_2019.loc[i+6, 'w_cfs'] != 1):
        df_2019.loc[i, 'six_day_drought'] = 1
    else:
        df_2019.loc[i, 'seven_day_drought'] = 1

list_1day2019 = df_2019['one_day_drought'].tolist()
list_2day2019 = df_2019['two_day_drought'].tolist()
list_3day2019 = df_2019['three_day_drought'].tolist()
list_4day2019 = df_2019['four_day_drought'].tolist()
list_5day2019 = df_2019['five_day_drought'].tolist()
list_6day2019 = df_2019['six_day_drought'].tolist()
list_7day2019 = df_2019['seven_day_drought'].tolist()

#count the number of times the value 1 occurs in the list
list_1day2019 = list_1day2019.count(1)
list_2day2019 = list_2day2019.count(1)
list_3day2019 = list_3day2019.count(1)
list_4day2019 = list_4day2019.count(1)
list_5day2019 = list_5day2019.count(1)
list_6day2019 = list_6day2019.count(1)
list_7day2019 = list_7day2019.count(1)


data1 = [list_1day2006, list_1day2007, list_1day2008, list_1day2009, list_1day2010, list_1day2011, list_1day2012, list_1day2013, list_1day2014, list_1day2015, list_1day2016, list_1day2017, list_1day2018, list_1day2019]
data2 = [list_2day2006, list_2day2007, list_2day2008, list_2day2009, list_2day2010, list_2day2011, list_2day2012, list_2day2013, list_2day2014, list_2day2015, list_2day2016, list_2day2017, list_2day2018, list_2day2019]
data3 = [list_3day2006, list_3day2007, list_3day2008, list_3day2009, list_3day2010, list_3day2011, list_3day2012, list_3day2013, list_3day2014, list_3day2015, list_3day2016, list_3day2017, list_3day2018, list_3day2019]
data4 = [list_4day2006, list_4day2007, list_4day2008, list_4day2009, list_4day2010, list_4day2011, list_4day2012, list_4day2013, list_4day2014, list_4day2015, list_4day2016, list_4day2017, list_4day2018, list_4day2019]
data5 = [list_5day2006, list_5day2007, list_5day2008, list_5day2009, list_5day2010, list_5day2011, list_5day2012, list_5day2013, list_5day2014, list_5day2015, list_5day2016, list_5day2017, list_5day2018, list_5day2019]
data6 = [list_6day2006, list_6day2007, list_6day2008, list_6day2009, list_6day2010, list_6day2011, list_6day2012, list_6day2013, list_6day2014, list_6day2015, list_6day2016, list_6day2017, list_6day2018, list_6day2019]
data7 = [list_7day2006, list_7day2007, list_7day2008, list_7day2009, list_7day2010, list_7day2011, list_7day2012, list_7day2013, list_7day2014, list_7day2015, list_7day2016, list_7day2017, list_7day2018, list_7day2019]

data = [data1, data2, data3, data4, data5, data6, data7]

###

sns.set_style("whitegrid")
# Override Matplotlib's default font family for Seaborn text elements
plt.rcParams['font.family'] = 'DejaVu Sans'

fig, ax = plt.subplots(figsize=(10, 7))
boxprops = dict(facecolor='royalblue', edgecolor='black')
whiskerprops = dict(color='black')
medianprops = dict(color='black')
flierprops = dict(markerfacecolor='black')
capprops = dict(color='black')
bp = sns.boxplot(data=data, ax=ax, boxprops=boxprops, whiskerprops=whiskerprops, medianprops=medianprops, flierprops=flierprops, capprops=capprops)
for whisker in bp.artists:
    whisker.set(color='black')
    
    

ax.set_xticklabels(['1', '2', '3', '4', '5', '6', '7+'], fontsize=24, rotation=0)
ax.yaxis.set_tick_params(labelsize=24)
ax.set_title('Low Wind Resource Days', fontsize=30, pad=10)
ax.set_ylabel('Occurrences per Year', fontsize=26)
ax.set_xlabel('Consecutive Days', fontsize=24, labelpad=5)
ax.tick_params(axis='x', which='both', bottom='on', labelbottom='on') #Can make xticks go away

ax.set_ylim(-0.05, 20)
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
plt.tick_params(axis='y', which='both', left='on', labelleft='on')

ax = plt.gca() 
# Set the color of the spines
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Set the linewidth of the spines
ax.spines['left'].set_linewidth(1)
ax.spines['bottom'].set_linewidth(1)


plt.grid(False)
#plt.savefig(os.path.join(output_path, 'wind_droughts_per_year.jpg'), dpi=300,bbox_inches='tight')
plt.show()

#print the median number of droughts per year
print('Median number of 1 day droughts per year: ', statistics.median(data1))
print('Median number of 2 day droughts per year: ', statistics.median(data2))
print('Median number of 3 day droughts per year: ', statistics.median(data3))
print('Median number of 4 day droughts per year: ', statistics.median(data4))
print('Median number of 5 day droughts per year: ', statistics.median(data5))
print('Median number of 6 day droughts per year: ', statistics.median(data6))
print('Median number of 7+ day droughts per year: ', statistics.median(data7))

#print all values in df_2016
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    #print(df_2016)


#print the median number of droughts per year
print('Median number of droughts per year: ', statistics.median(data))