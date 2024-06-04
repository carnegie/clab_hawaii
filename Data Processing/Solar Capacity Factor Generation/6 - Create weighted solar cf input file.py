'''This script will weight the different input files and add their weighted values to produce one weighted average csv file.'''
#Import modules
import pandas as pd
import numpy as np
import os
from pathlib import Path
from datetime import datetime
import csv

#Create path to folder with all the solar capacity factor csv files
docs = Path("/Users/covel/OneDrive/Desktop/Solar Pypsa Format Indiv Locations/")
# Define the directory containing the CSV files
directory = r"C:\Users\covel\OneDrive\Desktop\Solar Pypsa Format Indiv Locations"

weight = Path("/Users/covel/OneDrive/Desktop/Solar Weights.csv")


#Ensures all values are >=1

# Function to process values, ensuring non-numeric values are handled
def process_value(value):
    try:
        # Convert the value to a float
        num = float(value)
        # Return the minimum of the value and 1
        return min(num, 1)
    except ValueError:
        # If conversion fails, return the original value
        return value

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        # Construct the full file path
        file_path = os.path.join(directory, filename)
        
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Process column E (assuming column E is the 5th column, index 4) from row 7 onwards (index 6)
        df.iloc[6:, 4] = df.iloc[6:, 4].apply(process_value)
        
        # Save the processed CSV file back to the same path
        df.to_csv(file_path, index=False)

print("Done")





#Read in the 4th column of the weight csv file starting at row 2
read_weight = pd.read_csv(weight, sep=",", usecols=[3], skiprows=0)
#print(read_weight)

#read in the first column of the weight csv file starting at row 2
read_weight_location = pd.read_csv(weight, sep=",", usecols=[0], skiprows=0)
#print(read_weight_location)


#print(read_weight_location.iloc[1,0])
#print(read_weight.iloc[1,0])


combined_values = pd.DataFrame()

#ensuring that the correct file is being chosen for the correct weighting
for file in docs.iterdir():
    print(file)
for i in range(108):
    print(read_weight_location.iloc[i][0])
    print(read_weight.iloc[i][0])
    
    

for file in docs.iterdir():
    print(file)
    data = pd.read_csv(file, sep=",")
    combined_values[file.stem[0:5]] = data.iloc[5:,4]
    combined_values[file.stem[0:5]] = combined_values[file.stem[0:5]].astype(float)
    
print(combined_values)

print(combined_values.dtypes)

for i in range(108):
    #multiply the combined_values[read_weight_location[i][0]] by read_weight.iloc[i][0]
    
    combined_values[str(read_weight_location.iloc[i][0])] = combined_values[str(read_weight_location.iloc[i][0])] * read_weight.iloc[i][0]

#Sum the values in each row
combined_values['Sum'] = combined_values.sum(axis=1)
print(combined_values)

#Save combined_values['Average'] to a new csv file
new_file = 'Weighted Solar CFs.csv'
combined_values.to_csv(new_file, sep=",", index = False, columns=['Sum'])