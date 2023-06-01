'''
This file makes a contour plot of the system cost per kWh for each fixed battery/H2 storage condition
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
from matplotlib.colors import ListedColormap
import pickle
import os
import pandas as pd
from matplotlib import ticker
from matplotlib.cm import ScalarMappable



x = [0, 6.66,13.32,20,50,200]
y = [0,3.33,6.66,13.32,20,26.66,33.32]
X, Y = np.meshgrid(y,x)

print(X) #x is battery
print(Y) #y is H2


path = '/Users/Dominic/output_data/1_year_e1_contour/'
os.chdir(path)
#read in the system cost from the case results tab

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


#Make Contour Plot
fig, ax = plt.subplots()
levels = [0.15,0.2,0.25,0.3,0.35,0.4,0.45]


#plt.contourf(X, Y, Z, 10, cmap='OrRd', locator=ticker.LogLocator())
qcs = plt.contourf(X, Y, Z, levels, cmap='OrRd', extend='max')
qcs.cmap.set_over('gray')
plt.colorbar(qcs,label='System Cost ($/kWh)');

#make labels
plt.xlabel('Battery Storage (MWh)')
plt.ylabel('H2 Storage (MWh)')
plt.title('System Cost Under Fixed Battery \n and H2 Storage Conditions')
plt.xticks(np.arange(0, 36, step=6))
plt.yticks(np.arange(0, 201, step=25))
plt.savefig('System Cost Contour Plot.png', dpi=300)
plt.show()
