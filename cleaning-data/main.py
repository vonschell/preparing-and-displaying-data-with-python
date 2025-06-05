import json
import re

with open("data.json", "r") as text:
    data = json.load(text)
    
for item in data:
    item["category"] = re.compile(" [\.(]").split(item["category"])[0]
    
    print(data)