The process to collect solar irradiation data from the NSRDB specific to Oahu, then convert the data into capacity factors is outlined in this folder.

1 - Download solar data from the NSRDB data viewer (https://nsrdb.nrel.gov/data-viewer). With this interactive map tool, you can create a polygon from points surrounding Oahu and download data from every point within the polygon. The "USA & Americas (30, 60min / 4km / 1998-2022)" dataset was selected. ArcGIS Pro was used to create a 4km grid around Oahu and determine which points included in the download had no gridded overlap with the island. A total of 108 points were identified with a nonzero amount of gridded overlap with Oahu. These 108 points were then processed as detailed in subsequent steps to determine the solar capacity factors. Each year of data for each point is downloaded as a separate csv.

2 - 
