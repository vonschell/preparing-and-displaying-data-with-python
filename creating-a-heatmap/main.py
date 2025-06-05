import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

with open("tips.csv", "r") as csvfile:
    tips = pd.read_csv(csvfile, delimiter=",")
    
tips_pivoted = tips.pivot_table(values="tip", index=["size"], columns=["time"])

fig = sns.heatmap(tips_pivoted, annot=True, cmap="Purples")

fig.set_ylim(0,6)

plt.xlabel("Time")
plt.ylabel("Size")
plt.title("Heatmap of Tips($) by Party Size and Time")

plt.savefig("heatmap_tips.png")