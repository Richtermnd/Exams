def main():
    s = '1121121121121111'  # аналитика
    while '11' in s:
        if '112' in s:
            s = s.replace('112', '7', 1)
        else:
            s = s.replace('11', '3', 1)
    print(sum(int(x) for x in s))


main()