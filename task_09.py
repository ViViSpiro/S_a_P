# Функция для объединения двух словарей
def connect_dicts(dict1, dict2):
    
    # Вычисляем суммы значений
    sum1 = sum(dict1.values())
    sum2 = sum(dict2.values())
    
    # Определяем приоритетный словарь
    if sum1 > sum2:
        primary, secondary = dict1, dict2
    else:
        primary, secondary = dict2, dict1  # при равных суммах приоритет у dict2
    
    # Формируем результат
    result = {}
    
    # Сначала добавляем из приоритетного
    for key, value in primary.items():
        if value >= 10:
            result[key] = value
    
    # Затем из второго, если ключ еще не занят
    for key, value in secondary.items():
        if value >= 10 and key not in result:
            result[key] = value
    
    # Сортируем по значениям
    return dict(sorted(result.items(), key=lambda item: item[1]))


# Получаем входные данные
try:
    dict1 = eval(input())
    dict2 = eval(input())
    print(connect_dicts(dict1, dict2))
except:
    print({})