# Задание 1
# Обчислення площі еліпса
# Функція повинна обчислювати площу еліпса за великими і малими напівосями.

# import math
#
# def calculate_ellipse_area(a, b):
#     if a <= 0 or b <= 0:
#         raise ValueError("Длины полуосей должны быть положительными числами.")
#
#     return math.pi * a * b
#
# try:
#     a = float(input("Введите длину большой полуоси (a): "))
#     b = float(input("Введите длину малой полуоси (b): "))
#
#     area = calculate_ellipse_area(a, b)
#     print(f"Площадь эллипса с полуосями a = {a} и b = {b} равна {area:.2f}")
# except ValueError as e:
#     print(f"Ошибка: {e}")


# Задание 2
# Гармонічний ряд
# Напишіть функцію, яка обчислює суму перших n членів гармонічного ряду

# def harmonic_sum(n):            # n указывает сколько членов ряда нужно суммировать.
#     if n <= 0:
#         raise ValueError("n должно быть положительным целым числом.")
#
#     result = 0
#     for i in range(1, n + 1):
#         result += 1 / i
#     return result
#
# try:
#     n = int(input("Введите количество членов ряда (n): "))
#     sum_harmonic = harmonic_sum(n)
#     print(f"Сумма первых {n} членов гармонического ряда: {sum_harmonic:.5f}")
# except ValueError as e:
#     print(f"Ошибка: {e}")


# Задание 3
# Кут між двома векторами
# Функція, яка обчислює кут між двома векторами в просторі, використовуючи їх
# скалярний добуток і довжини.


# import math
#
# def vector_angle(u, v):
#     dot_product = u[0] * v[0] + u[1] * v[1] + u[2] * v[2]                   # скалярное произведение
#
#     magnitude_u = math.sqrt(u[0] ** 2 + u[1] ** 2 + u[2] ** 2)              # длины векторов
#     magnitude_v = math.sqrt(v[0] ** 2 + v[1] ** 2 + v[2] ** 2)
#
#     if magnitude_u == 0 or magnitude_v == 0:
#         raise ValueError("Длина вектора не может быть равна нулю.")
#
#     cos_theta = dot_product / (magnitude_u * magnitude_v)                   # косинус угла
#
#     cos_theta = max(-1, min(1, cos_theta))                                  # избегаем ошибок округления, ограничивая значение cos_theta
#
#     theta_rad = math.acos(cos_theta)                                        # угол в радианах
#
#     theta_deg = math.degrees(theta_rad)                                     # перевод в градусы
#
#     return theta_deg
#
# try:
#     u = tuple(map(float, input("Введите через пробел координаты первого вектора (u_x, u_y, u_z): ").split()))
#     v = tuple(map(float, input("Введите через пробел координаты второго вектора (v_x, v_y, v_z): ").split()))
#
#     angle = vector_angle(u, v)
#     print(f"Угол между векторами: {angle:.2f} градусов")
# except ValueError as e:
#     print(f"Ошибка: {e}")

# Задание 4        для выполнения сначала надо установить matplotlib. В терминале ввести "pip install matplotlib"
# Моделювання кидка м'яча
# Створіть функцію, яка моделює траєкторію кидка м'яча, використовуючи формули
# кінематики з урахуванням кута кидка.

# import math
# import matplotlib.pyplot as plt                 # для построения графика траектории.
#
# def simulate_trajectory(v0, angle_deg):
#     g = 9.8                                                                 # ускорение свободного падения (м/с^2)
#
#     angle_rad = math.radians(angle_deg)                                     # перевод угла в радианы
#
#     T = (2 * v0 * math.sin(angle_rad)) / g                                  # время полета
#
#     t_points = [t / 100 for t in range(int(T * 100) + 1)]                   # расчёт точек траектории. временные шаги
#     x_points = [v0 * t * math.cos(angle_rad) for t in t_points]
#     y_points = [v0 * t * math.sin(angle_rad) - 0.5 * g * t ** 2 for t in t_points]
#
#     x_points = [x for x, y in zip(x_points, y_points) if y >= 0]            # удаляем отрицательные точки (если мяч упал на землю)
#     y_points = [y for y in y_points if y >= 0]
#
#     plt.figure(figsize=(10, 6))                                             # график
#     plt.plot(x_points, y_points, label="Траектория мяча")
#     plt.title("Моделирование траектории кидка мяча")
#     plt.xlabel("Расстояние (м)")
#     plt.ylabel("Высота (м)")
#     plt.legend()
#     plt.grid(True)
#     plt.show()
#
# try:
#     v0 = float(input("Введите начальную скорость (м/с): "))
#     angle_deg = float(input("Введите угол броска (в градусах): "))
#
#     if v0 <= 0 or not (0 <= angle_deg <= 90):
#         raise ValueError("Скорость должна быть положительной, а угол в пределах [0, 90] градусов.")
#
#     simulate_trajectory(v0, angle_deg)
# except ValueError as e:
#     print(f"Ошибка: {e}")

