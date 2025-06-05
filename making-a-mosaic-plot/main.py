import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import json
from statsmodels.graphics.mosaicplot import mosaic

# Load data from JSON file
with open("data.json", "r") as text:
  data = json.load(text)

# Clean and preprocess the "Category" field
for item in data:
  item["Category"] = re.compile(r" [\.(]").split(item["Category"])[0]

print(data)

# Define classes and statuses to filter data
classes = ["Mammalia", "Aves", "Reptillia"]
statuses = ["Endangered", "Critically endangered", "Vulnerable"]

# Filter data for mosaic plot
mosaic_data = []
for item in data:
  if item["Animal Class"] in classes and item["Category"] in statuses:
    mosaic_data.append(item)

# Define properties for the mosaic plot
properties = {
  "Endangered": {"color": "#FACDB6"},
  "Critically endangered": {"color": "#C5CADE"},
  "Vulnerable": {"color": "#A8DBD2"},
}

# Set font size for the plot
plt.rc("font", size=8)

# Create a DataFrame for the mosaic plot
mosaic_dataframe = pd.DataFrame(mosaic_data)

# Generate the mosaic plot
fig = mosaic(
  mosaic_dataframe,
  ["Category", "Animal Class"],
  title="Conservation Status by Animal Class",
  gap=[0.02, 0.02],
  axes_label=True,
  properties=lambda x: properties[x[0]],
)

