'''
This script will add the word 'solar' to the end of the name of each csv file in a folder.
'''
#imoport modules
import os
from pathlib import Path
import csv

#Create path to folder with all the solar capacity factor csv files
#docs = Path("/Users/Dominic/Desktop/NSRDB cfs with leap/4 - MEM ready solar cfs by location with leap")
docs = Path("/Users/Dominic/Desktop/2019 wind data")

for file in docs.iterdir():
    #print(file)
    old_name = file.stem
    #print(old_name)
    old_name_5 = old_name[0:5]
    #print(old_name_5)
    new_name = old_name_5 + ' with cfs wind.csv'
    #print(new_name)
    #specify the path of the renamed file
    new_name = os.path.join(docs, new_name)
    os.rename(file, new_name)