# Задание 5
# Число Пі методом Монте-Карло
# Реалізуйте алгоритм для наближеного обчислення числа π\pi методом Монте-Карло.

# import random
#
# def monte_carlo_pi(num_points):
#     inside_circle = 0
#
#     for _ in range(num_points):
#
#         x = random.uniform(0, 1)                                  # генерация случайных координат x и y в диапазоне [0, 1]
#         y = random.uniform(0, 1)
#
#         if x ** 2 + y ** 2 <= 1:                                        # проверяем, находится ли точка внутри круга радиуса 1
#             inside_circle += 1
#
#     pi_approx = 4 * inside_circle / num_points                          # отношение точек внутри круга к общему числу точек
#     return pi_approx
#
# try:
#     num_points = int(input("Введите количество точек для метода Монте-Карло: "))
#     if num_points <= 0:
#         raise ValueError("Количество точек должно быть положительным числом.")
#
#     pi_value = monte_carlo_pi(num_points)
#     print(f"Приближённое значение числа π для {num_points} точек: {pi_value}")
# except ValueError as e:
#     print(f"Ошибка: {e}")

# Задание 1   ч 2
# Обчислення часу в дорозі Реалізуйте функцію, яка приймає дату і час початку поїздки та її тривалість (у
# годинах), і обчислює дату й час прибуття.

# from datetime import datetime, timedelta
#
# def calculate_arrival_time(start_date_time, duration_hours):
#     try:
#         start = datetime.strptime(start_date_time, "%Y-%m-%d %H:%M")        # преобразуем строку в объект datetime
#
#         duration = timedelta(hours=duration_hours)                          # создаем объект timedelta на основе длительности поездки
#
#         arrival = start + duration                                          # вычисляем время прибытия
#
#         return arrival.strftime("%Y-%m-%d %H:%M")                           # возвращаем дату и время в строковом формате
#     except ValueError:
#         return "Ошибка: Неверный формат даты и времени. Используйте формат 'YYYY-MM-DD HH:MM'."
#
# try:
#     start_date_time = input("Введите дату и время отправления (в формате 'YYYY-MM-DD HH:MM') (Например: 2024-12-09 14:30): ")
#     duration_hours = float(input("Введите длительность поездки (в часах): "))
#
#     arrival_time = calculate_arrival_time(start_date_time, duration_hours)
#     print(f"Время прибытия: {arrival_time}")
# except ValueError:
#     print("Ошибка: Пожалуйста, введите корректное числовое значение для длительности.")


# Задание 2   ч 2
# Генерація календаря для місяця. Напишіть функцію, яка створює текстовий календар для заданого місяця і року.

# import calendar
#
# def generate_calendar(year, month):
#     try:
#         cal = calendar.month(year, month)                           # получаем текстовый календарь для заданного месяца и года
#
#         return cal
#     except ValueError:
#         return "Ошибка: Неверный месяц или год. Убедитесь, что год положительный, а месяц от 1 до 12."
#
# try:
#     year = int(input("Введите год (например, 2024): "))
#     month = int(input("Введите месяц (от 1 до 12): "))
#
#     calendar_text = generate_calendar(year, month)
#     print(calendar_text)
# except ValueError:
#     print("Ошибка: Пожалуйста, введите корректные числовые значения для года и месяца.")



