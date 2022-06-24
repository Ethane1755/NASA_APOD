from bs4 import BeautifulSoup
import requests
import os
from datetime import date

today=date.today()
d=today.strftime('%y%m%d')

RootUrl = "https://apod.nasa.gov/apod"
url = "https://apod.nasa.gov/apod/ap"+d+".html"
html = requests.get(url)

s = BeautifulSoup(html.text, 'lxml')

results=s.find_all("img")
image_links = [result.get("src") for result in results]

for index, link in enumerate(image_links):
    if not os.path.exists("images"):
        os.mkdir("images")
    link=link[:-9]
    img = requests.get(RootUrl+'/'+link+'.jpg')
    with open("images\\"+d+".jpg", "wb") as file:
        file.write(img.content) 
print('NASA APOD of',today.strftime('%Y/%m/%d'),'done.')
print('Press any key to continue...')
input()