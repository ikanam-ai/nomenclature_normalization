import requests
import json
from similar import similar_df_in_df, similar_df_in_ksr
import pandas as pd

# URL вашего веб-сервиса
api_url = "http://83.143.66.61:27370/generate"  # Замените на фактический URL вашего веб-сервиса



example = 'Плита пазогребневая Кнауф влагостойкая 667х500х100 (24 шт/подд)'
print('input')
print(example)
print()
df_path = 'data/new_train.csv'
df = pd.read_csv(df_path).reset_index(drop=True)

ksr_path = 'data/ksr_clean.csv'
ksr = pd.read_csv(ksr_path).reset_index(drop=True)

res = similar_df_in_df(df, example)[['record_name', 'ref_name']]
#record_name,ref_code,ref_name,ref_unit
record_names = res['record_name'].tolist()
ref_names = res['ref_name'].tolist()
print('sim')
print(record_names)
print()

# Создаем один массив, чередуя значения
result_array = list(sum(zip(record_names, ref_names), ()))

payload = {
    "text_list": result_array + [example]
}
# Отправка POST запроса
response = requests.post(api_url, json=payload)

# Преобразование строки в словарь
data = json.loads(response.text)
print('model_gen')
print(data['predict'].split('\n')[-1])
print()

# Декодирование содержимого
decoded_predict = data['predict'].split('\n')[-1]

result = similar_df_in_ksr(ksr, decoded_predict)
# Печать ответа
print('result')
print(result.tolist())
print()
