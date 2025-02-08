# считать название строки и ывести её
# def file_read(file_name: str) -> None:
#     read_name = open(file_name, encoding='utf-8')
#     print(read_name.read())


# def file_n_lines(file_name: str, n: int) -> None:
#     f = open(file_name, 'r', encoding = 'utf-8')
#     for i in range(n):
#         print(f.readline(), end = '')
#
# file_n_lines('hello.txt',3)


# def create_file_with_numbers(n: int) -> None:
#     a = open(f'range_{n}.txt','a',encoding='utf-8')
#     for i in range(n+1)
#         a.writelines(f'{i}\n')
#     a.close()

def open_file(file_name: str):
    with open('lorem.txt', 'r') as f: #открываем файл с помощью контексного менеджера
        f = f.read().upper().split() #читаем, большие, разделить
        words = {}
        for i in f:
            words[i] = f.count(i)
    print(words)
open_file('lorem.txt')
#     with open('lorem.txt', 'r', encoding='UTF-8') as file:
#         print(len(set(word.strip().lower() for word in file.read().split())))
#
# open_file('lorem.txt')