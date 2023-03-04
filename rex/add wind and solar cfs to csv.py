"""
This code will obtain data from multiple csv files, calculate solar capacity 
factors from the data, and export those data to a new csv file.
"""
# Import modules
import pandas as pd
import numpy as np
import os
import glob
import matplotlib.pyplot as plt


#Create a list of the csv files in the data folder
data_path="/Users/Dominic/Desktop/trial/"
csv_files = glob.glob(os.path.join(data_path, "*.csv"))

#Read the seventh column from a csv file into a pandas dataframe. Skip rows 0 and 1. Repeat for each csv file in csv_files
for file in csv_files:
    data = pd.read_csv(file, sep=",", header=0, usecols=[7], skiprows=[0,1], nrows=8760)
    #print(data)
    
    #Calculate the solar capacity factor for each row in the dataframe by dividing the data in column 7 by 1000
    data['Solar Capacity Factor'] = data.iloc[:,0]/1000
    print(data)

    #Save the solar capacity factor data to a column 12 of the csv file that it came from.
    #data.to_csv(file, sep=",", index=0, mode='a', columns=['Solar Capacity Factor'])









#Make a blank array of characters named wind_cfs to hold the wind capacity factor data
wind_cfs = np.zeros((8761, 1))
#Name the first row of the array "Wind Capacity Factor"

print(wind_cfs)
#Read the eigth column from a csv file into a pandas dataframe. Skip rows 0, 1, and all rows past 8763. Repeat for each csv file in csv_files
for file in csv_files:
    wind = pd.read_csv(file, sep=",", header=0, usecols=[8], skiprows=[0,1], nrows=8760)
    print(wind)
    #Calculate the wind capacity factor for each row in the dataframe using a piecewise function that determines capacity factor based on wind speed. Append this value to a new column in the dataframe.
    for i in range(len(wind)):
        if wind.iloc[i,0] < 3:
            wind_cfs[i+1] = 0
        elif wind.iloc[i,0] >= 3 and wind.iloc[i,0] < 4:
            wind_cfs[i+1] = 0.0043
        elif wind.iloc[i,0] >= 4 and wind.iloc[i,0] < 5:
            wind_cfs[i+1] = 0.0323
        elif wind.iloc[i,0] >= 5 and wind.iloc[i,0] < 6:
            wind_cfs[i+1] = 0.0771
        elif wind.iloc[i,0] >= 6 and wind.iloc[i,0] < 7:
            wind_cfs[i+1] = 0.1426
        elif wind.iloc[i,0] >= 7 and wind.iloc[i,0] < 8:
            wind_cfs[i+1] = 0.2392
        elif wind.iloc[i,0] >= 8 and wind.iloc[i,0] < 9:
            wind_cfs[i+1] = 0.3528
        elif wind.iloc[i,0] >= 9:
            wind_cfs[i+1] = 0.4765

    print(wind_cfs)
    #Save the wind capacity factor data to a column 13 of the csv file that it came from.
    #wind_cfs.to_csv(file, sep=",", index=0, mode='a', columns=['Wind Capacity Factor'])