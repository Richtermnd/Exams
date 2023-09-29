def to_n(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    for n in range(3, 100):
        a = to_n(68, n)
        if a[-1] == 2 and len(a) == 4:
            print(n)

main()