**The process to collect solar irradiation data from the NSRDB specific to Oahu, then convert the data into capacity factors is outlined in this folder.**

**1** - Download solar data from the NSRDB data viewer (https://nsrdb.nrel.gov/data-viewer). With this interactive map tool, you can create a polygon from points surrounding Oahu and download data from every point within the polygon. The "USA & Americas (30, 60min / 4km / 1998-2022)" dataset was selected. ArcGIS Pro was used to create a 4km grid around Oahu and determine which points included in the download had no gridded overlap with the island. A total of 108 points were identified with a nonzero amount of gridded overlap with Oahu. These 108 points were then processed as detailed in subsequent steps to determine the solar capacity factors. Each year of data for each point is downloaded as a separate csv.

**2** -  Add wind and solar cfs to csv.py 

* This script will create solar and wind capacity factors for each csv in the full NSRDB download. It will add these factors back into the .csv they were derived from. Note, wind capacity factors generated from this script did not end up being used for analysis in the paper, as we opted to use more detailed wind data from the NREL WIND Toolkit. There are technically two scripts. Use the one with LEAP YEAR in the name on folders with data from leap years only. Likewise, use the one with NON LEAP YEARS on folders with data from years that are not leap years.

**3** - Sort locations into new folders.py 

* This script will sort the .csv's for all years and all locations into one of 108 folders specific to the location. It creates these folders as well.

**4** - add all yearly solar cfs together per location.py 

* This script will parse all the .csv's at one location and combine their solar capacity factors together into a new .csv. Can be easily modified to do this process for the wind capacity factors. Includes the data from Feb 29th on all specified leap years. You must manually specify leap years. It will not automatically determine them

**5** - Generate proper format PyPSA csv solar cfs.py 

* This script will input the PyPSA format into a dataframe and add the capacity factors to the correct column and row of that dataframe, then export the dataframe to a new .csv based on the input data file name. It requires that you already have a csv formatted to be used in PyPSA. It is in this folder, named "full with leap solar cfs format.csv" 

**6** - Create weighted solar cf input file.py

* This script will weight the different input files and add their weighted values to produce one weighted average csv file. It retrieves the weights from the file included in this folder, "Solar Weights.csv"
