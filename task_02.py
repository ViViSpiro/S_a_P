# Функция для определения элементов списка, попадающих в диапазон
def coincidence(list=None, range=None):
    
    # Проверка на наличие обоих параметров
    if list is None or range is None:
        return []
    
    result = []
    
    # Проходим по каждому элементу списка
    for item in list:        
        # Проверяем, является ли элемент числом (int или float)
        if not isinstance(item, (int, float)):
            continue
        
        # Проверяем, попадает ли число в диапазон
        if item >= range.start and item < range.stop:
            result.append(item)
    
    return result
