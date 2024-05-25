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
  
def get_manga(name : str) :
  try : 
   split = name.split()
   join = "-".join(split)
   res =  requests.get(f"https://komikindo.co/manga/{join}/")
   data = []
   soup = BeautifulSoup(res.text, "html.parser")

   def get_total_chapter() :
    
     for i in soup.find_all("div", {"id" : "chapterlist"}):
       
       jsons = {
         "total_chapter" : len(i.find_all("li", {"data-num" : True})),
         "new_chapter" : soup.find("span", {"class" : "epcur epcurlast"}).text
       }
       return jsons

   def get_description() :
    get_data = soup.find("tbody").find_all("td")
    komikindo = soup.find("i", {"itemprop" : "name"})
    desc = soup.find("div", {"itemprop" : "description"})
    jsons = {
      "about" : desc.find("p").text,
      "status" : get_data[1].text,
      "type" : get_data[3].text,
      "released" : get_data[5].text,
      "author" : get_data[7].text,
      "postedOn" : get_data[11].find("time").text,
      "postedBy" : komikindo.text,
    }
    return jsons
    
    

   jsons = {
    "url" : res.url,
    "title" : soup.find("h1", class_="entry-title").text,
    "description" : get_description(),
    "statistic" : get_total_chapter()
  }
   data.append(jsons)
   with open("data.json", "w") as f :
    json.dump(data, f, indent=4)
    if data == [] :
      print("Error Manga Tidak Ditemukan")
    else :
      print("Scraping Manga Success")
  except Exception as e :
    print("Error Manga Tidak Ditemukan")

def get_chapter(name : str, chapter : int) :
  try :
   split = name.split()
   join = "-".join(split)
   data = []
   res =  requests.get(f"https://komikindo.co/{join}-chapter-{str(chapter)}/")
   soup = BeautifulSoup(res.content, "html.parser")
   for i in soup.find_all("img", {"data-tai" : True}) :
    
     jsons = {
      "src" : i["src"],
      "page" : i["data-tai"]
    }
     data.append(jsons)
   with open("get_chapter.json", "w") as f :
    json.dump(data, f, indent=4)
    if data == [] :
      print("Error Chapter Tidak Ditemukan")
    else :
      print("Scraping Chapter Success")
  except Exception as e :
    print("Error ", e)
    
    
def all_manga(name : str, chapter : int) :
  get_chapter(name, chapter)
  get_manga(name)

  
all_manga("one piece", 120)