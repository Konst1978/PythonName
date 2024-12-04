# Задание 1
# Створення індексу ключових слів у файлі
# • Програма має проаналізувати текстовий файл і створити індекс ключових слів. Для
# кожного слова зберігається список номерів рядків, у яких це слово зустрічається.
# • Завдання ускладнюється, якщо враховувати варіації слів (наприклад, "run" і
# "running").


# import re
# from collections import defaultdict         # словарь позволяет создать значения по умолчанию для ключей, которых еще нет в словаре
#                                             # Если такого ключа еще нет, он его создаст, и ошибки не будет
#
# def russian_stem(word):                                         # удаляем окончания
#     if word.endswith('а') or word.endswith('я'):                # для существительных
#         return word[:-1]
#     elif word.endswith('ть') or word.endswith('ет') or word.endswith('ит') or word.endswith('ла') or word.endswith( # для глаголов
#             'ли'):
#         return word[:-2]
#     elif word.endswith('ый') or word.endswith('ий') or word.endswith('ая') or word.endswith('ие'):      # для прилагательных
#         return word[:-2]
#     return word
#
#
# def create_keyword_index(file_name, use_stemming=False):                        # создает индекс всех слов
#                                                     # Если use_stemming прийдет True, то слова обрабатываются с помощью фун. russian_stem
#     try:
#         keyword_index = defaultdict(list)                               # cоздаем индекс ключевых слов
#
#         with open(file_name, 'r', encoding='utf-8') as infile:          # открываем файл
#             for line_num, line in enumerate(infile, start=1):
#                 words = re.findall(r'\b\w+\b', line.lower())            # разбиваем строку на слова
#                 for word in words:
#                     if use_stemming:                                        # приводим слово к корню, если use_stemming=True
#                         word = russian_stem(word)
#                     if line_num not in keyword_index[word]:
#                         keyword_index[word].append(line_num)
#
#         return dict(keyword_index)
#     except FileNotFoundError:
#         print(f"Файл {file_name} не найден.")
#         return {}
#     except Exception as e:
#         print(f"Произошла ошибка: {e}")
#         return {}
#
# file_name = "input.txt"                                                 # имя текстового файла
#
# index = create_keyword_index(file_name)                                 # создание простого индекса
# print("Индекс без учета корней слов:")
# for word, lines in index.items():
#     print(f"{word}: строки {lines}")
#
# index_with_stemming = create_keyword_index(file_name, use_stemming=True)        # создание индекса с учетом корней
# print("\nИндекс с учетом корней слов:")
# for word, lines in index_with_stemming.items():
#     print(f"{word}: строки {lines}")



# Задание 2
# Пошук файлів із певним вмістом
# • Напишіть програму, яка сканує задану директорію (включно з піддиректоріями) і
# знаходить всі файли, які містять задане ключове слово.

# import os                                                           # для обхода всех дирректорий и поддирректорий
#
# def find_files_with_keyword(directory, keyword):
#     for root, dirs, files in os.walk(directory):                            # проходим по всем файлам в дирректории
#         for file in files:
#             file_path = os.path.join(root, file)
#             try:
#                 with open(file_path, 'r', encoding='utf-8') as f:
#                     content = f.read()                                      # читаем содержимое
#                     if keyword.lower() in content.lower():                  # если ключевое слово найдено
#                         print(f"Файл найден: {file_path}")
#             except (UnicodeDecodeError, FileNotFoundError) as e:
#                 continue                                                    # если файл например в хреновой кодировке
#
#
# directory = input("Введите путь к дирректории для поиска: ")
# keyword = input("Введите ключевое слово для поиска: ")
#
# find_files_with_keyword(directory, keyword)


# Задание 3
# Статистика великих файлів
# • Програма має обробити великий текстовий файл і зібрати статистику:
# o Кількість слів.
# o Найчастіше вживані слова.
# o Довжина найдовшого слова.

