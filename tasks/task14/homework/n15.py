def to_dec(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    for x in range(21, 30):
        if to_dec(x, 3)[-2:] == [1, 1]:
            print(x)


main()
