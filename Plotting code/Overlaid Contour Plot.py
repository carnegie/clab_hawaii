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
X1,Y1 =np.meshgrid(y,x)

print(X) #x is battery
print(Y) #y is H2


sys_land_use2 = sys_land_use2.reshape(6,7)
print(sys_land_use2)


cost = pd.DataFrame()

def read_text_file(file_path):
    with open(file_path, 'rb') as f:
        global cost
        data = pickle.load(f)
        case_data = data['case results']
        system_cost = case_data['system cost [$/h]']
        system_cost_kwh = system_cost/1000
        cost = pd.concat([cost, system_cost_kwh], axis=0)
        
file_count = 0        
# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".pickle"):
        file_path = f"{path}\{file}"

        #count the number of files
        file_count += 1
  
        # call read text file function
        read_text_file(file_path)

#Rename the columns of cost
cost.columns = ['System Cost [$/kWh]']

#Create an array of the system cost
Z = np.array([10])
for i in range(0, file_count):
    #Append the system cost to the array
    Z = np.append(Z, [cost['System Cost [$/kWh]'].values[i]])
print(Z)

#Reshape the array to match the meshgrid
Z = Z.reshape(6,7)
print(Z)

levels = [0.15,0.2,0.25,0.3,0.35,0.4,0.45]
levels2 = [25, 50, 75, 100, 125, 150, 175, 200]
qcs = plt.contourf(X, Y, Z, levels, cmap='RdPu', extend='max', alpha = 1)
qcs.cmap.set_over('gray')


qcs2 = plt.contourf(X1, Y1, sys_land_use2, levels2, cmap='OrRd', extend='max', alpha=0.6)
qcs2.cmap.set_over('gray')
plt.colorbar(qcs2, label='System Land Use (km^2)', pad=0.1);
plt.colorbar(qcs,label='System Cost ($/kWh)');
plt.title('Overlaid System Costs and System Land Use', x=0.71,y=1.07)
plt.xlabel('Battery Storage (MWh)')
plt.ylabel('H2 Storage (MWh)')
plt.savefig('Overlaid Contour Plot.png', dpi=300)
plt.show()