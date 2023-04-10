# Create a program that will ask user to search a word. Search this word in Giphy (use their API). Return links to these GIFs as a result

import requests

GIPHY_API_URL = 'http://api.giphy.com/v1/gifs/search'
GIPHY_API_KEY = '0ZOI0serShuGjOEsQ9klNgeXNcBzQYWg'

search_term = input('Enter a search term: ')

params = {
    'api_key': GIPHY_API_KEY,
    'q': search_term
}

response = requests.get(GIPHY_API_URL, params=params)
if response.ok:
    data = response.json()['data']
    gif_urls = [gif['url'] for gif in data]
    print('GIF URLs:')
    for url in gif_urls:
        print(url)
else:
    print(f'Error: {response.status_code} - {response.reason}')
