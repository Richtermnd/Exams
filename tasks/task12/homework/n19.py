def main():
    a = 'кара'
    i = len(a)
    b = 'т'
    while i > 1:
        c = a[i - 1]
        b += c
        i -= 1
    print(b)


main()