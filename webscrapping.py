#python D:\WebDevelopment\python\webscrapping.py
numberofMovies=input("enter the number of movies you want to view: ")
number=numberofMovies

url="https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&count="+number

import requests
r=requests.get(url)

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.content,"html.parser")

print("****************************************"+"\n")
for i in soup.findAll("div", class_="lister-item mode-advanced"):
  print("Title: "+i.h3.a.text,end="")
  print(i.find("span", class_="genre").text)
  print("IMDB Rating: "+i.find("strong").text)
  print("Link: "+"https://www.imdb.com"+i.find('a').get("href")+ "\n")
  print("****************************************"+"\n")
  
