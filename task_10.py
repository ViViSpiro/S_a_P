# Импорт модулей: re для регулярных выражений, Counter для подсчета
import re
from collections import Counter

# Функция, возвращающая словарь со статистикой частоты употребления входящих в неё слов
def count_words(string):
    # Если строка пустая или None - возвращаем пустой словарь
    if string is None or string == "":
        return {}
    
    # Ищем все слова (буквы, апостроф, дефис) в нижнем регистре
    words = re.findall(r"\b[a-zA-Z'-]+\b", string.lower())
    
    # Counter подсчитывает частоту, преобразуем в обычный словарь
    return dict(Counter(words))


# Ввод и вывод с обработкой ошибок
try:
    s = input().strip()  # Читаем строку, убираем пробелы по краям
    
    if s == "":  # Пустой ввод
        print({})
    else:
        try:
            # Пробуем выполнить ввод как код Python (для чисел, списков и т.д.)
            print(count_words(eval(s)))
        except:
            # Если не получилось - используем как обычную строку
            print(count_words(s))
except:
    # Любая ошибка (например, Ctrl+C) - выводим пустой словарь
    print({})