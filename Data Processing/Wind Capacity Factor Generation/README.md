**1** - Download Wind Toolkit data from AWS server for OEDI (https://data.openei.org/s3_viewer?bucket=nrel-pds-wtk&prefix=Hawaii%2F). This downloads an h5 file containing all points for Hawaii for the selected year and hub height.  

**2** - determine wind locations around oahu.py

* This script was used to identify the index number plus latitude and longitude of any points in the h5 file that fell within a square region encompassing Oahu. ArcGIS Pro was then used to determine which of these points had no gridded overlap with the island. A total of 437 points were identified with a nonzero amount of gridded overlap with Oahu. These 437 points were then processed as detailed in subsequent steps to determine the wind capacity factors.

**3** access specific h5 values and add them to csv.py

*This script extracted data for the given 437 points from the h5 file. Since the h5 files contain one year of data, this file must be changed for each yearly h5 you are extracting from. The uploaded script was used to extract the 2019 values for each of the 437 points. This script also calculates the capacity factors for each wind speed value. The script saves the files as year_point.csv
