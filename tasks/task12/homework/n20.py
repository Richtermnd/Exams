def main():
    a = 'ИНФОРМАТИКА'
    m = 10
    b = a[m - 1]
    for k in 4, 5:
        c = a[k - 1]
        b += c
    for k in 1, 2, 3:
        c = a[k - 1]
        b += c
    print(b)


main()