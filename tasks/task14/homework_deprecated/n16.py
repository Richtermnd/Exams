def to_dec(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    i = 40
    while bin(i)[-4:] != '1011':
        i -= 1
    print(i)


main()