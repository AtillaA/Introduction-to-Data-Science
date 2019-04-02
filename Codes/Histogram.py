import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv ('C:\\Users\\..\\vgsales-edited. csv')

sns.set_palette ('deep' , desat = .6)
sns.set context (rc = {"figure.figsize": (8,4)})

fig = plt.figure()
fig.suptitle('Global Video Game Release Per Year', fontsize = 20)

plt.hist(df.Year.dropna (), bins = 41) 
plt.xlabel('Year', fontsize= 20) 
plt.ylabel('Amount' , fontsize= 20)

plt.show ()
