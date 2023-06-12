def f(n):
    a = n
    r = ''
    while a:
        r += str(a % 3)
        a //= 3
    r = r[::-1]
    r += str(n % 3)
    return int(r, 3)


def solution():
    for i in range(100):
        if f(i) >= 100:
            print(f(i))

    
solution()