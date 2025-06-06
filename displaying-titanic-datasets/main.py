import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

dataframe = pd.read_csv('titanic.csv')
dataframe = dataframe.replace({"Survived": {0: "Did Not Survive", 1: "Survived"}})

sns.scatterplot(x="Age", y="Fare", hue="Survived", data=dataframe)

plt.xlabel("Passenger Age")
plt.ylabel("Passenger Fare")
plt.title("Titanic Passenger Age vs Fare")

plt.savefig("titanic.png")