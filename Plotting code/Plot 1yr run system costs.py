'''This code will plot the technology mix of all the 1-year runs from 2006 to 2019 in a stacked bar chart.'''

from __future__ import division
import numpy as np
from os import listdir

import pickle
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import matplotlib.gridspec as gridspec
import matplotlib.ticker as ticker

import datetime
from matplotlib.dates import drange
from matplotlib.ticker import FormatStrFormatter

#Plotting colors
solar_q = 'orange'
wind_q = 'blue'
pgp_q = 'pink'
batt_q = 'purple'

#List for costs
wind_no_pgp = []
solar_no_pgp = []
batt_no_pgp = []

wind_pgp = []
solar_pgp = []
batt_pgp = []
pgp_pgp = []

#Input paths for pickle files
no_pgp_2006 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/No PGP/Outputs/one_year_2006_no_normal_no_pgp_output.pickle'
yes_pgp_2006 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/Yes PGP/Outputs/one_year_2006_no_normal_yes_pgp_output.pickle'
no_pgp_2007 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/No PGP/Outputs/one_year_2007_no_normal_no_pgp_output.pickle'
yes_pgp_2007 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/Yes PGP/Outputs/one_year_2007_no_normal_yes_pgp_output.pickle'
no_pgp_2008 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/No PGP/Outputs/one_year_2008_no_normal_no_pgp_output.pickle'
yes_pgp_2008 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/Yes PGP/Outputs/one_year_2008_no_normal_yes_pgp_output.pickle'
no_pgp_2009 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/No PGP/Outputs/one_year_2009_no_normal_no_pgp_output.pickle'
yes_pgp_2009 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/Yes PGP/Outputs/one_year_2009_no_normal_yes_pgp_output.pickle'
no_pgp_2010 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/No PGP/Outputs/one_year_2010_no_normal_no_pgp_output.pickle'
yes_pgp_2010 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/Yes PGP/Outputs/one_year_2010_no_normal_yes_pgp_output.pickle'
no_pgp_2011 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/No PGP/Outputs/one_year_2011_no_normal_no_pgp_output.pickle'
yes_pgp_2011 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/Yes PGP/Outputs/one_year_2011_no_normal_yes_pgp_output.pickle'
no_pgp_2012 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/No PGP/Outputs/one_year_2012_no_normal_no_pgp_output.pickle'
yes_pgp_2012 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/Yes PGP/Outputs/one_year_2012_no_normal_yes_pgp_output.pickle'
no_pgp_2013 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/No PGP/Outputs/one_year_2013_no_normal_no_pgp_output.pickle'
yes_pgp_2013 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/Yes PGP/Outputs/one_year_2013_no_normal_yes_pgp_output.pickle'
no_pgp_2014 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/No PGP/Outputs/one_year_2014_no_normal_no_pgp_output.pickle'
yes_pgp_2014 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/Yes PGP/Outputs/one_year_2014_no_normal_yes_pgp_output.pickle'
no_pgp_2015 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/No PGP/Outputs/one_year_2015_no_normal_no_pgp_output.pickle'
yes_pgp_2015 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/Yes PGP/Outputs/one_year_2015_no_normal_yes_pgp_output.pickle'
no_pgp_2016 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/No PGP/Outputs/one_year_2016_no_normal_no_pgp_output.pickle'
yes_pgp_2016 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/Yes PGP/Outputs/one_year_2016_no_normal_yes_pgp_output.pickle'
no_pgp_2017 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/No PGP/Outputs/one_year_2017_no_normal_no_pgp_output.pickle'
yes_pgp_2017 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/Yes PGP/Outputs/one_year_2017_no_normal_yes_pgp_output.pickle'
no_pgp_2018 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/No PGP/Outputs/one_year_2018_no_normal_no_pgp_output.pickle'
yes_pgp_2018 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/Yes PGP/Outputs/one_year_2018_no_normal_yes_pgp_output.pickle'
no_pgp_2019 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/No PGP/Outputs/one_year_2019_no_normal_no_pgp_output.pickle'
yes_pgp_2019 = '/Users/Dominic/Desktop/Experiment Runs With Up-To-Date Inputs/PGP vs No PGP Reliability/Normalized/Yes PGP/Outputs/one_year_2019_no_normal_yes_pgp_output.pickle'

#make a list with the names of all the no_pgp runs
list_no_pgp= [no_pgp_2006, no_pgp_2007, no_pgp_2008, no_pgp_2009, no_pgp_2010, no_pgp_2011, no_pgp_2012, no_pgp_2013, no_pgp_2014, no_pgp_2015, no_pgp_2016, no_pgp_2017, no_pgp_2018, no_pgp_2019]

#make a list with the names of all the yes_pgp runs
list_yes_pgp= [yes_pgp_2006, yes_pgp_2007, yes_pgp_2008, yes_pgp_2009, yes_pgp_2010, yes_pgp_2011, yes_pgp_2012, yes_pgp_2013, yes_pgp_2014, yes_pgp_2015, yes_pgp_2016, yes_pgp_2017, yes_pgp_2018, yes_pgp_2019]


#Add system components to the cost lists
for run in list_no_pgp:
    with open(run, 'rb') as f:
        data = pickle.load(f)
        component_results = data['component results']
        spending = component_results['Capital Expenditure']
        gen = spending['Generator']
        wind = gen['onwind']
        solar = gen['solar']
        batt = spending['StorageUnit']
        battery = batt['battery']

        case_results = data['case results']
        objective = case_results['objective [$]']
        print(objective)
        hourly_cost = case_results['system cost [$/h]']
        print(hourly_cost)

        wind_cost = wind * (hourly_cost/objective) / 1000
        solar_cost = solar * (hourly_cost/objective) / 1000
        battery_cost = battery * (hourly_cost/objective) / 1000

        wind_no_pgp = np.append(wind_no_pgp, wind_cost)
        solar_no_pgp = np.append(solar_no_pgp, solar_cost)
        batt_no_pgp = np.append(batt_no_pgp, battery_cost)

