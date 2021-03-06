from bs4 import BeautifulSoup
import requests
import os
from datetime import date
import re

today=date.today()
d=today.strftime('%y%m%d')

RootUrl = "https://apod.nasa.gov/apod/"
url = "https://apod.nasa.gov/apod/ap"+d+".html"
html = requests.get(url)

s = BeautifulSoup(html.text, 'lxml')

if not os.path.exists("text"):
    os.mkdir("text")
txt=s.get_text()
l=txt.split('astronomer')
txt=l[1]
l1=txt.split('Tomorrow')
exp=str(l1[0])
l2=exp.split('.')
exp=('.'.join(l2[1:]))
exp=exp.replace("\n"," ")
line=exp.find('Image')
exp=exp[:line]+'\n'+exp[line:]
line=exp.find('Explanation')
exp=exp[:line]+'\n'+exp[line:]
list1=exp.split('.  ')
exp=('.\n'.join(list1))
exp=re.sub(' +', ' ', exp)
path = "text\\"+d+'.txt'
with open(path, 'w') as f:
    f.write(exp)

results=s.find_all("img")
image_links = [result.get("src") for result in results]

for index, link in enumerate(image_links):
    if not os.path.exists("images"):
        os.mkdir("images")
    l=link
    link=link[:-5]
    a=1
    while a!=0:
        response = requests.get(RootUrl+link+'.jpg')
        if response.status_code == 200:
            a=0
            k=RootUrl+link+'.jpg'
        else:
            link=link[:-1]
            a=1
    m=RootUrl+l
    if k!='':
        img = requests.get(k)
    else:
        img = requests.get(m)
    with open("images\\"+d+".jpg", "wb") as file:
        file.write(img.content) 
print('NASA APOD of',today.strftime('%Y/%m/%d'),'done.')
print('Press any key to continue...')
input()