import matplotlib.pyplot as plt

snack_scores = [80,45,34]

slice_labels = ["Chocolate", "Cheese", "Pickles"]

colors = ["D2691E", "#ff7f50", "#8A2BE2"]

plt.pie(snack_scores, labels=slice_labels)

plt.title("Snack Scores", fontsize=22)

plt.savefig("snack_scores.png")