# Задание 3   ч 2
# Старіння документів. Функція, яка перевіряє, чи пройшло більше 10 років з дати створення документа.

# from datetime import datetime
#
# def is_document_old(creation_date):
#     try:
#         creation_date_obj = datetime.strptime(creation_date, "%Y-%m-%d")    # преобразуем строку с датой создания в объект datetime
#
#         current_date = datetime.now()                                               # получаем текущую дату
#
#         delta = current_date - creation_date_obj                                    # вычисляем разницу между текущей датой и датой создания
#
#         if delta.days > 3650:                                                       # прошло ли более 10 лет (3650 дней = 10 лет)
#             return True
#         else:
#             return False
#     except ValueError:
#         return "Ошибка: Неверный формат даты. Используйте формат 'YYYY-MM-DD'."
#
# try:
#     creation_date = input("Введите дату создания документа (в формате 'YYYY-MM-DD'): ")
#
#     if is_document_old(creation_date) == True:
#         print("Документ старше 10 лет.")
#     elif is_document_old(creation_date) == False:
#         print("Документ не старше 10 лет.")
#     else:
#         print(is_document_old(creation_date))
# except ValueError:
#     print("Ошибка: Пожалуйста, введите корректную дату.")


# Задание 4   ч 2
# Вік у днях, місяцях і роках. Реалізуйте функцію, яка приймає дату народження і обчислює вік у днях, місяцях та роках.

# from datetime import datetime
#
# def calculate_age(birth_date):
#     try:
#         birth_date_obj = datetime.strptime(birth_date, "%Y-%m-%d")  # преобразуем строку в объект datetime
#
#         current_date = datetime.now()                                       # получаем текущую дату
#
#
#         years = current_date.year - birth_date_obj.year                     # рассчитываем разницу в годах
#
#         # если день рождения еще не наступил в этом году, уменьшаем возраст на 1 год
#         if current_date.month < birth_date_obj.month or (
#                 current_date.month == birth_date_obj.month and current_date.day < birth_date_obj.day):
#             years -= 1
#
#         if current_date.month >= birth_date_obj.month:                      # рассчитываем разницу в месяцах
#             months = current_date.month - birth_date_obj.month
#         else:
#             months = 12 + current_date.month - birth_date_obj.month
#
#         # если день рождения уже был в этом году, надо уменьшить количество месяцев на 1
#         if current_date.day < birth_date_obj.day:
#             months -= 1
#
#         if current_date.day >= birth_date_obj.day:                          # рассчитываем разницу в днях
#             days = current_date.day - birth_date_obj.day
#         else:
#             # если день рождения еще не наступил в текущем месяце, берем дни из предыдущего месяца
#             prev_month = current_date.replace(
#                 month=current_date.month - 1) if current_date.month > 1 else current_date.replace(month=12,
#                                                                                                   year=current_date.year - 1)
#             days = (current_date - prev_month.replace(day=prev_month.day)).days
#
#         return years, months, days
#     except ValueError:
#         return "Ошибка: Неверный формат даты. Используйте формат 'YYYY-MM-DD'."
#
# try:
#     birth_date = input("Введите вашу дату рождения (в формате 'YYYY-MM-DD'): ")
#
#     years, months, days = calculate_age(birth_date)
#     if isinstance(years, int):                                                      # если все успешно
#         print(f"Ваш возраст: {years} лет, {months} месяцев и {days} дней.")
#     else:
#         print(years)
# except ValueError:
#     print("Ошибка: Пожалуйста, введите корректную дату.")


# Задание 5   ч 2
# Розподіл дат. Функція, яка генерує список усіх понеділків між двома заданими датами.

