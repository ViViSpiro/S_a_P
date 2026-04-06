# Функция для того, чтобы поменять местами минимальные и максимальные элементы и добавить минимум в конец массива
def sort_list(lst):
    # Проверка на пустой список
    if lst is None or len(lst) == 0:
        return []
    
    # Находим минимальное и максимальное значение
    min_val = min(lst)
    max_val = max(lst)
    
    # Если минимальное равно максимальному (все элементы одинаковые)
    if min_val == max_val:
        return lst + [min_val]
    
    # Создаем новый список для результата
    result = []
    
    # Проходим по каждому элементу исходного списка
    for item in lst:
        if item == min_val:
            result.append(max_val)
        elif item == max_val:
            result.append(min_val)
        else:
            result.append(item)
    
    # Добавляем минимальное значение в конец
    result.append(min_val)
    
    return result