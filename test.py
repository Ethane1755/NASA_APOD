import requests
response = requests.get('https://apod.nasa.gov/apod/image/2206/20220624_ALLINEAMENTO_SPECIALEweb.jpg')
if response.status_code == 200:
    print('Web site exists')
else:
    print('Web site does not exist') 