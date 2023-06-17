def to_dec(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    for i in range(25, 49):
        if to_dec(i, 11)[-1] == 1:
            print(i)
            break


main()