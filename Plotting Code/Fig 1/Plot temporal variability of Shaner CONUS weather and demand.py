# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 16:06:53 2023

@author: Dominic
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 11:25:28 2023

@author: Dominic
"""

'''
This script will determine the mean of the wind speed per day of the year for each year in the WIND toolkit data. 
It will compare this mean to each value in the data and determine how much larger or smaller each value is than the mean. 
It will then graph the difference between each value and the mean for each day of the year for each year in the data.'''
import os
import sys
import csv
import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

HI_wind = Path("/Users/covel/OneDrive/Desktop/wind_cf_Dan_normalized_to_0.38_mean_United States - 2006 thru 2015.csv")
HI_solar = Path("/Users/covel/OneDrive/Desktop/solar_series_Shaner_unnormalized - 2006 onward.csv")
HI_demand = Path("/Users/covel/OneDrive/Desktop/CONUS_demand 2006-2015.csv")
output_path = '/Users/covel/OneDrive/'
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
#print(getData(HI_wind))


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
    
def stat_quantile(groupby_dataframe, quantile):
	output = groupby_dataframe.quantile(q = quantile)
	return output

def time_shift(array, hourstoshift):

	for i in range(hourstoshift):

		row = array.iloc[0] # take stock of first row
		array = array.shift(-1) # remove first entry and shift all data up one row
		array.iloc[-1] = row # put old first row as last row

	
	array = array.values
	return array

def process_data(demand, solar, wind, region):

    #get the data
    demand_df_40 = getData(demand)
    demand_df = demand_df_40[demand_df_40.year != '1979']
    demand_df.reset_index(drop=True, inplace=True)
#    if region == 'WECC':
#        demand_df = demand_df.rename(columns={'demand': 'demand (MW)'})
        
    solar_df = getData(solar)
    wind_df = getData(wind)  
    
    #turn the year month day columns into one new column called date
    dateMaker(demand_df, 'demand')
    dateMaker(solar_df, 'solar')
    dateMaker(wind_df, 'wind')
    
    #normalize the data (ie divide by the 39 year mean)
    demand_mean = demand_df['demand (MW)'].mean()
    solar_mean = solar_df['s_cfs'].mean()
    wind_mean = wind_df['w_cfs'].mean()
    
    demand_df['demand (MW)']=demand_df['demand (MW)']/demand_mean
    solar_df['s_cfs']=solar_df['s_cfs']/solar_mean
    wind_df['w_cfs']=wind_df['w_cfs']/wind_mean
    
    #make y values for plotting main fig (resample to take the daily mean)
    dailyMean_demand = demand_df.resample('D').mean()
    dailyMean_solar = solar_df.resample('D').mean()
    dailyMean_wind = wind_df.resample('D').mean()
    
    #groups each value by day of year (can compare the same day in many diff years)
    demand_gb=dailyMean_demand.groupby(dailyMean_demand.index.dayofyear)
    solar_gb=dailyMean_solar.groupby(dailyMean_solar.index.dayofyear)
    wind_gb=dailyMean_wind.groupby(dailyMean_wind.index.dayofyear)
    
    #median for each day
    y_demand = demand_gb.median()
    y_solar = solar_gb.median()
    y_wind = wind_gb.median()
    
    demand_quartiles = []
    #makes the 50% / 100% areas
    demand_fourth_quartile = stat_quantile(demand_gb, 1)
    demand_quartiles.append(demand_fourth_quartile)
    demand_third_quartile = stat_quantile(demand_gb, 0.75)
    demand_quartiles.append(demand_third_quartile)
    demand_first_quartile = stat_quantile(demand_gb, 0.25)
    demand_quartiles.append(demand_first_quartile)
    demand_zeroth_quartile = stat_quantile(demand_gb, 0)
    demand_quartiles.append(demand_zeroth_quartile)
    
    solar_quartiles = []
    solar_fourth_quartile = stat_quantile(solar_gb, 1)
    solar_quartiles.append(solar_fourth_quartile)
    solar_third_quartile = stat_quantile(solar_gb, 0.75)
    solar_quartiles.append(solar_third_quartile)
    solar_first_quartile = stat_quantile(solar_gb, 0.25)
    solar_quartiles.append(solar_first_quartile)
    solar_zeroth_quartile = stat_quantile(solar_gb, 0)
    solar_quartiles.append(solar_zeroth_quartile)
    
    wind_quartiles=[]
    wind_fourth_quartile = stat_quantile(wind_gb, 1)
    wind_quartiles.append(wind_fourth_quartile)
    wind_third_quartile = stat_quantile(wind_gb, 0.75)
    wind_quartiles.append(wind_third_quartile)
    wind_first_quartile = stat_quantile(wind_gb, 0.25)
    wind_quartiles.append(wind_first_quartile)
    wind_zeroth_quartile = stat_quantile(wind_gb, 0)
    wind_quartiles.append(wind_zeroth_quartile)
    
    x_values = range(len(y_demand))
    
    return x_values, y_demand, y_solar, y_wind, demand_quartiles, solar_quartiles, wind_quartiles, solar_mean, wind_mean

#plot
    
HI_x_values, HI_y_demand, HI_y_solar, HI_y_wind, HI_demand_quartiles, HI_solar_quartiles, \
HI_wind_quartiles, HI_solar_mean, HI_wind_mean = process_data(HI_demand, HI_solar, HI_wind, 'HI')


#print('CONUS demand std deviation over the year',HI_y_demand.std())
#print('CONUS solar std deviation over the year',HI_y_solar.std())
#print('CONUS wind std deviation over the year',HI_y_wind.std())

# Calculating the relative standard deviation for each dataset
relative_std_demand = (HI_y_demand.std() / HI_y_demand.mean()) * 100
relative_std_solar = (HI_y_solar.std() / HI_y_solar.mean()) * 100
relative_std_wind = (HI_y_wind.std() / HI_y_wind.mean()) * 100

# Printing the results
print('CONUS demand relative std deviation over the year:', relative_std_demand, '%')
print('CONUS solar relative std deviation over the year:', relative_std_solar, '%')
print('CONUS wind relative std deviation over the year:', relative_std_wind, '%')

'''
wind_mxmn = HI_wind_quartiles[0]['w_cfs']-HI_wind_quartiles[3]['w_cfs']
wind_mxmn_avg = wind_mxmn.mean()
print(wind_mxmn_avg)
wind_index = wind_mxmn.idxmax()
solar_mxmn = HI_solar_quartiles[0]['s_cfs']-HI_solar_quartiles[3]['s_cfs']
solar_mxmn_avg = solar_mxmn.mean()
print(solar_mxmn_avg)
solar_index = solar_mxmn.idxmax()

print('Wind max daily median',HI_y_wind['w_cfs'].max())
print('Wind max daily median index',HI_y_wind['w_cfs'].idxmax())
print('Wind min daily median',HI_y_wind['w_cfs'].min())
print('Wind min daily median index',HI_y_wind['w_cfs'].idxmin(),'\n')

print('Solar max daily median',HI_y_solar['s_cfs'].max())
print('Solar max daily median index',HI_y_solar['s_cfs'].idxmax())
print('Solar min daily median',HI_y_solar['s_cfs'].min())
print('Solar min daily median index',HI_y_solar['s_cfs'].idxmin(),'\n')

print('Demand max daily median',HI_y_demand['demand (MW)'].max())
print('Demand max daily median index',HI_y_demand['demand (MW)'].idxmax())
print('Demand min daily median',HI_y_demand['demand (MW)'].min())
print('Demand min daily median index',HI_y_demand['demand (MW)'].idxmin())
'''
#
#WI_wind_mxmn = WECC_wind_quartiles[0]['wind capacity']-WECC_wind_quartiles[3]['wind capacity']
#WI_wind_index = WI_wind_mxmn.idxmax()
#WI_solar_mxmn = WECC_solar_quartiles[0]['solar capacity']-WECC_solar_quartiles[3]['solar capacity']
#WI_solar_index = WI_solar_mxmn.idxmax()

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
months =['Jan', 'Mar', 'May',  'Jul', 'Sep', 'Nov']

#==============================================================================
#Plot
#==============================================================================

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
months =['Jan', 'Mar', 'May',  'Jul', 'Sep', 'Nov']

fig = plt.figure(figsize=(30, 7))
ax1 = plt.subplot(141)

ax1.plot(HI_x_values, HI_y_demand, color='black', linewidth='2', label='demand', zorder=2)
ax1.fill_between(HI_x_values, HI_demand_quartiles[3]['demand (MW)'], HI_demand_quartiles[0]['demand (MW)'], alpha = 0.3, facecolor = 'black', zorder=2)
ax1.fill_between(HI_x_values, HI_demand_quartiles[2]['demand (MW)'], HI_demand_quartiles[1]['demand (MW)'], alpha = 0.5, facecolor = 'black',zorder=2)

ax1.plot(HI_x_values, HI_y_solar, color='orange', linewidth='2', label='solar', zorder=1)
ax1.fill_between(HI_x_values, HI_solar_quartiles[3]['s_cfs'], HI_solar_quartiles[0]['s_cfs'], alpha = 0.3, facecolor = 'orange', edgecolor = 'orange', zorder=1)
ax1.fill_between(HI_x_values, HI_solar_quartiles[2]['s_cfs'], HI_solar_quartiles[1]['s_cfs'], alpha = 0.5, facecolor = 'orange', edgecolor = 'orange', zorder=1)

ax1.plot(HI_x_values, HI_y_wind, color='blue', linewidth='2', label='wind', zorder=0)
ax1.fill_between(HI_x_values, HI_wind_quartiles[3]['w_cfs'], HI_wind_quartiles[0]['w_cfs'], alpha = 0.3, facecolor = 'blue', zorder=0)
ax1.fill_between(HI_x_values, HI_wind_quartiles[2]['w_cfs'], HI_wind_quartiles[1]['w_cfs'], alpha = 0.5, facecolor = 'blue', zorder=0)


ax1.set_ylabel('Power divided by\n10-year mean', fontsize = 26, color = 'black')
ax1.set_title('CONUS Resources', fontsize=30)
ax1.set_xlim(0, 365)
ax1.set_ylim(0,3.5)
ax1.set_xticks(np.arange(10, 360, 62))
ax1.set_xticklabels(months, fontsize = 24)
ax1.set_yticklabels(ax1.get_yticks(), fontsize=24)
ax1.set_xlabel('Month of year', fontsize=24, labelpad=10)


#fig.text(0.13, 0.93, 'a)', size='large')
#fig.text(0.13, 0.265, 'b)', size='large')
#
#Determine the range of the highest and lowest wind and solar capacity
#ax1.annotate('Wind range: {}'.format(round(wind_mxmn.max(), 2)), xy=(wind_index, 1.5), xytext=(wind_index, 1.5), fontsize=12)
#ax1.annotate('Solar range: {}'.format(round(solar_mxmn.max(), 2)), xy=(solar_index, 1.5), xytext=(solar_index, 1.5), fontsize=12)

plt.tight_layout()
#plt.savefig('C:\\Users\\Dominic\\desktop\\Oahu Results\\CONUS_Shaner_10yr.png', dpi=300, bbox_inches='tight')
plt.show()