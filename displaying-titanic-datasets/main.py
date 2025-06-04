import csv
import numpy as np
import matplotlib.pyplot as plt
import Seaborn as sns
import pandas as pd

dataframe = pd.read_csv('titanic.csv')

sns.scatterplot(x="Age", y="Fare", hue="Survived", data=dataframe)