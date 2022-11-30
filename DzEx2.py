'''
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''


def sum_numbers():
    lst = []
    result = []
    n = int(input("Enter size list: "))
    for i in range(n):
        lst.append(int(input("Enter some number: ")))
    print(lst)
    if n % 2 == 0:
        for i in range(0, ((len(lst) // 2))):
            result.append(lst[i] * lst[len(lst) - 1 - i])
    else:
        for i in range(0, ((len(lst) // 2) + 1)):
            result.append(lst[i] * lst[len(lst) - 1 - i])

    print(result)

sum_numbers()



