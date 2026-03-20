class BlockTranspositionCipher:
    """
    Класс для шифрования и дешифрования текста методом блочной перестановки.
    """
    
    def __init__(self, text, key, decrypt=False):
        """
        Инициализация шифратора/дешифратора.
        
        Аргументы:
            text: исходный текст для шифрования или зашифрованный текст для дешифрования
            key: ключ для перестановки (строка из уникальных английских букв)
            decrypt: если True - режим дешифрования, False - режим шифрования
        """
        self._text = text
        self._key = key
        self._decrypt = decrypt
        
        # Валидация ключа
        self._validate_key()
        
        # Преобразуем ключ в числовой массив
        self._key_indices = self._key_to_indices()
        
        # Длина ключа (размер блока)
        self._block_size = len(key)
        
        # Разбиваем текст на блоки
        self._blocks = self._split_into_blocks()
        
        # Создаем порядок перестановки для полного блока
        self._full_order = self._get_permutation_order()
    
    def _validate_key(self):
        """
        Проверяет ключ на соответствие требованиям:
        - состоит только из букв английского алфавита
        - все буквы уникальны (без учета регистра)
        
        Raises:
            ValueError: если ключ не соответствует требованиям
        """
        if not self._key:
            raise ValueError("Ключ не может быть пустым")
        
        # Проверяем, что все символы - буквы английского алфавита
        if not all(c.isalpha() and c.isascii() for c in self._key):
            raise ValueError("Ключ должен состоять только из букв английского алфавита")
        
        # Проверяем уникальность букв (без учета регистра)
        key_lower = self._key.lower()
        if len(key_lower) != len(set(key_lower)):
            raise ValueError("Все буквы в ключе должны быть уникальны")
    
    def _key_to_indices(self):
        """
        Преобразует ключ в числовой массив.
        Каждому символу присваивается его порядковый номер в алфавите (a=0, b=1, ..., z=25).
        
        Returns:
            list: список чисел, соответствующих порядку символов в ключе
        """
        indices = []
        for char in self._key.lower():
            # ord('a') = 97, вычитаем чтобы получить 0-25
            indices.append(ord(char) - ord('a'))
        return indices
    
    def _split_into_blocks(self):
        """
        Разбивает текст на блоки заданного размера.
        Для шифрования: дополняет последний блок пробелами при необходимости.
        Для дешифрования: разбивает на блоки полного размера, 
        последний блок может быть короче.
        
        Returns:
            list: список блоков
        """
        blocks = []
        
        if self._decrypt:
            # Для дешифрования разбиваем на блоки полного размера,
            # последний блок может быть короче
            for i in range(0, len(self._text), self._block_size):
                block = self._text[i:i + self._block_size]
                blocks.append(block)
        else:
            # Для шифрования дополняем последний блок пробелами
            for i in range(0, len(self._text), self._block_size):
                block = self._text[i:i + self._block_size]
                # Если блок короче, чем размер блока, дополняем пробелами
                if len(block) < self._block_size:
                    block = block.ljust(self._block_size)
                blocks.append(block)
        
        return blocks
    
    def _get_permutation_order(self):
        """
        Определяет порядок перестановки символов в блоке.
        Для шифрования: сортирует символы ключа по алфавиту.
        Для дешифрования: определяет обратный порядок.
        
        Returns:
            list: список индексов для перестановки
        """
        # Создаем список пар (индекс_в_ключе, числовое_значение_буквы)
        key_pairs = list(enumerate(self._key_indices))
        
        # Сортируем по числовому значению буквы
        sorted_pairs = sorted(key_pairs, key=lambda x: x[1])
        
        if self._decrypt:
            # Для дешифрования нужно восстановить исходный порядок
            # Создаем массив для обратной перестановки
            reverse_order = [0] * self._block_size
            for new_pos, (old_pos, _) in enumerate(sorted_pairs):
                reverse_order[old_pos] = new_pos
            return reverse_order
        else:
            # Для шифрования возвращаем позиции в порядке сортировки
            return [old_pos for old_pos, _ in sorted_pairs]
    
    def _transform_block(self, block):
        """
        Применяет перестановку к одному блоку.
        
        Аргументы:
            block: строка-блок для преобразования
            
        Returns:
            str: преобразованный блок
        """
        current_size = len(block)
        order = self._full_order
        
        # Если блок короче полного размера, используем только
        # те позиции, которые есть в блоке
        if current_size < self._block_size:
            # Создаем урезанный порядок, сохраняя только существующие индексы
            filtered_order = [pos for pos in order if pos < current_size]
            result = [''] * current_size
            for new_pos, old_pos in enumerate(filtered_order):
                result[new_pos] = block[old_pos]
            return ''.join(result)
        else:
            # Для полного блока используем полный порядок
            result = [''] * self._block_size
            for new_pos, old_pos in enumerate(order):
                result[new_pos] = block[old_pos]
            return ''.join(result)
    
    def __iter__(self):
        """
        Возвращает итератор по блокам.
        """
        self._current_block = 0
        return self
    
    def __next__(self):
        """
        Возвращает следующий блок.
        
        Returns:
            str: следующий блок (зашифрованный или расшифрованный)
        
        Raises:
            StopIteration: когда блоки закончились
        """
        if self._current_block >= len(self._blocks):
            raise StopIteration
        
        block = self._blocks[self._current_block]
        self._current_block += 1
        
        return self._transform_block(block)


