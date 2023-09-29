def to_n(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    for x in range(4, 100):
        if int('21', x) * int('13', x) == int('313', x):
            print(x)
            break


main()