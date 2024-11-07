import requests

api_key = 'c847ab1c-f9e6-4793-8322-e57581abecc1'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

print(definitions)
