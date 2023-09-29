def to_n(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    for x in range(21, 29):
        if to_n(x, 3)[-2:] == [1, 1]:
            print(x) 


main()