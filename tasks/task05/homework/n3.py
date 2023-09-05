def f(n):
    r = bin(n)[2:]
    r += r[-1]
    r += '1' if r.count('1') % 2 else '0'
    r += '1' if r.count('1') % 2 else '0'
    return int(r, 2)


def solution():
    i = 1
    while f(i) <= 130:
        i += 1
    print(i)

    
solution()