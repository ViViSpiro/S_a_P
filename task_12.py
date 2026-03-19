class Dessert:
    """Базовый класс, представляющий десерт с названием и калорийностью."""
    
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


class JellyBean(Dessert):
    """
    Класс, представляющий конкретный вид десерта - конфету JellyBean.
    Расширяет класс Dessert атрибутом flavor (вкус).
    """
    
    def __init__(self, name=None, calories=None, flavor=None):
        """ Конструктор класса JellyBean. """
        # Вызываем конструктор родительского класса
        super().__init__(name, calories)
        # Добавляем новый атрибут
        self._flavor = flavor
    
    # Геттер для flavor
    def get_flavor(self):
        """Возвращает вкус конфеты."""
        return self._flavor
    
    # Сеттер для flavor
    def set_flavor(self, flavor):
        """Устанавливает вкус конфеты."""
        self._flavor = flavor
    
    # Свойство для flavor
    flavor = property(get_flavor, set_flavor)
    
    def is_delicious(self):
        """
        Переопределенный метод проверки вкусности.
        Возвращает False только для вкуса "black licorice".
        """
        # Если вкус не задан или это не "black licorice" - десерт вкусный
        if self._flavor is None:
            return True
        
        # Проверяем, является ли вкус "black licorice" (без учета регистра)
        if str(self._flavor).lower() == "black licorice":
            return False
        
        # В остальных случаях - вкусный
        return True
    

# ========== ЗАПУСК РАБОТЫ С ИНТЕРАКТИВОМ ==========
if __name__ == "__main__":
    print("=" * 60)
    print("СОЗДАНИЕ ДЕСЕРТА JELLYBEAN")
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
    
    # Ввод вкуса
    flavor = input("Введите вкус (и/или нажмите Enter): ").strip()
    if flavor == "":
        flavor = None
    
    # Создаем десерт JellyBean
    jelly = JellyBean(name, calories, flavor)
    
    print("\n" + "=" * 60)
    print("ИНФОРМАЦИЯ О JELLYBEAN")
    print("=" * 60)
    print(f"Название: {jelly.name or 'Не указано'}")
    print(f"Калории: {jelly.calories or 'Не указаны'}")
    print(f"Вкус: {jelly.flavor or 'Не указан'}")
    print(f"Полезный: {jelly.is_healthy()}")
    print(f"Вкусный: {jelly.is_delicious()}")
    
    # Предложение изменить
    print("\n" + "=" * 60)
    print("ИЗМЕНЕНИЕ ДЕСЕРТА JELLYBEAN")
    print("=" * 60)
    print("(оставьте поле пустым, если не хотите менять)")
    
    new_name = input("Новое название: ").strip()
    if new_name:
        jelly.name = new_name
    
    new_calories = input("Новые калории: ").strip()
    if new_calories:
        try:
            jelly.calories = float(new_calories)
        except ValueError:
            jelly.calories = new_calories
    
    new_flavor = input("Новый вкус: ").strip()
    if new_flavor:
        jelly.flavor = new_flavor
    
    print("\n" + "=" * 60)
    print("ОБНОВЛЕННАЯ ИНФОРМАЦИЯ")
    print("=" * 60)
    print(f"Название: {jelly.name}")
    print(f"Калории: {jelly.calories}")
    print(f"Вкус: {jelly.flavor}")
    print(f"Полезный: {jelly.is_healthy()}")
    print(f"Вкусный: {jelly.is_delicious()}")
    