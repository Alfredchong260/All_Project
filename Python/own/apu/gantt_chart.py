import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import timedelta
import chardet

# Read the file and get the data
data = pd.read_excel('./schedule.xlsx')

# Convert the data type to datetime
data['Start'] = pd.to_datetime(data['Start'], format="%Y_%m_%d")
data['End'] = pd.to_datetime(data['End'], format="%Y_%m_%d")

# sort tasks by start date
data.sort_values("Start", axis=0, ascending=True, inplace=True)
# reset index inplace
data.reset_index(drop=True, inplace=True)

# add duration column
data['Duration'] = data['End'] - data['Start'] + timedelta(days=1)

# add colume: start date of each task wrt the project daty 1
data['PastTime'] = data['Start'] - data['Start'][0]

# start drawing the graph
nrow = len(data)
plt.figure(num=1, figsize=[8, 5], dpi=100)
bar_width = 0.9

for i in range(nrow):
    i_rev = nrow - 1 - i

    # plot the last task first
    plt.broken_barh([(data['Start'][i_rev], data['Duration'][i_rev])], (i - bar_width / 2, bar_width), color="b")
    plt.broken_barh([(data['Start'][0], data['PastTime'][i_rev])], (i - bar_width / 2, bar_width), color="#f2f2f2")

y_pos = np.array(nrow)
# plt.yticks(y_pos, labels=reversed(data["Task"]))
print(data['Task'])
# plt.show()
    
