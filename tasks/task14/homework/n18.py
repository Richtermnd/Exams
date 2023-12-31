def to_n(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    # 1. [6; 35]
    # 2. [25, 125]
    for n in range(25, 36):
        if to_n(n, 11)[-1] == 1:
            print(n)


main()