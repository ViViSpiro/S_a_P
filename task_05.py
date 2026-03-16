# Импортируем модули для работы с датой и временем и работы с временными интервалами из стандартной библиотеки
from datetime import datetime, timedelta
# Функция, возвращающая дату через заданное количество дней
def date_in_future(integer):
    # Если integer не целое число, возвращаем текущую дату
    if not isinstance(integer, int):
        return datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    
    # Иначе возвращаем дату через integer дней
    return (datetime.now() + timedelta(days=integer)).strftime('%d-%m-%Y %H:%M:%S')

# Получаем входные данные и выводим результат
try:
    print(date_in_future(eval(input())))
except:
    print(date_in_future(None))