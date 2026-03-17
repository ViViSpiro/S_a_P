# Функция, которая возвращает произведение цифр, входящих в inputs
def multiply_numbers(inputs=None):

    # Если inputs не передан
    if inputs is None:
        return None
    
    # Преобразуем в строку
    inputs_str = str(inputs)
    
    # Собираем все цифры
    digits = [int(char) for char in inputs_str if char.isdigit()]
    
    # Если цифр нет
    if not digits:
        return None
    
    # Вычисляем произведение
    result = 1
    for digit in digits:
        result *= digit
    
    return result

# Получаем входные данные
input_str = input().strip()

try:
    if input_str == "":
        print(multiply_numbers())
    else:
        try:
            inputs = eval(input_str)
            print(multiply_numbers(inputs))
        except:
            print(multiply_numbers(input_str))
except:
    print(None)