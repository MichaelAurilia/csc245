import matplotlib
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


import warnings
warnings.filterwarnings('ignore')

df_pit=pd.read_csv('Pitching Stats.csv')

print(df_pit.head(3))
print(df_pit.info())

pit_col2 = ['Win', 'Loss', 'Games played', 'Games Started', 'Complete Game', 'Shutout', 'Save',
            'Save Opportunity', 'Innings pitched', 'hit', 'run', 'earned run',
            'home run', ' Hit Batsmen', 'base on balls', 'Strikeouts', 'WHIP',
            'AVG']
fig = plt.figure(figsize=(10, 10))

for i in range(len(pit_col2)):
    plt.subplot(5, 4, i + 1)
    sns.scatterplot(df_pit, x=df_pit[pit_col2[i]], y=df_pit['Earned run Average'])
    plt.title(pit_col2[i], fontsize=12)

plt.tight_layout()
plt.show()




