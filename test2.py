import requests

RootUrl = "https://apod.nasa.gov/apod/"
l='image/2206/20220624_ALLINEAMENTO_SPECIALEweb600'
a=1

while a!=0:
    response = requests.get(RootUrl+l+'.jpg')
    if response.status_code == 200:
        print('Web site exists')
        a=0
    else:
        print('Web site does not exist')
        l=l[:-1]
        a=1
        print(l)
        print(RootUrl+l+'.jpg')

