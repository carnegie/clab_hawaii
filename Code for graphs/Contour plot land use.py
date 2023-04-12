'''
This file makes a contour plot of the land use for each fixed battery/H2 storage condition
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
from matplotlib.colors import ListedColormap
import pickle
import os
import pandas as pd


path = '/Users/Dominic/output_data/1_year_e1_contour/'
os.chdir(path)

file_count = 0   
sys_land_use = np.array([])     
# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".pickle"):
        file_path = f"{path}\{file}"

        #count the number of files
        file_count += 1


        #read in the system cost from the component results tab
        with open(file, 'rb') as f:
            data = pickle.load(f)
            component_results = data['component results']
            #print(component_results)
            land_use = component_results['Optimal Capacity']
            #print(land_use)
            gen = land_use['Generator']
            #print(gen)
            wind = gen['onwind']
            #print(wind)
            solar = gen['solar']
            #print(solar)
            batt = land_use['StorageUnit']
            #print(batt)
            battery = batt['battery']
            #print(battery)
            h2 = land_use['Store']
            #print(h2)
            h2store = h2['h2_storage']
            #print(h2store)
            cell = land_use['Link']
            #print(cell)
            fuelcell = cell['fuel_cell']
            #print(fuelcell)
        
            sys_land = (wind*121.4058)+(solar*20.2343)+(battery*0.092916)+(h2store*0.0046417)+(fuelcell*0.250905)
            print(sys_land)
        
            #Append the value of sys_land to sys_land_use
            sys_land_use = np.append(sys_land_use, sys_land)

print(sys_land_use)


x = [0, 6.66,13.32,20]
y = [6.66,13.32,20]
X, Y = np.meshgrid(y,x)

print(X) #x is battery
print(Y) #y is H2


sys_land_use = sys_land_use.reshape(4,3)
print(sys_land_use)

#Make Contour Plot

plt.contourf(X, Y, sys_land_use, 4, cmap='OrRd')
plt.colorbar(label='System Land Use (km^2)');

#make labels
plt.xlabel('Battery Storage (MWh)')
plt.ylabel('H2 Storage (MWh)')
plt.title('System Land Use Under Fixed Battery \n and H2 Storage Conditions')
plt.xticks(np.arange(6.66, 21, step=4))
plt.yticks(np.arange(0, 21, step=5))
#plt.savefig('System Land Use Contour Plot.png', dpi=300)
plt.show()
