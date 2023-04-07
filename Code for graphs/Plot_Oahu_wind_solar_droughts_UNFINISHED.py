#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:00:31 2020

this handles droughts differently than the other one in that it
looks to see if the CF is less than the mean daily CF for that day of yr
rather than over the whole 39 yr period

@author: katherinerinaldi
"""

import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import seaborn as sns
from pathlib import Path

HI_wind = Path("/Users/Dominic/Desktop/Oahu wind toolkit means.csv")
HI_solar = Path("/Users/Dominic/Desktop/Oahu nsrdb means 2006 - 2019.csv")

#HI_wind = Path("/Users/Dominic/Desktop/20200809_HI_mthd1_1980-2019_wind.csv")
#HI_solar = Path("/Users/Dominic/Desktop/20200809_HI_mthd1_1980-2019_solar.csv")
output_path = '/Users/Dominic/'

cutoff= 0.1

#this takes in the file and gets rid of all lines before BEGIN_DATA
#then it returns a pandas dataframe

def getData(filename):
    with open(filename) as file:
        reader = csv.reader(file)
        
          #read to keyword 'BEGIN_DATA'
        while True:
            line = next(reader)
            if line[0] == 'BEGIN_DATA':
                break
        
        #take all non-blank lines
        data = []
        while True:
            try:
                line = next(reader)
                if any(field.strip() for field in line):
                    data.append(line)
            except:
                break
        
#        #turn data dataframe
        df = pd.DataFrame(data)
        headers = df.iloc[0]
        data_array  = pd.DataFrame(df.values[1:], columns=headers)

        return data_array


# this makes the new 'date' column in each type of dataframe (depending on how
# the original file is formatted there are diff options)
def dateMaker(df, dataType):
    if dataType == 'wind':
        df['w_cfs']=df['w_cfs'].astype(float)
    elif dataType == 'solar':
        df['s_cfs']=df['s_cfs'].astype(float)
    elif dataType == 'demand':
        df['demand (MW)']=df['demand (MW)'].astype(float)
    #added this little bit in to make the days align the right way
    # we were doing days from 1-24 and datetime does it from 0-23
    df['hour']=df['hour'].astype(int)
    df['hour']=df['hour']-1
    dates=pd.to_datetime(df[['year', 'month', 'day', 'hour']])
    df['date'] = dates
    df.set_index(['date'], inplace=True)

def getLTvalues(gb, mean, percent, capacityType):

    i=1
    is_lt_dates=[]
    is_lt_CF = []
    while i<=366:
        n=0
        days=len(gb.get_group(i))
        df=gb.get_group(i).reset_index()
        # cutoff=percent*mean[capacityType][i]
        while n<days:
            if df[capacityType][n]<cutoff:
                is_lt_dates.append(df['date'][n])
                is_lt_CF.append(df[capacityType][n])
            n+=1
        i+=1
    
    data={'dates':is_lt_dates, 'CF':is_lt_CF}
    lt_df = pd.DataFrame(data=data)
    lt_df=lt_df.set_index('dates')
    lt_df=lt_df.sort_index()
    
    return lt_df

def makeDFs(solar, wind):

    solar_df = getData(solar)
    wind_df = getData(wind)
            
    #turn the year month day columns into one new column called date
    dateMaker(solar_df, 'solar')
    dateMaker(wind_df, 'wind')
    
    dm_solar = solar_df.resample('D').mean()
    dm_wind = wind_df.resample('D').mean()
    
    dm_solar['dayofyr'] = dm_solar.index.dayofyear
    dm_wind['dayofyr']=dm_wind.index.dayofyear
    
    solar_gb=dm_solar.groupby(dm_solar.index.dayofyear)
    solar_gb_mean=solar_gb.mean()
    
    
    wind_gb=dm_wind.groupby(dm_wind.index.dayofyear)
    wind_gb_mean=wind_gb.mean()
    
    solar_lt_df = getLTvalues(solar_gb, solar_gb_mean, cutoff, 's_cfs')
    wind_lt_df = getLTvalues(wind_gb, wind_gb_mean, cutoff, 'w_cfs')
    
    return solar_lt_df, wind_lt_df, dm_solar, dm_wind

HI_solar_lt_df,HI_wind_lt_df, HI_solar_df, HI_wind_df= makeDFs(HI_solar, HI_wind) 


HI_solar_lt_df=HI_solar_lt_df.reset_index()
HI_wind_lt_df=HI_wind_lt_df.reset_index()


def get_common_dates(list1, list2):
    
    list1_as_set = set(list1)
    intersection = list1_as_set.intersection(list2)

    timestamps = list(intersection)
    timestamps.sort()
    
#    dates = [datetime.datetime.strptime(ts, "%Y-%m-%d") for ts in timestamps]
#    dates.sort()
    
    return timestamps

def get_consecutive_days(df):

    dates = df['dates']
    
    grouped_start = []
    grouped_end = []
    grouped_span = []
    
    
    for i in range(len(dates)): 
        
        if i != 0: 
            index = len(grouped_span) - 1
    
            if (dates[i].date() - grouped_end[index]).days == 1: 
                grouped_end[index] = dates[i].date() 
                grouped_span[index] = (grouped_end[index]-grouped_start[index]).days + 1
            else: 
                grouped_start.append(dates[i].date())
                grouped_end.append(dates[i].date())
    
                array_size=len(grouped_end)-1
                grouped_span.append((grouped_end[array_size]-grouped_start[array_size]).days+1)
                
        else: 
            grouped_start.append(dates[i].date())
            grouped_end.append(dates[i].date())
    
            array_size=len(grouped_end)-1
            grouped_span.append((grouped_end[array_size]-grouped_start[array_size]).days+1)
    
    days_data={'start':grouped_start, 'end':grouped_end, 'span':grouped_span}
    final_df=pd.DataFrame(data=days_data)
    
    return final_df

consec_HI_solar=get_consecutive_days(HI_solar_lt_df)
consec_HI_wind=get_consecutive_days(HI_wind_lt_df)

# CA_combo = get_common_dates(CA_solar_lt_df['dates'], CA_wind_lt_df['dates'])
# WECC_combo = get_common_dates(WECC_solar_lt_df['dates'], WECC_wind_lt_df['dates'])

def add_duration(df):
    df['duration']=''
    one=df[df['span']==1]
    two=df[df['span']==2]
    three2six=df[df['span'].between(3,6)]
    sevenplus=df[df['span']>=7]
    for ind in one.index:
        df['duration'][ind]='1 day'
    for ind in two.index:
        df['duration'][ind]='2 days'
    for ind in three2six.index:
        df['duration'][ind]='3-6 days'
    for ind in sevenplus.index:
        df['duration'][ind]='7+ days'
    years=pd.DatetimeIndex(df['start']).year
    df['year']=years
    
    drought_dict={'1 day':len(one), '2 days':len(two), '3-6':len(three2six), '7+ days':len(sevenplus)}
    print(drought_dict)
    
    return df

add_duration(consec_HI_solar)
add_duration(consec_HI_wind)


# def fill_missing_values(df):
#     years = np.arange(1980, 2019, 1)
    
#     df[df.year]

years=np.arange(2006, 2019, 1)
full_years=np.repeat(years, 4)

durations=['1 day', '2 days', '3-6 days', '7+ days']
full_durations=['1 day', '2 days', '3-6 days', '7+ days']
i=0
while i<38:
    full_durations.extend(durations)
    i+=1

arrays=[full_years, full_durations]
tuples = list(zip(*arrays))

new_index = pd.MultiIndex.from_tuples(tuples, names=['year', 'duration'])

HIsolarevents=pd.DataFrame({'# events' : consec_HI_solar.groupby( [ "year", "duration"] ).size()})
HIsolar2plot=HIsolarevents.reindex(new_index, fill_value=0)
HIsolar2plot=HIsolar2plot.reset_index()
HIsolar2plot['region']='HI'

HIwindevents=pd.DataFrame({'# events' : consec_HI_wind.groupby( [ "year", "duration"] ).size()})
HIwind2plot=HIwindevents.reindex(new_index, fill_value=0)
HIwind2plot=HIwind2plot.reset_index()
HIwind2plot['region']='HI'


solar=HIsolar2plot
wind=HIwind2plot
        
fig = plt.figure(figsize=(4,5.5))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

sns.boxplot(ax=ax1, x=solar['duration'], y=solar['# events'], whis=[0, 100],
            hue=solar['region'], palette=['orange', 'tomato'])
sns.boxplot(ax=ax2, x=wind['duration'], y=wind['# events'], whis=[0, 100], hue=wind['region'], 
            palette=['lightsteelblue', 'cornflowerblue'])

ax1.legend()
ax2.legend()


ax2.set_xlabel('Drought duration', fontsize=12)
ax1.set_xlabel('')

ax1.set_title('(a) Solar', fontsize=14)
ax2.set_title('(b) Wind', fontsize=14)
ax1.set_ylabel('')
ax2.set_ylabel('')

ax1.yaxis.set_ticks(np.arange(0, 13, 2))
ax1.set_ylim(-1, 13)

ax2.yaxis.set_ticks(np.arange(0, 30, 4))
ax2.set_ylim(-1, 31)

# plt.ylabel('Number of resource droughts in 39 year period', fontsize = 14)

plt.tight_layout()
plt.text(-1.2, 8,'Number of drought events per year', fontsize = 14, rotation=90)

plt.savefig('Oahu solar wind droughts.jpg', dpi = 300, bbox_inches='tight')
plt.show()