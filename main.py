from string import ascii_lowercase as low, ascii_uppercase as up, punctuation as punc



# a = input().split()
# a1 = int(a[0])
# a2 = int(a[1])
# count = 0
# while a1 <= a2:
#     count += 1
#     a1*=3
#     a2*=2
#     if a1 > a2:
#         print(count)
# import a
from typing import Tuple

# numbers = [2, 3, 7, 9, 5, 0, 6, 3, 6, 0, 1, 7, 9, 4, 4, 4, 2, 2, 6, 9, 1, 7, 0, 3, 8, 1, 0, 3, 8, 0, 8, 4, 0, 2, 3,
# 6, 6, 1, 5, 8, 7, 2, 3, 8, 7, 7, 1, 2, 2, 8, 4, 3, 4, 8, 0, 7, 9, 8, 3, 7, 7, 7, 7, 5, 1, 7, 4, 5, 0, 8, 0, 9, 2,
# 4, 7, 6, 6, 5, 9, 7, 1, 7, 8, 8, 3, 4, 9, 7, 6, 4, 2, 0, 0, 0, 9, 4, 0, 9, 4, 4, 4, 5, 5, 4, 2, 5, 9, 4, 8, 1, 5,
# 7, 1, 0, 2, 6, 8, 7, 2, 7, 9, 3, 6, 4, 7, 5, 0, 7, 2, 0, 8, 2, 9, 8, 6, 4, 4, 7, 5, 5, 9, 4, 9, 5, 6, 9, 1, 1, 3,
# 1, 5, 2, 1, 7, 0, 0, 7, 8, 1, 3, 0, 0, 4, 4, 3, 3, 6, 7, 8, 6, 1, 2, 0, 2, 0, 9, 9, 0, 5, 2, 4, 1, 7, 4, 9, 9, 4,
# 9, 6, 9, 2, 7, 1, 2, 4, 5, 4, 0, 9, 0] # здесь должен быть ваш код numbers.remove(4) # здесь должен быть ваш код
# print(*numbers)

# let = input()
# while len(let) > 0:
#     let = let[1:-1]
#     print(*let)

# n = int(input())
# count = 1
# s = 0
# while s <= n:
#     s = count ** 2
#     if s <= n:
#         print(s)
#         count += 1

# sum1 = 0
# n = int(input())
# while n != 0:
#     sum1 += n
#     n = int(input())
# print(sum1)

# n = int(input())
# i = 1
# while i <= n:
#     if n % i == 0:
#         print(i)
#     i+=1

# a, b = map(int,input().split())
# #b = int(input())
# while a != b:
#     if a > b:
#         a= a - b
#     else:
#         b = b - a
# print(a)

# import math
# n , m = map(int, input().split())
# print((n * m) // math.gcd(n , m))

# t = 7
# while t > 1:
#     t -= 1
#     if t == 3:
#         break
#     print(t)

# t = 7
# while t > 1:
#     t -= 1
#     if t == 3 or t == 1:
#         continue
#     print(t)

# elements = range(123)
# print(len(elements))
# b = 0
# for i in range(50,101):
#     b+=i**3
# print(b)
# a = list(input().split())  # читаем входной список
# b = []
# c = []
# for i in range(len(a)):
#     if a[i].lower() not in b:
#         b.append(a[i].lower())
#         c.append(a[i])
# print(c)
# def sum_of_digits(n):
#     return sum(int(digit) for digit in str(n))
#
# total_sum = 0
#
# for num in range(1000, 10000):
#     if sum_of_digits(num) == 20:
#         total_sum += num
#
# print("Сумма всех четырёхзначных чисел, сумма цифр которых равна 20, равна:", total_sum)
##a, b = int(input()), list(input().split())
# print(sorted(b))

# a = []
# n = int(input())
# for i in range(n):
#   a.append(list(map(int,input().split())))

# for i in range(n):
#    for j in range(n):
#        if i==j:
#            a[i][j] = 10
#        elif i>j:
#           a[i][j] = 3
#        else:
#            a[i][j] = 5
# for i in a:
#    print(i)

