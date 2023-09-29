def to_n(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def f(x, y):
    a = 1 * 21 ** 4 + \
        2 * 21 ** 3 + \
        y * 21 ** 2 + \
        x * 21 ** 1 + \
        9 * 21 ** 0
            
    b = 3 * 21 ** 4 + \
        6 * 21 ** 3 + \
        y * 21 ** 2 + \
        9 * 21 ** 1 + \
        9 * 21 ** 0
    
    return a + b

def main():
    for x in range(21):
        if all(f(x, y) % 18 == 0 for y in range(21)):
            print(f(x, 5) // 18)


main()