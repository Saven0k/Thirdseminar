'''
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''

lst =  [1.1, 1.2, 3.1, 5, 10.01]

def f(lst):
    print(lst)
    for item in lst:
        if item % 1 == 0:
            lst.remove(item)
        else:
            for i in range(0 , len(lst)):
                lst[i] = round((lst[i] - (lst[i] // 1)) , 3)
    result = max(lst) - min(lst)
    print(result)
f(lst)