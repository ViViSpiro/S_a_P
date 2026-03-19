class Dessert:
    """Класс, представляющий десерт с названием и калорийностью."""
    
    def __init__(self, name=None, calories=None):
        """Конструктор с необязательными параметрами."""
        self._name = name      # Поле для названия
        self._calories = calories  # Поле для калорий
    
    # Геттер для name
    def get_name(self):
        """Возвращает название десерта."""
        return self._name
    
    # Сеттер для name
    def set_name(self, name):
        """Устанавливает название десерта."""
        self._name = name
    
    # Геттер для calories
    def get_calories(self):
        """Возвращает калорийность десерта."""
        return self._calories
    
    # Сеттер для calories
    def set_calories(self, calories):
        """Устанавливает калорийность десерта."""
        self._calories = calories
    
    # Свойства для удобного доступа (альтернатива геттерам/сеттерам)
    name = property(get_name, set_name)
    calories = property(get_calories, set_calories)
    
    def is_healthy(self):
        """
        Проверяет, полезный ли десерт (калорий < 200).
        При ошибках возвращает False.
        """
        # Если калории не заданы - не полезный
        if self._calories is None:
            return False
        
        try:
            # Пробуем преобразовать в число и сравнить
            return float(self._calories) < 200
        except (TypeError, ValueError):
            # Если не число - не полезный
            return False
    
    def is_delicious(self):
        """Все десерты вкусные! Всегда возвращает True."""
        return True
    
# ========== ЗАПУСК РАБОТЫ С ИНТЕРАКТИВОМ ==========
if __name__ == "__main__":
    print("=" * 60)
    print("СОЗДАНИЕ ДЕСЕРТА")
    print("=" * 60)
    
    # Ввод названия
    name = input("Введите название десерта (и/или нажмите Enter): ").strip()
    if name == "":
        name = None
    
    # Ввод калорий
    calories_input = input("Введите калорийность (и/или нажмите Enter): ").strip()
    if calories_input == "":
        calories = None
    else:
        try:
            # Пробуем преобразовать в число
            calories = float(calories_input)
            # Если это целое число, сохраняем как int
            if calories.is_integer():
                calories = int(calories)
        except ValueError:
            # Если не число, оставляем как строку
            calories = calories_input
    
    # Создаем десерт
    dessert = Dessert(name, calories)
    
    print("\n" + "=" * 60)
    print("ИНФОРМАЦИЯ О ДЕСЕРТЕ")
    print("=" * 60)
    print(f"Название: {dessert.name or 'Не указано'}")
    print(f"Калории: {dessert.calories or 'Не указаны'}")
    print(f"Полезный: {dessert.is_healthy()}")
    print(f"Вкусный: {dessert.is_delicious()}")
    
    # Предложение изменить
    print("\n" + "=" * 60)
    print("ИЗМЕНЕНИЕ ДЕСЕРТА")
    print("=" * 60)
    print("(оставьте поле пустым, если не хотите менять)")

    
    new_name = input("Новое название: ").strip()
    if new_name:
        dessert.name = new_name
    
    new_calories = input("Новые калории: ").strip()
    if new_calories:
        try:
            dessert.calories = float(new_calories)
        except ValueError:
            dessert.calories = new_calories
    
    print("\n" + "=" * 60)
    print("ОБНОВЛЕННАЯ ИНФОРМАЦИЯ")
    print("=" * 60)
    print(f"Название: {dessert.name}")
    print(f"Калории: {dessert.calories}")
    print(f"Полезный: {dessert.is_healthy()}")
    print(f"Вкусный: {dessert.is_delicious()}")
