def to_n(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    # 1. [0; 5 ** 4 - 1]
    # 2. [16: +inf]
    cnt = 0
    for x in range(16, 5 ** 4):
        if hex(x)[-1] == 'c':
            cnt += 1
    print(cnt)


main()