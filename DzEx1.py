'''
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''


def sum_numbers():
    lst = []

    for i in range(5):
        lst.append(int(input("Enter some number: ")))
    print(lst)
    result = 0
    for i in range(1 , len(lst), 2):
        result += lst[i]
    print(result)
sum_numbers()