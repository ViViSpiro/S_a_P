# Функция для определения максимального нечетного элемента
def max_odd(array=None):
    # Проверка на пустой массив или None
    if array is None:
        return None
    
    odd_numbers = []
    
    # Проходим по каждому элементу массива
    for item in array:
        # Пропускаем None
        if item is None:
            continue
        
        # Проверяем, является ли элемент числом (int или float)
        if not isinstance(item, (int, float)):
            continue
        
        # Проверяем, является ли число нечетным целым
        if isinstance(item, float):
            # Проверяем, что число целое (с учетом погрешности)
            if item == int(item) and int(item) % 2 != 0:
                odd_numbers.append(int(round(item)))
        else:  # int
            if item % 2 != 0:
                odd_numbers.append(item)
    
    # Если нет нечетных чисел, возвращаем None
    if len(odd_numbers) == 0:
        return None
    
    # Возвращаем максимальное нечетное число
    return max(odd_numbers)