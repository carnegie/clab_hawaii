import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import seaborn as sns
from pathlib import Path
import os
from scipy.stats import linregress

sns.set(style='ticks')

HI_wind = Path("/Users/Dominic/Desktop/WIND weighted average Oahu wind cfs 2006-2019.csv")
HI_solar = Path("/Users/Dominic/Desktop/NSRDB weighted average Oahu solar cfs 2006-2019.csv")
output_path = '/Users/Dominic/desktop/Oahu Results'

# Read in the data
df_wind = pd.read_csv(HI_wind, header=5, usecols=[4])
df_solar = pd.read_csv(HI_solar, header=5, usecols=[4])

# Take the mean of every 24 rows (every day) of df
df_wind = df_wind.groupby(np.arange(len(df_wind)) // 24).mean()
df_solar = df_solar.groupby(np.arange(len(df_solar)) // 24).mean()

# Calculate the regression line
x = np.array(df_solar)
y = np.array(df_wind)
slope, intercept, r_value, p_value, std_err = linregress(x[:, 0], y[:, 0])
regression_line = slope * np.array(x) + intercept

# Calculate the R-squared value
r_squared = r_value ** 2

fig, ax = plt.subplots(figsize=(8, 8))
ax = plt.subplot2grid((1, 1), (0, 0), colspan=1, rowspan=1)
# Plot the scatterplot of data points
sns.scatterplot(data=pd.DataFrame({'x': x[:, 0], 'y': y[:, 0]}), x='x', y='y', ax=ax, color='royalblue')

ax.set_xticks(np.arange(0, 0.351, 0.05))
ax.set_ylim(-0.04, 1.25)
ax.set_yticks(np.arange(0, 1.21, 0.2))


# Plot the regression line
ax.plot(x, regression_line, color='black', label=f'y = {slope:.2f}x + {intercept:.2f}  | $R^2$ = {r_squared:.6f}')



ax.set_xlabel('Solar Capacity Factor', fontsize=26, labelpad=10)
ax.set_ylabel('Corresponding\nWind Capacity Factor', fontsize=26,labelpad=10)
ax.set_title('Capacity Factors\nAveraged Per Day', fontsize=28, pad=15)
ax.tick_params(axis='both', which='major', labelsize=24)
ax.tick_params(axis='x', rotation=45)
plt.legend(loc='upper right',fontsize=20)
plt.tight_layout()
plt.savefig(os.path.join(output_path, 'Average Solar and Wind Capacity Factors Per Day Over 14-Year Period.png'), dpi=300, bbox_inches='tight')
plt.show()
