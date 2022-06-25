from bs4 import BeautifulSoup
import requests
import os
from datetime import date

today=date.today()
d=today.strftime('%y%m%d')

RootUrl = "https://apod.nasa.gov/apod/"
url = "https://apod.nasa.gov/apod/ap"+d+".html"
html = requests.get(url)

s = BeautifulSoup(html.text, 'lxml')

results=s.find_all("img")
image_links = [result.get("src") for result in results]

for index, link in enumerate(image_links):
    if not os.path.exists("images"):
        os.mkdir("images")
    link=link[:-5]
    print(link)
    a=1
    while a!=0:
        response = requests.get(RootUrl+link+'.jpg')
        if response.status_code == 200:
            print('Web site exists')
            a=0
        else:
            print('Web site does not exist')
            link=link[:-1]
            a=1
            print(link)
            print(RootUrl+link+'.jpg')
            k=RootUrl+link+'.jpg'
    img = requests.get(k)
    with open("images\\"+d+".jpg", "wb") as file:
        file.write(img.content) 
print('NASA APOD of',today.strftime('%Y/%m/%d'),'done.')
print('Press any key to continue...')
input()