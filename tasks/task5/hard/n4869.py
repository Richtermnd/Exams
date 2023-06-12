"""
Алгоритм получает на вход натуральное число N > 1 и строит по нему новое число R следующим образом:
1 Строится двоичная запись числа N.

2 Вычисляется количество единиц, стоящих на чётных местах в двоичной записи числа N без ведущих нулей, 
и количество нулей, стоящих на нечётных местах. Места отсчитываются слева направо (от старших разрядов к младшим, начиная с единицы).

3 Результатом работы алгоритма становится модуль разности полученных двух чисел.

Пример. Дано число N = 39 Алгоритм работает следующим образом:
1 Строится двоичная запись: 3910 = 1001112
2 Выделяем единицы на чётных и нули на нечётных местах: 100111
На чётных местах стоят две единицы, на нечётных – один ноль.
3 Модуль разности равен 1
Результат работы алгоритма R = 1

При каком наименьшем N в результате работы алгоритма получится R = 5?
"""


def f(n):
    r = bin(n)[2:]
    return abs(r[1::2].count('1') - r[::2].count('0'))


def solution():
    for i in range(1, 10000):
        if f(i) == 5:
            print(i)
            break


solution()
