import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

with open("books.csv","r") as datafile:
    data = pd.read_csv(datafile,delimiter=",")

language_counts = data['language_code'].value_counts().head(5)

#map language codes to full language names in the dataset
language_names = {
    "eng": "English",
    "spa": "Spanish",   
    "ger": "German",
    "en-US": "English (US)",
    "en-GB": "English (UK)",
}

# Convert language codes to full names using the dictionary
full_labels = [language_names.get(code, code) for code in language_counts.index]
plt.pie(language_counts, labels=full_labels)

plt.title("What Language Does Your Book Speak?")
plt.axis("equal")
plt.savefig("book_languages_piechart.png")