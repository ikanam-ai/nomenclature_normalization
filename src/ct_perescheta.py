import re
import pandas as pd
# Определяем все возможные единицы измерения
units = {
    'км': ['км'],
    'м2': ['м2'],
    'м3': ['м3'],
    'см': ['см'],
    'м': ['м'],
    'шт': ['шт'],
    'компл': ['компл'],
    'маш.-ч': ['маш.-ч'],
    'т': ['т'],
    'кг': ['кг'],
    'мг': ['мг'],
    'л': ['л'],
    'мл': ['мл'],
    'пар': ['пар'],
    'рулон': ['рулон'],
    'секция': ['секция'],
    'панель': ['панель'],
    'кВт-ч': ['кВт-ч']
}

# Создание обратного словаря для быстрого поиска основной единицы по производной
unit_map = {u: main_unit for main_unit, derived_units in units.items() for u in derived_units}

def extract_units_and_values(line):
    # Регулярное выражение для поиска чисел и единиц измерения, включая дробные числа
    pattern = re.compile(r'(\d+(?:[.,]\d+)?(?:\s*\d+(?:[.,]\d+)?)?)\s*([a-zA-Zа-яА-Я0-9-.]+)')
    
    # Найти все совпадения по шаблону и фильтровать по unit_map
    matches = [(value.replace(',', '.'), unit) for value, unit in pattern.findall(line) if unit in unit_map]
    
    return matches


def filter_units(row):
    req_ex = row['req_ex']
    num_class = row['num_class']
    res = [i for i in req_ex if i[1] in num_class]
    if len(res)==1:
      return res[0]
    elif len(res)==0:
      return req_ex[-1]
    elif len(res)>1:
      return res[-1]

def extract_second_number(row):
    value = row
    # Используем регулярное выражение для поиска чисел
    numbers = re.findall(r'\d+(?:[.,]\d+)?', str(value))
    # Если найдено хотя бы два числа, возвращаем второе
    if len(numbers) >= 2:
        return numbers[-1]
    # Если найдено ровно одно число, возвращаем его
    elif len(numbers) == 1:
        return numbers[0]
    else:
        return value


def coef_perescheta_1(ref_unit, col):
    ct = 1
    if ref_unit != col:
        if col is not 'NA':
            if col == 'см' and ref_unit == 'м':
                return 0.01
            if col == 'м' and ref_unit == 'км':
                return 0.001
            if col == 'см' and ref_unit == 'км':
                return 0.00001
                
    
            if col == 'г' and ref_unit == 'кг':
                return 0.001
                
            if col == 'г' and ref_unit == 'т':
                return 0.000001
            if col == 'кг' and ref_unit == 'т':
                return 0.001
            if col == 'т' and ref_unit == 'кг':
                return 1000
            if col == 'мл':
                return 0.001

        return 'NA'
    else:
      return 1

def coef_perescheta_2(ref_unit, value, col):
    if len(extract_units_and_values(ref_unit)) == 0:
        ct = coef_perescheta_1(ref_unit, col)
        if ct != 'NA':
            ref_mult = 1
            ref_unit = ref_unit
            return ct * value
        else:
            return None
    else:
        ct = coef_perescheta_1(extract_units_and_values(ref_unit)[-1][-1], col)
        if ct != 'NA':
            ref_mult = float(extract_units_and_values(ref_unit)[-1][0])
            ref_unit = extract_units_and_values(ref_unit)[-1][-1]
            return ref_mult*ct
        else:
            return None

def calcul_ct(data):
#  data = {'req':'Бур по бетону SDS-Plus 8x200 mm 10 1 шт 100 л', 'num_class': '100 шт'}
    data['req_ex'] = extract_units_and_values(data['req'])
    if len(data['req_ex']) != 0:
        data['filtered_req_ex'] = filter_units(data)
        data['value'], data['unit'] = pd.Series(data['filtered_req_ex'])
        data['value'] = pd.to_numeric(extract_second_number(data['value']), errors='coerce')
        data['ct'] = coef_perescheta_2(data['num_class'], data['value'], data['unit'])
    else:
        data['ct'] = None
    return None if data['ct']==None else float(data['ct'])
