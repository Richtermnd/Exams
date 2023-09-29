def to_dec(x: int, n: int) -> list[int]:
    a = []
    while x:
        a = [x % n] + a
        x //= n
    return a


def main():
    cnt = 0
    for i in range(17, 625):
        if to_dec(i, 16)[-1] == 12:
            cnt += 1
    print(cnt)


main()