# from datetime import datetime, timedelta
#
# def get_mondays(start_date, end_date):
#     try:
#         start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")      # преобразуем строки в объекты datetime
#         end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
#
#         if start_date_obj > end_date_obj:                                   # проверяем, что начальная дата раньше конечной
#             return "Ошибка: Начальная дата должна быть раньше конечной."
#
#         mondays = []
#
#         days_to_monday = (7 - start_date_obj.weekday()) % 7                 # переводим start_date в ближайший понедельник
#         current_monday = start_date_obj + timedelta(days=days_to_monday)
#
#         while current_monday <= end_date_obj:                               # генерируем понедельники до конечной даты
#             mondays.append(current_monday.strftime("%Y-%m-%d"))
#             current_monday += timedelta(weeks=1)
#
#         return mondays
#     except ValueError:
#         return "Ошибка: Неверный формат даты. Используйте формат 'YYYY-MM-DD'."
#
# try:
#     start_date = input("Введите начальную дату (в формате 'YYYY-MM-DD'): ")
#     end_date = input("Введите конечную дату (в формате 'YYYY-MM-DD'): ")
#
#     mondays = get_mondays(start_date, end_date)
#
#     if isinstance(mondays, list):                                       # если список успешно сгенерирован
#         print("Понедельники между датами:")
#         for monday in mondays:
#             print(monday)
#     else:
#         print(mondays)
# except ValueError:
#     print("Ошибка: Пожалуйста, введите корректные даты.")


# Задание 6   ч 2
# Збіг днів народження. Реалізуйте функцію, яка перевіряє, чи припадає дата народження користувача на
# вихідний (субота/неділя) протягом заданого року.

# from datetime import datetime
#
# def is_birthday_on_weekend(birth_date, year):
#     try:
#         birth_date_obj = datetime.strptime(birth_date, "%Y-%m-%d")      # преобразуем строку в объект datetime
#
#         birth_date_this_year = birth_date_obj.replace(year=year)                # заменяем год на заданный для проверки
#
#         if birth_date_this_year.weekday() in [5, 6]:            # если день недели - суббота (5) или воскресенье (6)
#             return True
#         else:
#             return False
#     except ValueError:
#         return "Ошибка: Неверный формат даты. Используйте формат 'YYYY-MM-DD'."
#
# try:
#     birth_date = input("Введите вашу дату рождения (в формате 'YYYY-MM-DD'): ")
#     year = int(input("Введите год для проверки: "))
#
#     result = is_birthday_on_weekend(birth_date, year)
#
#     if isinstance(result, bool):            # если результат булевое значение
#         if result:
#             print(f"Ваше день рождения в {year} году выпадает на выходной (субботу или воскресенье).")
#         else:
#             print(f"Ваше день рождения в {year} году не выпадает на выходной.")
#     else:
#         print(result)
# except ValueError:
#     print("Ошибка: Пожалуйста, введите корректные данные.")


# Задание 7   ч 2
# Графік на основі дати. Напишіть функцію, яка будує графік, показуючи активність користувача за датами
# (кількість подій у кожен день місяця).

# import matplotlib.pyplot as plt
# from collections import Counter
# from datetime import datetime
#
# def plot_activity(events):
#     dates = [datetime.strptime(event, '%Y-%m-%d') for event in events]      # преобразуем строки в объект datetime
#
#     day_counts = Counter([date.day for date in dates])                      # количество событий в каждый день месяца
#
#     days = sorted(day_counts.keys())                                        # сортируем дни месяца
#     counts = [day_counts[day] for day in days]                              # считаем количество событий на каждый день
#
#     # Строим график
#     plt.figure(figsize=(10, 6))
#     plt.plot(days, counts, marker='o', linestyle='-', color='b')
#
#     plt.title("График активности по дням месяца")
#     plt.xlabel("День месяца")
#     plt.ylabel("Количество событий")
#     plt.xticks(range(1, 32))                                    # устанавливаем подписи по оси X для дней от 1 до 31
#     plt.grid(True)
#     plt.show()
#
# events = [
#     "2024-12-01", "2024-12-02", "2024-12-02", "2024-12-05", "2024-12-05",
#     "2024-12-05", "2024-12-07", "2024-12-10", "2024-12-15", "2024-12-15"
# ]
#
# plot_activity(events)


# Задание 8   ч 2
# Таймер зворотного відліку. Функція, яка виводить зворотний відлік до заданої дати й часу

