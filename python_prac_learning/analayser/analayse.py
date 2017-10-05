import pandas as pd
import matplotlib.pyplot as plt

headers = ["date", "visitors"]
data = pd.read_csv("visitors.csv", skiprows=4, names = headers)
data.head()	

#print(data)

headers = ["date", "visitors_new"]
data_new = pd.read_csv("visitors_new.csv", skiprows=4, names = headers)
data_new.head()	



data_combined = pd.merge(data, data_new)
data_combined.head()

data_combined.sort_values("date", axis=0, ascending=True, inplace=True, kind='quicksort', na_position='last')
#data_combined.sort(["date"])

data_combined.set_index("date", inplace=True)
data_combined.head()

data_combined.plot()
plt.show()


