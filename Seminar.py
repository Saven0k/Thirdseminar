from time import time


'''

!!
Пожалуйста посмотрите на данное решение скажите оно правильное?
!!


1. Реализуйте алгоритм задания случайных чисел без использования встроенного
генератора псевдослучайных чисел.

time_ = int(time())
time2_ = int(time_ / 10000000)
print(time2_)


N = int(input("Введите колличство чисел: "))

def random_number(n):
    print(time())
    result = []
    a = 1
    time_ = int(time())
    while a <= n:
        for i  in range(n):
            result.append(time_ % a)
            a+=10
    print(result)

random_number(N)


'''






'''
2. Задайте список. Напишите программу, которая определит, присутствует ли в
заданном списке строк некое число.
['22', '33', '123', 'fwefe', 'ytyy', '55']

f(n)



spisok = ['22', '33', '123', 'fwefe', 'ytyy', '55']

number = int(input("Enter some number: "))

def find_some_number(some_number , lst):
    for i in range(len(lst)):
        if lst[i].isdigit() and int(lst[i]) == some_number:
            print("THis number is this list")
find_some_number(number , spisok)



3. Напишите программу, которая определит позицию второго вхождения строки в
списке либо сообщит, что её нет.

*Пример:*

- список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
- список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
- список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
- список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
- список: [], ищем: "123", ответ: -1
'''

spisok1 =  ["qwe", "asd", "zxc", "qwe", "ertqwe"]
spisok2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
spisok3 =  ["йцу", "фыв", "ячс", "цук", "йцукен"]
spisok4 = ["123", "234", 123, "567"]

sp1 = "qwe"
sp2 = "йцу"
sp3 = "йцу"
sp4 = "123"


#number = input("Enter some string: ")

def find_second_position_in_list(lst , string):
    count = 0
    temp = 0
    for i in range(len(lst)):
        if lst[i] == string:
            count += 1
            temp = i
            if count == 2:
                break

    print(temp)
find_second_position_in_list(spisok1 , sp1)
find_second_position_in_list(spisok2 , sp2)
find_second_position_in_list(spisok3 , sp3)
find_second_position_in_list(spisok4 , sp4)
