def main():
    s = 46 * '1' + 31 * '2'
    while '111' in s:
        s = s.replace('1111', '2', 1)
        s = s.replace('222', '1', 1)
    print(s)


main()