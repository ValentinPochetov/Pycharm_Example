# numbers = list(map(int, open("numbers.txt").read().split()))
# number_three_digit = 0
# sum_two_digit = 0
# for i in numbers:
#     if 100 <= i <= 999:
#         number_three_digit += 1
#     if 10 <= i <= 99:
#         sum_two_digit += int(i)
# print(number_three_digit, sum_two_digit, sep='\n')


#print(input().count('7'))
# def truncate(text, length):
#     # BEGIN (write your solution here)
#     return text[:length] + '...'
#
# print(truncate('i love you', 4))

# def get_hidden_card(cards: str, stars: int = 4):
#     print((stars * "*") + cards[-4:])
#
# get_hidden_card(input(), int(input()))

# def trim_and_repeat(text: str, offset: int = 0, repetition: int = 1):
#     new_text = text[offset:]
#     return new_text * repetition
#
# print(trim_and_repeat('hython', 3, 2))

# def letter_multiply(text: str, bukv: str = 1, numbers: int = 1) -> str:
#     zamena = bukv * numbers
#     return text.replace(bukv, zamena)
#
# print(letter_multiply('python', 'p', 2))

# def get_age_difference(year1: int, year2: int):
#     result = year1 - year2
#     return f"The age difference is {abs(result)}"
#
# def  is_leap_year(year: int):
#     if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#         return True
#     else:
#         return False
#
#
# assert is_leap_year(2016)
# assert is_leap_year(2000)
# assert not is_leap_year(2017)
# assert not is_leap_year(2018)
# assert not is_leap_year(1900)
print("Hello WORLD".split())