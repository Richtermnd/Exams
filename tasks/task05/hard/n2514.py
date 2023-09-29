"""
Оно не сложно, оно душное.
"""

def f(n):
    r = ''
    for i in range(3):
        r += str(int(str(n)[i * 2]) + int(str(n)[i * 2 + 1]))
    r = int(r)
    r = bin(r)[2:] + str(r % 2)
    return int(r, 2)


for i in range(10 ** 5, 10 ** 6):
    a = f(i)
    if a == 1519 and str(i)[-2] == '9' and '2' in str(i):
        print(i)
        break
