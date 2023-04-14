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
from matplotlib import ticker


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
        
            print(file_path)
            #all the above values are in GW
            #Account for the fact that 3.9653305GW solar can be built on existing developments, thus taking up no more land
            solar = solar - 3.9653305
            if solar < 0:
                solar = 0
            
            #Account for the fact that (1/6) GW of onwind can be built per GW of solar, since turbines can be built on the same land as PV
            if solar > 0:
                wind = wind - (solar/6)
            else:
                wind = wind

            sys_land = (wind*121.4058)+(solar*20.2343)+(battery*0.092916)+(h2store*0.0046417)+(fuelcell*0.250905)
            print(sys_land)

            #Append the value of sys_land to sys_land_use
            sys_land_use = np.append(sys_land_use, sys_land)

print(sys_land_use)

#Below variable appends the land use cases to an array with one exorbinant value, which represents the 0batt 0h2 case that is infeasible and thus has no pickle file
sys_land_use2 = np.array([100000])
sys_land_use2 = np.append(sys_land_use2, sys_land_use)

print(sys_land_use2)


x = [0, 6.66,13.32,20,50,200]
y = [0, 3.33,6.66,13.32,20,26.66,33.32]
X, Y = np.meshgrid(y,x)

print(X) #x is battery
print(Y) #y is H2


sys_land_use2 = sys_land_use2.reshape(6,7)
print(sys_land_use2)

#Make Contour Plot

#plt.contourf(X, Y, sys_land_use2, 100, cmap='OrRd', locator=ticker.LogLocator())
plt.contourf(X, Y, sys_land_use2, 100, cmap='OrRd')
plt.colorbar(label='System Land Use (km^2)');

#make labels
plt.xlabel('Battery Storage (MWh)')
plt.ylabel('H2 Storage (MWh)')
plt.title('System Land Use Under Fixed Battery \n and H2 Storage Conditions')
plt.xticks(np.arange(0, 36, step=6))
plt.yticks(np.arange(0, 201, step=25))
plt.savefig('System Land Use Contour Plot at origin linear scale.png', dpi=300)
plt.show()
