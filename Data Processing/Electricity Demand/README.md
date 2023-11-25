This folder explains how the electricity demand input file was generated

1 - Download the FERC reporting data (https://www.ferc.gov/industries-data/electric/general-information/electric-industry-forms/form-no-714-annual-electric/data). At the time of this typing, electronic filing data is available from 2006-2020.

2 - Open the csv "Part 3 Schedule 2 - Planning Area Hourly Demand". Hawaiian Electric is respondent ID 178. This can be found on the "Respondent IDs" csv. Filter the data so that any row without "178" in cell A is removed. This will give you the values for only Hawaiian Electric. Use the "TOCOL" function in excel to sequentially append all the demand values into one column. Save this column in a new csv. This information is the total demand satisfied by Hawaiian electric per hour over the 2006-2020 time period.

3 - Mutliply each value by (1614.5/2168.1). This demand adjustment is based on Oahu's firm generation capacity divided Hawaiian Electric's overall firm generation capacity. These values come from the 2/15/2023 Hawaiian Electric Power Facts statement (https://www.hawaiianelectric.com/about-us/power-facts), the most recent statement available at the time of this typing. 

4 - Determine demand points that are erroneous.py

* This script identifies outliers in the data by computing the median and iqr and using q1-1.5iqr or q3+1.5iqr as the limit for non-outlier data.
It then performs regression imputation to replace those outliers with appropriate values. This is the final step in generating demand input file.
