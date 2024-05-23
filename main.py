import requests
from bs4 import BeautifulSoup
import json

res = requests.get("https://komikindo.co/one-piece-chapter-1/")

soup = BeautifulSoup(res.content, "html.parser")
list = []

for tag in soup.find_all("img", {"data-tai" : True}):
  js = {
    "src" : tag["src"],
    "page" : tag["data-tai"]
  }
  apd = list.append(js)

with open(f"./data.json", "w") as f :
  print("success")
  json.dump(list, f, indent = 4)