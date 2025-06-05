import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import json
from statsmodels.graphics.mosaicplot import mosaic

with open("data.json", "r") as text:
    data = json.load(text)

for item in data:
  item["Category"] = re.compile(" [\.(]").split(item["Category"])[0]

print(data)