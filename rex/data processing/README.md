This README covers the process needed to convert the NSDRB data into usable capacity factors that are in the proper format for MEM.

Each .py script in the data processing folder has a number at the start of its name. This is the order in which these scripts need to be run.

Process outline:

1 - Add wind and solar cfs to csv.py
  This script will create solar and wind capacity factors for each csv in the full NSRDB download. It will add these factors back into the .csv they were derived from
  
2 - Sort locations into new folders.py
  This script will sort the .csv's for all years and all locations into one of 91 folders specific to the location. It creates these folders as well
  
3 - add all yearly solar cfs together per location.py
  This script will parse all the .csv's at one location and combine their solar capacity factors together into a new .csv. Can be easily modified to do this process for the wind capacity factors
