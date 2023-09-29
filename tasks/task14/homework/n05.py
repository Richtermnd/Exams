def cnt_4_equal_100(x: int, n: int) -> list[int]:
    cnt = 0
    while x:
        cnt += x % n == 4
        x //= n
        if cnt > 100:
            return False
    return cnt == 100


def main():
    for a in range(1000):
        x = 125 ** 200 - 5 ** a + 74
        if cnt_4_equal_100(x, 5):
            print(a)
            break


main()