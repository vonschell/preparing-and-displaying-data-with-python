import csv
import numpy as np

# ADD CODE: Convert titanic1.csv
with open("titanic1.csv", "r") as file:
  data = csv.reader(file,delimiter=",")
  headers = next(data)
  data_list = list(data)
  titanic_data1 = np.array(data_list)

# ADD CODE: Convert titanic2.csv 
with open("titanic2.csv", "r") as file:
  data = csv.reader(file,delimiter=",")
  headers = next(data)
  data_list = list(data)
  titanic_data2 = np.array(data_list)

# ADD CODE: Merge two datasets


# ADD CODE: Print out shape and number of dimensions of merged dataset