import requests
import json

# URL вашего веб-сервиса
api_url = "http://83.143.66.61:27370/generate"  # Замените на фактический URL вашего веб-сервиса

example = 'Плита пазогребневая Кнауф влагостойкая 667х500х100 (24 шт/подд)'
# Отправка POST запроса
payload = {'req':example}
print(payload)
response = requests.post(api_url, json=payload)
print(response)

# Преобразование строки в словарь
data = json.loads(response.text)
print(data)
