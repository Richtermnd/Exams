def to_n(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    for x in range(100):
        if int('33', x + 4) - int('33', 4) == 33:
            print(x)
            break


main()