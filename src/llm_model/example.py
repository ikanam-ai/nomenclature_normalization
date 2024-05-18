import requests

# URL вашего веб-сервиса
api_url = "http://83.143.66.61:27368/generate"  # Замените на фактический URL вашего веб-сервиса

# Пример текста промпта
prompt_text = "Привет, придумай 10 филосовских проблем для обсуждения фрейдомарксизма"

# Параметры запроса
payload = {
    "prompt": prompt_text
}

# Отправка POST запроса
response = requests.post(api_url, json=payload)

# Печать ответа
print(response.text)