# import time
# from datetime import datetime
#
# def countdown(target_date_str):
#     target_date = datetime.strptime(target_date_str, "%Y-%m-%d %H:%M:%S")       # дату в объект datetime
#
#     while True:
#         current_time = datetime.now()                                       # текущее время
#
#         time_remaining = target_date - current_time                         # разница между текущим временем и заданной датой
#
#         if time_remaining.total_seconds() <= 0:                             # если Обратный отсчет завершен
#             print("Обратный отсчет завершено!")
#             break
#
#         days = time_remaining.days                                      # вычисляем дни, часы, минуты и секунды
#         hours, remainder = divmod(time_remaining.seconds, 3600)
#         minutes, seconds = divmod(remainder, 60)
#
#         print(f"Осталось: {days} дн. {hours:02}:{minutes:02}:{seconds:02}")       # выводим обратный отсчет
#
#         time.sleep(1)                               # задержка на 1 секунду
#
# target_date = "2024-12-31 23:59:59"
# countdown(target_date)


# Задание 9   ч 2
# Обчислення робочих годин. Функція, яка рахує кількість робочих годин між двома датами (виключаючи вихідні).

# from datetime import datetime, timedelta
#
# def count_working_hours(start_date_str, end_date_str):
#     start_date = datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S")         # строки в объект datetime
#     end_date = datetime.strptime(end_date_str, "%Y-%m-%d %H:%M:%S")
#
#     total_working_hours = 0                                         # для подсчета рабочих часов
#
#     if start_date > end_date:                                       # проверяем, начальная дата меньше конечной
#         start_date, end_date = end_date, start_date                 # если нет, меняем местами
#
#     # проходим по каждому дню между датами
#     current_date = start_date
#     while current_date < end_date:
#         if current_date.weekday() < 5:                                      # если это рабочий день
#
#             day_end = min(current_date.replace(hour=18, minute=0, second=0), end_date)          # если это текущий день между началом и концом. считаем время
#             day_start = max(current_date.replace(hour=9, minute=0, second=0), start_date)
#
#             if day_start < day_end:                                             # проверяем, не закончился день до того как начался
#                 total_working_hours += (day_end - day_start).seconds / 3600     # преобразуем в часы
#
#         current_date += timedelta(days=1)                                       # переходим на следующий день
#
#     return total_working_hours
#
# start_date = "2024-12-01 08:00:00"                              # начало
# end_date = "2024-12-05 17:30:00"                                # конец
# working_hours = count_working_hours(start_date, end_date)
# print(f"Количество рабочих часов: {working_hours:.2f}")


# Задание 10   ч 2
# Календар подій. Реалізуйте програму, яка дозволяє додавати події до календаря і виводити їх список за обраний день

# from datetime import datetime
#
# calendar = {}                               # словарь для хранения событий
#
# def add_event():
#     date_str = input("Введите дату события (в формате YYYY-MM-DD): ")
#     try:
#         event_date = datetime.strptime(date_str, "%Y-%m-%d").date()         # проверяем корректность введенной даты
#         event_description = input("Введите описание события: ")
#
#         if date_str not in calendar:                                            # добавляем событие в словарь
#             calendar[date_str] = []
#         calendar[date_str].append(event_description)
#
#         print(f"Событие добавлено на {event_date}: {event_description}")
#     except ValueError:
#         print("Некорректный формат даты! Попробуйте снова.")
#
# def show_events():
#     date_str = input("Введите дату для просмотра событий (в формате YYYY-MM-DD): ")
#     try:
#         event_date = datetime.strptime(date_str, "%Y-%m-%d").date()     # проверка корректности введенной даты
#
#         if date_str in calendar:                                            # вывод событий для указанной даты
#             print(f"События на {event_date}:")
#             for idx, event in enumerate(calendar[date_str], start=1):
#                 print(f"{idx}. {event}")
#         else:
#             print(f"На {event_date} событий нет.")
#     except ValueError:
#         print("Некорректный формат даты! Попробуйте снова.")
#
#
# def main():
#     while True:
#         print("\nМеню:")
#         print("1. Добавить событие")
#         print("2. Показать события")
#         print("3. Выйти")
#
#         choice = input("Выберите действие (1/2/3): ")
#
#         if choice == "1":
#             add_event()
#         elif choice == "2":
#             show_events()
#         elif choice == "3":
#             print("Выход из программы.")
#             break
#         else:
#             print("Некорректный выбор! Попробуйте снова.")
#
# main()