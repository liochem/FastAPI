import requests
url = 'http://127.0.0.1:8000'
response = requests.get(f'{url}/hello')
print(response.content)

n = {'number': 3}
response2 = requests.get(f'{url}/multiply', params=n)
print(response2.content)

