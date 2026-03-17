# Функция для разбивки массива слов на группы по анаграммам
def combine_anagrams(words_array):
    
    # Словарь для хранения групп анаграмм
    anagram_groups = {}
    
    # Проходим по каждому слову
    for word in words_array:
        # Ключ - отсортированные буквы слова в нижнем регистре
        key = "".join(sorted(word.lower()))
        
        # Добавляем слово в соответствующую группу
        if key in anagram_groups:
            anagram_groups[key].append(word)
        else:
            anagram_groups[key] = [word]
    
    # Возвращаем список групп
    return list(anagram_groups.values())

# Получаем входные данные
try:
    words = eval(input())
    result = combine_anagrams(words)
    print(result)
except:
    print([])