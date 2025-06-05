import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
with open("books.csv", "r") as datafile:
    data = pd.read_csv(datafile, delimiter=",")

# Get the top 5 most common language codes
language_counts = data['language_code'].value_counts().head(5)

# Map language codes to full language names
language_names = {
    "eng": "English",
    "spa": "Spanish",
    "ger": "German",
    "en-US": "English (US)",
    "en-GB": "English (UK)",
}

# Convert language codes to full names using the dictionary
full_labels = [language_names.get(code, code) for code in language_counts.index]

# Create a pie chart
plt.pie(
    language_counts, 
    labels=full_labels, 
    autopct=lambda pct: f'{pct:.1f}%', textprops={'fontsize': 8},
    colors=sns.color_palette("pastel")
)

# Add title and save the chart
plt.title("What Language Does Your Book Speak?")
plt.axis("equal")
plt.savefig("book_languages_piechart.png")