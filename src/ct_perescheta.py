import pandas as pd
import re

def get_unit(measure):
    # Регулярное выражение для поиска единицы измерения
    unit_search = re.search(r'(м2|м3|м|кг|шт|т|компл|рулон|км)', measure)
    if unit_search:
        return unit_search.group(1)
    return "другая"


units = {
    'км': ['км'],
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

def extract_units_and_values(line):
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

#data = [
#    {'req':'Бур по бетону SDS-Plus 8x200 mm 100 шт', 'num_class': '100 шт'},
#   {'req':'Бур по бетону SDS-Plus 8x200 mm 100 м', 'num_class': '10 км'},
#    {'req':'Бур по бетону SDS-Plus 8x200 mm 0.1 кг', 'num_class': '1 т'},
#]
#test = pd.DataFrame(data)
#test[['value', 'unit']] = test['req'].apply(lambda x: pd.Series(extract_units_and_values(x)))
#test['value'] = pd.to_numeric(test['value'], errors='coerce')

def coef_perescheta_1(ref_unit, col):
    ct = 1
    if get_unit(ref_unit) == col:
        return ct
    if ref_unit != col:
        if col is not None:
            if col == 'см' and ref_unit == 'м':
                ct = 0.01
            if col == 'м' and get_unit(ref_unit) == 'км':
                ct = 0.001
            if col == 'см' and get_unit(ref_unit) == 'км':
                ct = 0.00001
                
                
            if col == 'г' and get_unit(ref_unit) == 'кг':
                ct = 0.001
                
            if col == 'г' and get_unit(ref_unit) == 'т':
                ct = 0.000001
            if col == 'кг' and get_unit(ref_unit) == 'т':
                ct = 0.001
            if col == 'т' and get_unit(ref_unit) == 'кг':
                ct = 1000
            if col == 'мл':
                ct = 0.001
            return ct
        return None

def coef_perescheta_2(ref_unit, value, col):
    ct = coef_perescheta_1(ref_unit, col)
    if ct != None:
        ct = value*ct
        if ref_unit == col:
            return ct
        if get_unit(ref_unit) == 'см':
            if ref_unit == '10 см':
                ct = ct*0.1
                return(ct)
            if ref_unit == '100 см':
                ct = ct*0.01
                return(ct)
            if ref_unit == '1000 см':
                ct = ct*0.001
                return(ct)
        
        if get_unit(ref_unit) == 'мл':
            if ref_unit == '10 мл':
                ct = ct*0.1
                return(ct)
            if ref_unit == '100 мл':
                ct = ct*0.01
                return(ct)
            if ref_unit == '1000 мл':
                ct = ct*0.001
                return(ct)
            
        if get_unit(ref_unit) == 'шт':
            if ref_unit == '10 шт':
                ct = ct*0.1
                return(ct)
            if ref_unit == '100 шт':
                ct = ct*0.01
                return(ct)
            if ref_unit == '1000 шт':
                ct = ct*0.001
                return(ct)
            
        if get_unit(ref_unit) == 'т':
            if ref_unit == '1 т':
                return(ct)
            if ref_unit == '10 т':
                ct = ct*0.1
                return(ct)
            if ref_unit == '100 т':
                ct = ct*0.01
                return(ct)
            if ref_unit == '1000 т':
                ct = ct*0.001
                return(ct)
            
        if get_unit(ref_unit) == 'км':
            if ref_unit == '10 км':
                ct = ct*0.1
                return(ct)
            if ref_unit == '100 км':
                ct = ct*0.01
                return(ct)
            if ref_unit == '1000 км':
                ct = ct*0.001
                return(ct)


        if get_unit(ref_unit) == 'м': 
            if ref_unit == '10 м':
                ct = ct*0.1
                return(ct)
            if ref_unit == '100 м':
                ct = ct*0.01
                return(ct)
            if ref_unit == '1000 м':
                ct = ct*0.001
                return(ct)


        if get_unit(ref_unit) == 'м2': 
            if ref_unit == '10 м2':
                ct = ct*0.1
                return(ct)
            if ref_unit == '100 м2':
                ct = ct*0.01
                return(ct)
            if ref_unit == '1000 м2':
                ct = ct*0.001
                return(ct)

        if get_unit(ref_unit) == 'м3':
            if ref_unit == '10 м3':
                ct = ct*0.1
                return(ct)
            if ref_unit == '100 м3':
                ct = ct*0.01
                return(ct)
            if ref_unit == '1000 м3':
                ct = ct*0.001
                return(ct)

        if get_unit(ref_unit) == 'компл':
            if ref_unit == '10 компл':
                ct = ct*0.1
                return(ct)
            if ref_unit == '100 компл':
                ct = ct*0.01
                return(ct)
            if ref_unit == '1000 компл':
                ct = ct*0.001
                return(ct)

        if get_unit(ref_unit) == 'рулон':
            if ref_unit == '10 рулонов':
                ct = ct*0.1
                return(ct)
            if ref_unit == '100 рулонов':
                ct = ct*0.01
                return(ct)
            if ref_unit == '1000 рулонов':
                ct = ct*0.001
                return(ct)

#test['ct'] = test.apply(lambda row: coef_perescheta_2(row['num_class'], row['value'], row['unit']), axis=1)