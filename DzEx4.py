'''
Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''

def of_10_to_2st():
    number = int(input("Enter number: "))
    temp = ''
    while number > 0:
        temp = str(number % 2) + temp
        number = number // 2
    print(temp)

of_10_to_2st()
