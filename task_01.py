# Импортируем стандартную библиотеку для работы с регулярными выражениями
import re

# Функция для определения, является ли строка палиндромом
def is_palindrome(string):
    
    # Преобразуем в строку и удаляем все ненужные символы
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', str(string)).lower()

    # Проверка на пустую строку (после очистки)
    if len(cleaned) == 0:
        return False
    
    # Проверка на палиндром
    return cleaned == cleaned[::-1]

print(is_palindrome(input()))