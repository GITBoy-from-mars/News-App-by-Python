import requests
import json
Query = input("Enter topic of News: ")
url = f"q={Query} Your API key"

r = requests.get(url)
# print(r.text)
news = json.loads(r.text)

for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print("------------------------------------------------------------------\n") # seperator
