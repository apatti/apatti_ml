import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('movie_metadata.csv')
#print(data[data['language']=='Telugu'])
print("Types:")
print(data.dtypes)
data = data.dropna(subset=['budget'])
data = data[data['language']=='English']
#data['genres']=data['genres'].str.replace('|','\n')
med = data.groupby(['title_year'])['duration'].median()
print(med)

plt.figure()
#ax = med.plot(kind="bar",title="Median Duration vs Year",color=['red','yellow','maroon','orange','green','cyan'])
ax = med.plot(title="Median Duration of English movies over the years",color="Red")
ax.set_xlabel("Year")
ax.set_ylabel("Median Duration (Minutes)")
plt.show()
#print(data.groupby(['genres'])['budget'].median().sort(ascending=False))
        

