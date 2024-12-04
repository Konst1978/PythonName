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
