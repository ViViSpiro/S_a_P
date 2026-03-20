class EvenNumbers:
    """
    Итератор, который генерирует указанное количество четных чисел.
    Начинает с 0 и выдает числа: 0, 2, 4, ..., 2*(n-1)
    
    Конструктор принимает только целое число n.
    """
    
    def __init__(self, n):
        """
        Конструктор класса EvenNumbers.
        
        Аргументы:
            n: количество четных чисел для генерации (целое число)
        """
        # Проверяем, является ли n целым числом
        if isinstance(n, int):
            if n >= 0:
                self._n = n
            else:
                self._n = 0
                print("Предупреждение: количество чисел не может быть отрицательным. Будет сгенерировано 0 чисел.")
        else:
            # Если не целое число, выводим предупреждение
            self._n = 0
            print(f"Предупреждение: на вход принимается только целое число. Будет сгенерировано 0 чисел.")
        
        # Текущий индекс (какое по счету число генерируем)
        self._current_index = 0
    
    def __iter__(self):
        """
        Возвращает сам объект как итератор.
        Сбрасывает счетчик для повторного прохода.
        """
        self._current_index = 0
        return self
    
    def __next__(self):
        """
        Возвращает следующее четное число.
        
        Returns:
            int: следующее четное число (0, 2, 4, ...)
        
        Raises:
            StopIteration: когда сгенерировано n чисел
        """
        if self._current_index >= self._n:
            raise StopIteration
        
        result = 2 * self._current_index
        self._current_index += 1
        
        return result


# ========== ДЕМОНСТРАЦИЯ ==========
def demo():
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ КЛАССА EvenNumbers")
    print("=" * 60)
    
    # Пример из задания
    print("\nПример из задания (n=5):")
    evens = EvenNumbers(5)
    print(*evens, sep=', ')
    print()
    
# ========== ИНТЕРАКТИВНЫЙ РЕЖИМ ==========
def interactive_mode():
    print("=" * 60)
    print("ИНТЕРАКТИВНЫЙ РЕЖИМ")
    print("=" * 60)
    print("Принимается только целое число.")
    
    while True:
        print("\nВведите количество четных чисел (или 'exit' для выхода):")
        user_input = input("> ").strip()
        
        if user_input.lower() == 'exit':
            print("Выход из программы.")
            break
        
        try:
            # Пробуем преобразовать ввод в целое число
            n = int(user_input)
                        
            # Создаем итератор
            evens = EvenNumbers(n)
            
            # Генерируем числа
            numbers = list(evens)
            
            print(f"\nСгенерировано {len(numbers)} четных чисел:")            
            print(*numbers, sep=', ')
            
            # Показываем формулу
            if numbers:
                print(f"Формула: 0, 2, 4, ..., {2 * (n - 1) if n > 0 else 'нет чисел'}")
            
        except ValueError:
            # Если введено не число            
            evens = EvenNumbers(user_input)
            numbers = list(evens)
            print(f"\nСгенерировано {len(numbers)} четных чисел:")
            print(*numbers)
        except Exception as e:
            print(f"Ошибка: {e}")


# ========== ЗАПУСК ==========
if __name__ == "__main__":
    print("ВЫБОР РЕЖИМА РАБОТЫ")    
    print("1 - Демонстрация работы")
    print("2 - Интерактивный режим")
    
    choice = input("\nВаш выбор (1/2): ").strip()
    
    if choice == "1":
        demo()
    elif choice == "2":
        interactive_mode()    
    else:
        print("\nНеверный выбор. Выберите один из двух режимов работы.")        