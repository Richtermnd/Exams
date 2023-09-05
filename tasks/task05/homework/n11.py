def f(n):
    r = bin(n)[2:]
     
    return abs(r[1::2].count('1') - r[::2].count('0'))


def solution():
    i = 1
    while f(i) != 5:
        i += 1
    print(i)

    
solution()