# n = int(input())
# s = 0
# for i in range(n):
#     a = list(map(int,input().split()))
#     s += a[i]
# print(s)

# a, b = map(int, input().split())
# result = [i ** 2 for i in range(a, b + 1)] if a <= b else [i ** 3 for i in range(a, b - 1, -1)]
# print(result)

# st = 'Create a list of the first letters of every word in this string'
# a = st.split()
# print([i[0] for i in a])

# a = (1,)
# b = ('R',)
# c = ('A',)
# d = (2,)
# dd = a*3 + b*5 + c*8 + d*5
# print(dd)

# a = []
# a1,b1 = int(input()), int(input())
# for i in range(a1, b1 + 1):
#    a += a.append(i)
# print(a)

# a = int(input())
# b: tuple = ()
# for i in range(a,a*a+1):
#     if a[i] // 2 != 0:
#         b.append(i)
# print(b)

# sweet = {
#     "id": "0001",
#     "type": "donut",
#     "name": "Cake",
#     "ppu": 0.55,
#     "calories": 125,
# }
# del sweet['ppu']
# del sweet['type']
# print(sweet)
#
# sweet = {
#     "id": "0001",
#     "type": "donut",
#     "name": "Cake",
#     "ppu": 0.55,
#     "calories": 125,
# }
# sweet['wade'] = 230
# sweet['have_topping'] = True
# sweet['name'] = 'SuperCake'
# sweet['calories'] = 350
# print(sweet)

# sp = {}
# num = int(input())
# for i in range(num):
#     name = input()
#     sp[name] = 0
#     if name in sp:
#         print('ОК')
#     else:
#         sp[name] = 1
#         print(name(str(1)))
# stroka = input()
# dig = {}
# for i in range(len(stroka)):
#     if stroka.isalpha()[i]:
#         stroka[i] = dig.get(i, 0) + 1
# print(dig)
# def count_letters(input_string):
#     letter_count = {}
#
#     for char in input_string:
#         if char.isalpha():  # Проверяем, является ли символ буквой
#             char_lower = char.lower()  # Приводим букву к нижнему регистру
#             if char_lower in letter_count:
#                 letter_count[char_lower] += 1  # Увеличиваем счетчик
#             else:
#                 letter_count[char_lower] = 1  # Инициализируем счетчик
#
#     return letter_count
#
#
# # Пример использования
# input_string = input()
# result = count_letters(input_string)
# print(result)

# supermarket = {
#     "milk": {"quantity": 20, "price": 1.19},
#     "biscuits": {"quantity": 32, "price": 1.45},
#     "butter": {"quantity": 20, "price": 2.29},
#     "cheese": {"quantity": 15, "price": 1.90},
#     "bread": {"quantity": 15, "price": 2.59},
#     "cookies": {"quantity": 20, "price": 4.99},
#     "yogurt": {"quantity": 18, "price": 3.65},
#     "apples": {"quantity": 35, "price": 3.15},
#     "oranges": {"quantity": 40, "price": 0.99},
#     "bananas": {"quantity": 23, "price": 1.29}
# }
#
# print(sum([i['price']*i["quantity"] for i in supermarket.values()]))
words = ['mention', 'soup', 'pneumonia', 'tradition', 'concert', 'tease', 'generation',
         'winter', 'national', 'jacket', 'winter', 'wrestle', 'proposal', 'error',
         'pneumonia', 'concert', 'value', 'value', 'disclose', 'glasses', 'tank',
         'national', 'soup', 'feel', 'few', 'concert', 'wrestle', 'proposal', 'soup',
         'sail', 'brown', 'service', 'proposal', 'winter', 'jacket', 'mention', 'tradition',
         'value', 'feel', 'bear', 'few', 'value', 'winter', 'proposal', 'government',
         'control', 'value', 'few', 'generation', 'service', 'national',
         'tradition', 'government', 'mention', 'proposal']

# print(len(a:={i for i in words if len(i)>6}))
# for i in words:
#     if len(i) > 6:
#         print(i)


