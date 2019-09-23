import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DATA_SET_PATH = "F:\\Research\\IEEE SS12\\GLUCOSE.csv" #put your file path dude!
dataset = pd.read_csv(DATA_SET_PATH)
df = pd.DataFrame(dataset)

a=list(reversed(df['Gluc']))
b=list(reversed(df['Malaria']))
t =np.arange(0, 111.0, 1)
data1 = a
data2 = b

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('No. of patients record')
ax1.set_ylabel('Glucose', color=color)
ax1.plot(t, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # initiate a second axes that shares the same x-axis 

color = 'tab:blue'
ax2.set_ylabel('Malaria Presence', color=color)  # we already handled the x-label with axis machan
ax2.plot(t, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped just for correction purpose
plt.show()
