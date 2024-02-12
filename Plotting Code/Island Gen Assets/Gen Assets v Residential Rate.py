import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,10))
ax1 = plt.subplot2grid((1, 1), (0, 0), colspan=1, rowspan=1)
index = np.arange(2)  # Adjusted for two bars
bar_width = 0.7
opacity = 1

# Adjusting the data to match the previous example
values = [0.30, 0.145]  # Values for Diesel Only and Diesel, Natural Gas, and/or Coal
std_devs = [0.181, 0.074]  # Standard deviations

# Plotting the bars with capped error bars
p1 = ax1.bar(index[0], values[0], bar_width, yerr=std_devs[0],
             color='red', alpha=0.8, label='Diesel Only',
             error_kw=dict(elinewidth=2, ecolor='black', capsize=10))
p2 = ax1.bar(index[1], values[1], bar_width, yerr=std_devs[1],
             color='blue', alpha=0.8, label='Diesel, Natural Gas, and/or Coal',
             error_kw=dict(elinewidth=2, ecolor='black', capsize=10))

# Adding a black border to the bars
for bar in (p1 + p2):
    bar.set_linewidth(1)
    bar.set_edgecolor('black')

# Annotating statistical significance
x1, x2 = index  # x positions for the two groups
y, h, col = max(values) + 0.21, 0.02, 'black'  # y position, height of the line, color

ax1.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
ax1.text((x1+x2)*.5, y+h, "*", ha='center', va='bottom', color=col, fontsize=20)


plt.ylabel('Residential Rate ($/kWh)', fontsize=14)
plt.title('Island Fossil Fuel\nGeneration Assets vs.\nResidential Rate', y=1.015, fontsize=30)
plt.ylim(0, 0.55)  # Adjusting y-limit to accommodate the data and error bars
plt.xlim(-0.5, 1.5)  # Adjusting x-limit to properly space the bars
plt.xticks(index, ['Diesel Only', 'Diesel with\nNatural Gas\nand/or Coal'])  # Setting custom x-tick labels

# Setting major ticks
plt.yticks(np.arange(0, 0.56, 0.1), fontsize=12)

# Adding subticks without labels
ax1.set_yticks(np.arange(0, 0.56, 0.05), minor=True)

# Customizing the plot's aesthetics
ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
for item in ([ax.xaxis.label, ax.yaxis.label] + ax.get_xticklabels() + ax.get_yticklabels()):
    item.set_fontsize(24)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

ax.yaxis.label.set_fontsize(26)

plt.savefig('C:\\Users\\covel\\OneDrive\\desktop\\Oahu Results\\Island Gen Assets.jpg', dpi = 900, bbox_inches='tight')
plt.show()


from scipy import stats

# Diesel Only group statistics
mean_diesel_only = 0.3
std_dev_diesel_only = 0.181
n_diesel_only = 27

# Diesel with Natural Gas and Coal group statistics
mean_diesel_ng_coal = 0.145
std_dev_diesel_ng_coal = 0.074
n_diesel_ng_coal = 4

# Calculate the t-statistic and the p-value for the two independent samples
t_stat, p_value = stats.ttest_ind_from_stats(mean1=mean_diesel_only, std1=std_dev_diesel_only, nobs1=n_diesel_only,
                                             mean2=mean_diesel_ng_coal, std2=std_dev_diesel_ng_coal, nobs2=n_diesel_ng_coal,
                                             equal_var=False)

t_stat, p_value