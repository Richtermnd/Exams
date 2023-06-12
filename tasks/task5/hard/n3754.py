"""
Алгоритм получает на вход натуральное число N ≥ 10 и строит по нему новое число R следующим образом:
1) Все пары соседних цифр в десятичной записи N рассматриваются как двузначные числа (возможно, с ведущим нулём).

2) Из списка полученных на предыдущем шаге двузначных чисел выделяются наименьшее и наибольшее.

3) Результатом работы алгоритма становится сумма найденных на предыдущем шаге двух чисел.

Пример. Дано число N = 2022 Алгоритм работает следующим образом:
1) В десятичной записи выделяем двузначные числа: 20, 02, 22
2) Наименьшее из найденных чисел 02, наибольшее 22
3) 02 + 22 = 24
Результат работы алгоритма R = 24

При каком наименьшем N в результате работы алгоритма получится R = 137?
"""


def f(n):
    r = str(n)
    nums = [int(r[i: i + 2]) for i in range(len(r) - 1)]
    return max(nums) + min(nums)


def solution():
    for i in range(10, 10000000):
        if f(i) == 137:
            print(i)
            break

solution()
# print(f(2022))