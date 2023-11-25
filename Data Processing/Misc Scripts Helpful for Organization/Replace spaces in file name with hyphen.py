import os
import sys

directory = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Fourteen Year Runs w Lost Load/No PGP/'

for filename in os.listdir(directory):
    if filename.endswith(".xlsx"):
        full_path = os.path.join(directory, filename)  # Get the full path to the file
        new_filename = filename.replace(" ", "_")
        new_full_path = os.path.join(directory, new_filename)  # Get the full path for the new filename
        os.rename(full_path, new_full_path)  # Rename the file using the full paths
    else:
        continue