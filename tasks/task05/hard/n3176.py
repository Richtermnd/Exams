"""
На вход алгоритму Галиб-001 подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом:
1) Строится девятиричная запись числа N.

2) Подсчитывается количество пятёрок и семёрок в полученной записи. Если их количество одинаково, в конец записи добавляется её последняя цифра. 
В противном случае в конец записи добавляется цифра, которая встречается чаще. Если таких цифр несколько, выбирается наибольшая по значению.

3) Шаг 2 повторяется ещё четыре раза.

4) Результат переводится в шестнадцатиричную систему счисления.

При каком наибольшем исходном числе N < 10000 в результате работы алгоритма получится число, которое содержит в себе сочетание BAC?  
"""


def f(n):
    # 1
    temp = n
    r = ''
    while temp:
        r += str(temp % 9)
        temp //= 9
    r = r[::-1]

    # 2-3
    for _ in range(5):
        if r.count('5') == r.count('7'):
            r += r[-1]
        else:
            r += max(r, key=lambda x: (r.count(x), int(x)))
    
    # 4
    return hex(int(r, 9))[2:]


def solution():
    i = 9_999
    while 'bac' not in f(i):
        i -= 1
    print(i) 


solution()