#Add system components to the cost lists
for run in list_yes_pgp:
    with open(run, 'rb') as f:
        data = pickle.load(f)
        component_results = data['component results']
        spending = component_results['Capital Expenditure']
        gen = spending['Generator']
        wind = gen['onwind']
        solar = gen['solar']
        batt = spending['StorageUnit']
        battery = batt['battery']
        h2 = spending['Store']
        h2store = h2['h2_storage']
        cell = spending['Link']
        fuelcell = cell['fuel_cell']
        electrolysis = cell['electrolysis']


        case_results = data['case results']
        objective = case_results['objective [$]']
        hourly_cost = case_results['system cost [$/h]']

        wind_cost = wind * (hourly_cost/objective) / 1000
        solar_cost = solar * (hourly_cost/objective) / 1000
        battery_cost = battery * (hourly_cost/objective) / 1000
        pgp_cost = (h2store + fuelcell + electrolysis) * (hourly_cost/objective) / 1000

        wind_pgp = np.append(wind_pgp, wind_cost)
        solar_pgp = np.append(solar_pgp, solar_cost)
        batt_pgp = np.append(batt_pgp, battery_cost)
        pgp_pgp = np.append(pgp_pgp, pgp_cost)

print(wind_no_pgp + solar_no_pgp + batt_no_pgp)
print(wind_pgp + solar_pgp + batt_pgp + pgp_pgp)

#Make stacked bar plots with the capacity of each system component on the y axis and year on the x axis. Each year will have two bars, one for the no_pgp and one for the yes_pgp
fig, ax = plt.subplots()
index = np.arange(14)
bar_width = 0.35
opacity = 0.8
p1 = plt.bar(index, wind_no_pgp, bar_width, alpha=opacity, color=wind_q, label='Wind')
p2 = plt.bar(index, solar_no_pgp, bar_width, alpha=opacity, color=solar_q, label='Solar', bottom=wind_no_pgp)
p3 = plt.bar(index, batt_no_pgp, bar_width, alpha=opacity, color=batt_q, label='Battery', bottom=wind_no_pgp+solar_no_pgp)
p4 = plt.bar(index+bar_width, wind_pgp, bar_width, alpha=opacity, color=wind_q, label='Wind')
p5 = plt.bar(index+bar_width, solar_pgp, bar_width, alpha=opacity, color=solar_q, label='Solar', bottom=wind_pgp)
p6 = plt.bar(index+bar_width, batt_pgp, bar_width, alpha=opacity, color=batt_q, label='Battery', bottom=wind_pgp+solar_pgp)
p7 = plt.bar(index+bar_width, pgp_pgp, bar_width, alpha=opacity, color=pgp_q, label='PGP', bottom=wind_pgp+solar_pgp+batt_pgp)

plt.xlabel('Year')
plt.ylabel('Cost ($/kWh)')
plt.title('Cost of System Per 1-Year \nOptimization With and Without PGP')
plt.ylim(0, 0.18)

plt.xticks(index + bar_width/2, ('2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013','2014', '2015', '2016', '2017', '2018', '2019'))
ax.tick_params(axis='x', pad=13)
ax.tick_params(axis='x', which='both',length=0) #make x-axis tickmarks invisible

for tick in ax.get_xticklabels():
    tick.set_rotation(45)

plt.legend((p1[0], p2[0], p3[0], p7[0]), ('Wind', 'Solar', 'Battery', 'PGP'),bbox_to_anchor=(1, 0.6)) #add only one legend entry for each type of system component


#put a line of text under the x axis to label the two sets of bars
plt.text(0.055, -0.03, '–', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=9)
plt.text(0.078, -0.03, '+', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=8)

plt.text(0.122, -0.03, '–', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=9)
plt.text(0.145, -0.03, '+', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=8)

plt.text(0.187, -0.03, '–', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=9)
plt.text(0.210, -0.03, '+', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=8)

plt.text(0.252, -0.03, '–', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=9)
plt.text(0.275, -0.03, '+', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=8)

plt.text(0.319, -0.03, '–', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=9)
plt.text(0.342, -0.03, '+', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=8)

plt.text(0.385, -0.03, '–', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=9)
plt.text(0.408, -0.03, '+', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=8)

plt.text(0.454, -0.03, '–', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=9)
plt.text(0.477, -0.03, '+', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=8)
         
plt.text(0.519, -0.03, '–', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=9)
plt.text(0.542, -0.03, '+', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=8)

plt.text(0.586, -0.03, '–', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=9)
plt.text(0.609, -0.03, '+', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=8)

plt.text(0.652, -0.03, '–', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=9)
plt.text(0.675, -0.03, '+', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=8)

plt.text(0.719, -0.03, '–', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=9)
plt.text(0.742, -0.03, '+', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=8)

plt.text(0.785, -0.03, '–', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=9)
plt.text(0.808, -0.03, '+', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=8)

plt.text(0.852, -0.03, '–', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=9)
plt.text(0.875, -0.03, '+', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=8)

plt.text(0.919, -0.03, '–', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=9)
plt.text(0.942, -0.03, '+', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=8)

#plt.savefig('C:\\Users\\Dominic\\desktop\\Oahu Results\\capacity_1_yr_runs.png', dpi=300, bbox_inches='tight')