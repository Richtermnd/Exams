from itertools import product


def main():
    mask = '12345{}6{}8'
    for x, y in product(range(10), repeat=2):
        a = int(mask.format(x, y))
        if a % 17 == 0:
            print(a, a // 17)


main()