# letters = input('Введіть Ваші слова: ').lower().split(',')
# let_set = set()
# for phrase in letters:
#     if phrase in let_set:
#         print('ДА')
#     else:
#         print('НЕТ')
#     let_set.add(phrase)

# a = set(map(int, input().split()))
# b = set(map(int, input().split()))
# result = sorted(a.intersection(b))
# print(', '.join(map(str, result)))
# words = ['feel', 'graduate', 'movie', 'fashionable', 'bacon',
#          'drop', 'produce', 'acquisition', 'cheap', 'strength',
#          'master', 'perception', 'noise', 'strange', 'am']
#
# words_with_position = []
# for index, value in enumerate(words, 1):
#     words_with_position.append(((value, index)))
# print(list(words_with_position))

# При помощи enumerate обойдите слова этой коллекции и для каждого элемента выведите строку вида
# english_words = ('attack', 'bless', 'look', 'reckless', 'short', 'monster', 'trolley', 'sound',
#                  'ambiguity', 'researcher', 'trunk', 'coat', 'quantity', 'question', 'tenant',
#                  'miner', 'definite', 'kit', 'spectrum', 'satisfied', 'selection', 'carve',
#                  'ask', 'go', 'suggest')
# for index, value in enumerate(english_words, 1):
#     print(f"Word № {index} = {value}")
#
#  lst = list(map(int, input()))
#  for i in len(lst):
#     if i % 2 == 0:
#         if lst[i] * 2 > 9:
#             lst[i] = lst[i] * 2 - 9
#         else:
#             lst[i] *= 2

# def get_word_indices(strings: list[str]) -> dict:
#     # 1. Инициализируем пустой словарь для хранения индекса слов
#     word_indices = {}
#     # 2. Перебираем входной список строк через цикл, отслеживая индекс с помощью enumerate
#     for i, string in enumerate(strings):
#         # 3. Преобразуем текущую строку в нижний регистр и разбиваем ее на список слов
#         words = string.lower().split()
#
#         # 4. Перебираем в цикле слова в текущей строке
#         for word in words:
#             # 5. Добавляем условия для обновления словаря
#             if word not in word_indices:
#                 # Если слово еще не является ключом, создаем новую пару ключ-значение
#                 word_indices[word] = [i]
#             else:
#                 # Если слово уже является ключевым, добавляем текущий индекс к существующему списку
#                 word_indices[word].append(i)
#
#     # 6. Возвращаем словарь
#     return word_indices

# inp = input()
# print(1,2,3,4,5, sep=inp)

# num = int(input())
# sum_results = 0
# for i in str(num):
#     sum_results += i
# sum_results = int(sum_results)
# print(sum_results)

# letter = input()
# for let in letter:
#     if let == 'a' or let == 'e':
#         print('Ага! Нашлась')
#         break
#     else:
#         print(f'Текущая буква: {let}')
# if 'a' not in letter and 'e' not in letter:
#     print('Распечатали все буквы')

# a, b = int(input()), int(input())
# for i in range(a, b+1):
#     print(f"Число {i}; его квадрат = {i**2}; его куб = {i**3}")

# a = int(input())
# count = 0
# for i in range(a):
#     if i % 3 == 0 or i % 5 == 0:
#         count+=i
# print(count)

# a = int(input())
# for i in range(a):
#     b = input()
#     if len(b) < 10:
#         print(b)
#     else:
#         print(f"{(b[0], len(b), b[-1])}")

# n = map(list(int,input()))
# a = []
# for i in n:
#     a += i
# print(min(a))

# a = input().split()
# count_num = 0
# count_sum = 0
#
# for i in a:
#     for j in i:
#         if j.isdigit():  # Проверяем, является ли символ цифрой
#             count_num += 1
#             count_sum += int(j)  # Добавляем значение цифры к сумме
#
# print(f"{count_num}, {count_sum}")

# import pprint
# import os
# pprint.pprint(os.environ)
# import sys
# print(sys.getrecursionlimit())