# import re
# from collections import Counter             # класс для подсчета элементов
#
# def process_large_file(file_path):
#     words = []                                                              # список для всех слов в файле
#
#     try:
#         with open(file_path, 'r', encoding='utf-8') as f:
#             for line in f:                                                  # читаем файл построчно
#                 words_in_line = re.findall(r'\w+', line.lower())  # слова к нижнему регистру. регулярное выражение для разделения строки на слова
#                 words.extend(words_in_line)
#     except FileNotFoundError:
#         print("Файл не найден.")
#         return
#
#     word_count = len(words)                                                 # количество слов
#     word_frequencies = Counter(words)                                       # часто встречающиеся слова. считаем частоту каждого слова
#     most_common_words = word_frequencies.most_common(5)                     # топ-5 самых часто встречающихся слов
#
#     longest_word = max(words, key=len) if words else ''                     # длина самого длинного слова
#
#     print(f"Кол-во слов: {word_count}")
#     print(f"Чаще всего встречающиеся слова: {most_common_words}")
#     print(f"Длина самого длинного слова: {len(longest_word)} ({longest_word})")
#
# file_path = input("Введите путь к большому текстовому файлу: ")
# process_large_file(file_path)


# Задание 4
# Сортування рядків у файлі
# • Програма має прочитати текстовий файл, відсортувати його рядки за алфавітом і
# зберегти результат у новому файлі.


# with open('input.txt', 'r', encoding='utf-8') as infile:            # открываем файл
#     lines = infile.readlines()                                      # читаем все строки
#
#
# lines.sort()                                                        # сортируем
#
#
# with open('output.txt', 'w', encoding='utf-8') as outfile:          # открываем файл для записи
#     outfile.writelines(lines)                                       # записуем уже отсортированные
#
# print("Строки файла отсортированы и записаны в output.txt")



# Задание 5
# . Реалізація системи журналювання
# Напишіть програму, яка:
# • Зберігає повідомлення про події у текстовий файл у форматі: Час | Рівень |
# Повідомлення.
# • Забезпечує автоматичне створення нового файлу, якщо розмір журналу перевищує
# певний ліміт (наприклад, 1 МБ).

# import os
# import time
#
# def write_log(message, log_file='log.txt', size_limit=1 * 1024 * 1024):                 # функция для записи
#     if os.path.exists(log_file) and os.path.getsize(log_file) >= size_limit:            # проверка размера файла
#         timestamp = time.strftime('%Y%m%d_%H%M%S')                  # Если размер файла превышает лимит, переименовываем
#         os.rename(log_file, f"{log_file}_{timestamp}")
#
#     with open(log_file, 'a', encoding='utf-8') as file:                         # открываем файл для добавления сообщения
#         current_time = time.strftime('%Y-%m-%d %H:%M:%S')                       # получаем время
#         log_entry = f"{current_time} | INFO | {message}\n"                      # формируем строку
#         file.write(log_entry)                                                   # записываем сообщение
#
# write_log("Програма стартовала.")
# write_log("Пользователь вошел в систему")
# write_log("Завершено успешно")
# write_log("Пользователь вышел из системы")



# Задание 6
# Обробка великих файлів
# Напишіть програму, яка:
# • Читає великий текстовий файл (наприклад, кілька ГБ) построчно.
# • Фільтрує рядки за певним шаблоном (наприклад, рядки, що містять номер телефону).
# • Записує результат у новий файл

# import re
#
# def filter_lines(input_file, output_file, pattern):                             # фильтрация строк
#     with open(input_file, 'r', encoding='utf-8') as infile:                     # открываем входной файл
#         with open(output_file, 'w', encoding='utf-8') as outfile:               # открываем выходной файл для записи
#             for line in infile:                                             # проходим по каждой строке
#                 if re.search(pattern, line):                    # если строка соответствует шаблону, записываем в файл
#                     outfile.write(line)
#
# phone_pattern = r'\(\d{3}\)\s\d{3}-\d{4}'                       # пример шаблона для поиска номера телефона (формат: (XXX) XXX-XXXX)
#
# filter_lines('input.txt', 'output.txt', phone_pattern)
#
# print("Фильтрация завершена, результаты сохранены в файл output.txt.")


