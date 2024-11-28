import requests
import pprint

params = {
    'q' : 'html'
}

response = requests.get('https://api.github.com/search/repositories', params=params)

print(response.status_code)

response_json = response.json()

print(f'Количество репозиториев с использованием js: {response_json["total_count"]}')