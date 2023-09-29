def to_dec(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    for i in range(2, 10):
        res = to_dec(68, i)
        if res[-1] == 2 and len(res) == 4:
            print(i)


main()