#Importing seaborn, matplotlib, pandas, numpy, and requests. Note that from matplotlib pyplot is called and shortened (you can also shortern pyplot to p in certain cases).
import requests
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

#Source of the data.
data_url = "https://data.cityofnewyork.us/resource/uip8-fykc.json"

#Requesting the data for use. Generates a seperate json file.
r = requests.get(data_url)

#"Opens" the data.
with open("uip8-fykc.json", "w") as f: 
  f.write(r.text)

df = pd.read_json("uip8-fykc.json")
print(df.head())

#Prints out the longitudinal and latidudinal correlation calculation. Many arrests appear to concentrate in the same areas.
print("___")
print("The correlation is: ", np.corrcoef(df['longitude'], df['latitude'])[0,1])
print("___")

#Seaborn helps to plot the data on the scatterplot.
sns.lmplot(
    "longitude","latitude", df
).set_axis_labels("longitude", "latitude")

#Generates the plot. If explained to a layman, one could say that this essentially works like a print statement. 
plt.title("NYPD Arrests 2021")
plt.tight_layout()
plt.show()
