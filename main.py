import requests
from bs4 import BeautifulSoup
import json

###res = requests.get("https://komikindo.co/solo-leveling-side-story-chapter-01/")

"""soup = BeautifulSoup(res.content, "html.parser")
list = []

for tag in soup.find_all("img", {"data-tai" : True}):
  js = {
    "src" : tag["src"],
    "page" : tag["data-tai"]
  }
  apd = list.append(js)

with open(f"./data.json", "w") as f :
  print("success")
  json.dump(list, f, indent = 4)"""
  
def manga_read(name : str) :
  split = name.split()
  join = "-".join(split)
  res =  requests.get(f"https://komikindo.co/manga/{join}/")
  data = []
  soup = BeautifulSoup(res.text, "html.parser")
  def get_total_chapter() :
    
     for i in soup.find_all("li", {"data-num" : True}):
       find_chapter = i.find("a", {"href" : True})
       jsons = {
         "total_chapter" : find_chapter.text
       }
       return jsons
  jsons = {
    "title" : soup.find("h1", class_="entry-title").text,
    "statistic" : get_total_chapter()
  }
  data.append(jsons)
  with open("data.json", "w") as f :
    json.dump(data, f, indent=4)
manga_read("one piece")