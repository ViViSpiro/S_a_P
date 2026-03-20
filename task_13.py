import time
from functools import wraps
from collections import OrderedDict

def cached(max_size=None, seconds=None):
    """ Декоратор для кэширования результатов функции. """
    # Валидация параметров
    if max_size is not None:
        try:
            max_size = int(max_size)
            if max_size <= 0:
                max_size = None
        except (TypeError, ValueError):
            max_size = None
    
    if seconds is not None:
        try:
            seconds = int(seconds)
            if seconds <= 0:
                seconds = None
        except (TypeError, ValueError):
            seconds = None
    
    def decorator(func):
        # Кэш: ключ -> (значение, время_сохранения)
        cache = OrderedDict()
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal cache
            
            # Создаем ключ из аргументов
            # Преобразуем args и kwargs в кортеж для использования как ключ словаря
            key = (args, tuple(sorted(kwargs.items())))
            
            current_time = time.time()
            
            # Очищаем устаревшие записи, если задан seconds
            if seconds is not None:
                # Создаем новый OrderedDict без устаревших записей
                new_cache = OrderedDict()
                for k, (value, timestamp) in cache.items():
                    if current_time - timestamp <= seconds:
                        new_cache[k] = (value, timestamp)
                cache = new_cache
            
            # Проверяем, есть ли результат в кэше
            if key in cache:
                # Возвращаем закэшированный результат
                return cache[key][0]
            
            # Вычисляем результат
            result = func(*args, **kwargs)
            
            # Сохраняем в кэш
            cache[key] = (result, current_time)
            
            # Если размер кэша превышает max_size, удаляем самую старую запись
            if max_size is not None and len(cache) > max_size:
                # OrderedDict сохраняет порядок вставки
                # popitem(last=False) удаляет первый (самый старый) элемент
                cache.popitem(last=False)
            
            return result
        
        return wrapper
    return decorator


# ========== ПРОВЕРКА РАБОТЫ ==========
def example_from_task():
    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ НА ПРИМЕРЕ ИЗ ЗАДАНИЯ")
    print("=" * 60)
    
    @cached(max_size=3, seconds=10)
    def slow_function(x):
        print(f"Вычисляю для {x}...")
        return x ** 2
    
    # Первый вызов — вычисляется
    print("Первый вызов slow_function(2):")
    print(slow_function(2))
    
    # Повторный вызов с теми же аргументами — берётся из кэша 
    print("\nПовторный вызов slow_function(2) (из кэша):")
    print(slow_function(2))
    
    print("\nЖдем 15 секунд...")
    time.sleep(15)
    
    # Через 15 секунд кэш устарел, новое вычисление
    print("slow_function(2) после 15 секунд (устарело):")
    print(slow_function(2))


example_from_task()