# ========== ДЕМОНСТРАЦИЯ ==========
def demo():
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ КЛАССА BlockTranspositionCipher")
    print("=" * 60)
    
    # Пример 1: Шифрование с явной итерацией по блокам
    print("\nПример 1: Шифрование с явной итерацией по блокам")
    text = "HELLOWORLD"
    key = "bAc"
    
    print(f"Текст: '{text}'")
    print(f"Ключ: '{key}'")
    
    cipher = BlockTranspositionCipher(text, key, decrypt=False)
    print("Процесс шифрования по блокам:")
    for i, encrypted_block in enumerate(cipher, 1):
        print(f"Блок {i}: '{encrypted_block}'")
    
    # Пример 2: Полное шифрование
    print("\nПример 2: Полное шифрование")
    cipher = BlockTranspositionCipher(text, key, decrypt=False)
    encrypted = ''.join(cipher)
    print(f"Полный зашифрованный текст: '{encrypted}'")
    
    # Пример 3: Дешифрование с итерацией
    print("\nПример 3: Дешифрование с итерацией")
    decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
    print("Процесс дешифрования по блокам:")
    for i, decrypted_block in enumerate(decipher, 1):
        print(f"Блок {i}: '{decrypted_block}'")
    
    # Пример 4: Полное дешифрование с обрезкой пробелов
    print("\nПример 4: Полное дешифрование с обрезкой пробелов")
    decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
    decrypted = ''.join(decipher).rstrip()
    print(f"Полный расшифрованный текст: '{decrypted}'")
    
    # Дополнительная информация
    print("\n" + "=" * 60)
    print("ИНФОРМАЦИЯ О КЛЮЧЕ")
    print("=" * 60)
    key_obj = BlockTranspositionCipher("", key, decrypt=False)
    print(f"Ключ: '{key}'")
    print(f"Длина ключа: {len(key)}")
    print(f"Числовые значения букв: {key_obj._key_indices}")
    print(f"Порядок перестановки: {key_obj._get_permutation_order()}")


# ========== ИНТЕРАКТИВНЫЙ РЕЖИМ ==========
def interactive_mode():
    print("=" * 60)
    print("ИНТЕРАКТИВНЫЙ РЕЖИМ - БЛОЧНАЯ ПЕРЕСТАНОВКА")
    print("=" * 60)
    
    while True:
        print("\nВыберите действие:")
        print("1 - Зашифровать текст")
        print("2 - Расшифровать текст")
        print("3 - Выход")
        
        choice = input("\nВаш выбор (1/2/3): ").strip()
        
        if choice == "3":
            print("Выход из программы.")
            break
        
        if choice not in ["1", "2"]:
            print("Неверный выбор. Попробуйте снова.")
            continue
        
        text = input("\nВведите текст: ").strip()
        key = input("Введите ключ (уникальные английские буквы): ").strip()
        
        try:
            if choice == "1":
                cipher = BlockTranspositionCipher(text, key, decrypt=False)
                encrypted = ''.join(cipher)
                print(f"\nЗашифрованный текст: '{encrypted}'")
                
                # Показываем блоки
                print("\nБлоки:")
                cipher = BlockTranspositionCipher(text, key, decrypt=False)
                for i, block in enumerate(cipher, 1):
                    print(f"  Блок {i}: '{block}'")
            
            else:  # choice == "2"
                decipher = BlockTranspositionCipher(text, key, decrypt=True)
                decrypted = ''.join(decipher).rstrip()
                print(f"\nРасшифрованный текст: '{decrypted}'")
                
                # Показываем блоки
                print("\nБлоки:")
                decipher = BlockTranspositionCipher(text, key, decrypt=True)
                for i, block in enumerate(decipher, 1):
                    print(f"  Блок {i}: '{block}'")
        
        except ValueError as e:
            print(f"\nОшибка: {e}")


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