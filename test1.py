import requests
api_url="http://127.0.0.1:8000/albums/"

data=requests.get(api_url).json()
print(data)