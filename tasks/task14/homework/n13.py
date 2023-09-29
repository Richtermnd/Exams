def to_n(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    for n in range(4, 100):
        if int('132', n) + 0o13 == int('124', n + 1):
            print(n)
            break


main()