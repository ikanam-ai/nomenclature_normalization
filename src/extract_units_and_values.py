import pandas as pd

units = {
    'м2': ['м2'],
    'м3': ['м3'],
    'см': ['см'],
    'км': ['км'],
    'шт.': ['шт.'],
    'шт': ['шт'],
    'компл': ['компл'],
    'маш.-ч': ['маш.-ч'],
    'т': ['т'],
    'кг': ['кг'],
    'г': ['г'],
    'мг': ['мг'],
    'л': ['л'],
    'мл': ['мл'],
    'м': ['м'],
    'пар': ['пар'],
    'рулон': ['рулон'],
    'секция': ['секция'],
    'панель': ['панель'],
    'кВт-ч': ['кВт-ч']
}

# Создание обратного словаря для быстрого поиска основной единицы по производной
unit_map = {u: main_unit for main_unit, derived_units in units.items() for u in derived_units}

def units_and_values(line):
    # Регулярное выражение для поиска чисел и единиц измерения, включая дробные числа
    pattern = re.compile(r'(\d+(?:[.,]\d+)?(?:\s*\d+(?:[.,]\d+)?)?)\s*([a-zA-Zа-яА-Я0-9-]+)')
    
    # Найти все совпадения по шаблону
    matches = reversed(pattern.findall(line))
    
    for value, unit in matches:
        # Проверяем, есть ли найденная единица измерения в списке разрешенных
        if unit in unit_map:
            # Замена запятой на точку для корректного отображения чисел
            value = value.replace(',', '.')
            return value, unit
    
    return None, None

#df[['value', 'unit']] = df['record_name'].apply(lambda x: pd.Series(extract_units_and_values(x)))

def extract_second_number(value):
    # Используем регулярное выражение для поиска чисел
    numbers = re.findall(r'\d+', str(value))
    # Если найдено хотя бы два числа, возвращаем второе
    if len(numbers) >= 2:
        return int(numbers[1])
    # Если найдено ровно одно число, возвращаем его
    elif len(numbers) == 1:
        return int(numbers[0])
    else:
        return value

#df['value'] = df['value'].apply(extract_second_number)