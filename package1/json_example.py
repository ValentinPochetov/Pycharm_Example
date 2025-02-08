# import json
# from pprint import pprint
# # dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
# #          'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
# #          'z': 26}
# #
# # json1 = json.dumps(dict1)
# # pprint(json1)
# with open('manager_sales.json', 'r' ) as file:
#     data = json.load(file)
#     result = {}
#
#     # Обработка данных
#     for entry in data:
#         manager = entry['manager']
#         full_name = f"{manager['first_name']} {manager['last_name']}"
#
#         # Суммируем цены машин для каждого менеджера
#         total_sales = sum(car['price'] for car in entry['cars'])
#
#         # Добавляем или обновляем запись в результирующем словаре
#         if full_name in result:
#             result[full_name] += total_sales
#         else:
#             result[full_name] = total_sales
#
#     # Шаг 7: Сортировка по сумме продаж и вывод максимального значения
#     sorted_result = sorted(result.items(), key=lambda item: item[1], reverse=True)
#
#     # Вывод результатов
#     for name, total in sorted_result:
#         print(f"Менеджер: {name}, Общая сумма продаж: {total}")
#
#     # Вывод менеджера с максимальной суммой продаж
#     max_manager = max(sorted_result, key=lambda item: item[1])
#     print(f"nМенеджер с максимальной суммой продаж: {max_manager[0]}, Сумма: {max_manager[1]}")
# def normalize_url(site: str) -> object:
#     # Проверяем наличие http:// или https://
#     if site.startswith("http://"):
#         site = site.replace("http://", "https://")
#     elif not site.startswith("https://"):
#         site = "https://" + site
#
#     return site
from typing import Any


# print(normalize_url('https://httpbin.org/redirect-to?url=http://google.com'))
# def print_numbers(num):
#     while num != 0:
#         print(num)
#         num: int | Any = num - 1
#     print("finished!")

# print_numbers(4)

# def join_numbers_from_range(start, finish):
#     i = start
#     result = []
#     while i <= finish:
#         str(i)
#         result.append(i)
#         i += 1
#     print(*result)
#
# print(join_numbers_from_range(2, 3))

# def join_numbers_from_range(start, finish):
#     i = start
#     result = ""
#     while i <= finish:
#         result += str(i)  # Преобразуем число в строку и добавляем в список
#         i += 1
#     return result
#
# # Теперь вызываем функцию и выводим результат
# output = join_numbers_from_range(1, 5)
# print(output)  # Вывод: 2 3

# def my_substr(string: str, number: int):
#     return string[0:number]

# print(my_substr(input(), int(input())))

def sort_pair(a, b):
    if a < b:
        return (a, b)
    else:
        return (b, a)
print(sort_pair(1,5))