# Задание 7
# Пошук і заміна у великому файлі
# Напишіть програму, яка виконує пошук і заміну певного слова чи фрази у великому файлі,
# зберігаючи зміни у новому файлі

# import re
#
# def search_and_replace(input_file, output_file, search_pattern, replace_text):
#     with open(input_file, 'r', encoding='utf-8') as infile:                     # открываем входной файл
#         with open(output_file, 'w', encoding='utf-8') as outfile:               # открываем выходной файл для записи
#             for line in infile:                                                 # проходим по каждой строке
#                 modified_line = re.sub(search_pattern, replace_text, line)      # заменяем все найденые слова на новые
#                 outfile.write(modified_line)                                    # записываем изменённую строку в новый файл
#
# search_word = input("Введите слово, которое нужно заменить: ")
# replace_word = input("Введите слово, на которое нужно заменить: ")
#
# search_and_replace('input.txt', 'output.txt', search_word, replace_word)
#
# print("Поиск и замена закончена, результаты в файле output.txt.")


# Задание 8
#  Розбиття великого файлу за роздільниками
# Напишіть програму, яка зчитує великий файл і розбиває його на менші файли на основі
# роздільника (наприклад, порожнього рядка або спеціального символу)


# def split_file_by_delimiter(input_file, output_file_prefix, delimiter="\n\n"):
#
#     with open(input_file, 'r', encoding='utf-8') as infile:             # открываем исходный файл для чтения
#         content = infile.read()                                         # читаем файл
#
#     parts = content.split(delimiter)                                    # разбиваем контент на части на основе разделителя. Пустой строки
#
#     for i, part in enumerate(parts):                                        # для каждой части создаём новый файл
#         output_file = f"{output_file_prefix}_{i+1}.txt"                     # формируем имя для нового файла
#         with open(output_file, 'w', encoding='utf-8') as outfile:           # записываем каждую часть в новый файл
#             outfile.write(part.strip())                                     # убираем лишние пробелы в начале и в конце
#
#     print(f"Файл разбитый на {len(parts)} части.")
#
# split_file_by_delimiter('input.txt', 'output_file', delimiter="\n\n")


# Задание 9
# Напишіть програму, яка читає великий файл і створює новий файл, де текст записаний у
# зворотному порядку: рядки змінюються місцями, а кожен рядок читається справа наліво.


# def reverse_text(input_file, output_file):
#     with open(input_file, 'r', encoding='utf-8') as infile:
#         lines = infile.readlines()                                          # читаем строки
#
#     reversed_lines = [line.strip()[::-1] for line in lines][::-1]           # переворачиваем список строк
#
#     with open(output_file, 'w', encoding='utf-8') as outfile:               # записываем результат в новый файл
#         for line in reversed_lines:
#             outfile.write(line + "\n")
#
#     print(f"Результат записан в файл {output_file}")
#
# reverse_text('input.txt', 'output_reversed.txt')


# Задание 10
# Розбиття великого файлу за кількістю рядків
# Напишіть програму, яка зчитує великий файл і розбиває його на менші файли на основі
# кількості рядків. (скільки рядків скільки файлів, у кожному зберігається по одному рядку)


# def split_file_by_lines(input_file, output_file_prefix):
#     with open(input_file, 'r', encoding='utf-8') as infile:
#         lines = infile.readlines()                                              # читаем строки
#
#     for i, line in enumerate(lines, 1):                                         # разбиваем на отдельные файлы, по одному для каждой строки
#         output_file = f"{output_file_prefix}_{i}.txt"                           # формируем имя для нового файла
#
#         with open(output_file, 'w', encoding='utf-8') as outfile:               # записываем строку в новый файл
#             outfile.write(line)
#
#         print(f"Строка {i} записана в файл {output_file}")
#
# split_file_by_lines('input.txt', 'output_file')