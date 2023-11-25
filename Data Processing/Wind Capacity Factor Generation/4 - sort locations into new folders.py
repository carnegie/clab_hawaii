'''
This script will sort all the csv's into new folders based on the
location ID. Thus, all the 23 years of data for each location will
be in one folder
'''

from pathlib import Path
from datetime import datetime
import os

docs = Path("/Users/Dominic/Desktop/Post Edgar WIND Toolkit cfs with leap/")

for file in docs.iterdir():
    print(file)

for file in docs.iterdir():
    directory = file.parent
    extension = file.suffix

    name = file.stem

    year, point = name.split('_')
    print(point)

    new_path = docs.joinpath(point)
    new_name = f'{point} _ {year}{extension}'

    if not new_path.exists():
            new_path.mkdir()
        
    new_file_path = new_path.joinpath(new_name)
    file.replace(new_file_path)