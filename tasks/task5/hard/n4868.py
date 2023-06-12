"""
Алгоритм получает на вход натуральное число N > 1 и строит по нему новое число R следующим образом:
1 Вычисляется сумма чётных цифр в десятичной записи числа N. Если чётных цифр в записи нет, сумма считается равной нулю.

2 Вычисляется сумма цифр, стоящих на чётных местах в десятичной записи числа N без ведущих нулей. 
Места отсчитываются слева направо (от старших разрядов к младшим, начиная с единицы). Если число однозначное (цифр на чётных местах нет), сумма считается равной нулю.

3 Результатом работы алгоритма становится модуль разности полученных двух сумм.

Пример. Дано число N = 2021 Алгоритм работает следующим образом:
1 Чётные цифры в записи: 2, 0, 2, их сумма равна 4
2 Цифры на чётных местах: 0, 1, их сумма равна 1
3 Модуль разности полученных сумм равен 3
Результат работы алгоритма R = 3

При каком наименьшем N в результате работы алгоритма получится R = 13?
"""


def f(n):
    # 1
    r1 = sum(int(x) for x in str(n) if int(x) % 2 == 0)
    # 2
    r2 = sum(int(x) for x in str(n)[1::2])
    # 3
    return abs(r1 - r2)


def solution():
    for i in range(1, 10000):
        if f(i) == 13:
            print(i)
            break


solution()