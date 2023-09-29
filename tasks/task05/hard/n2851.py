def f(n):
    r = bin(n)[2:]
    ones = sum(x == '1' for x in r[1::2])
    zeros = sum(x == '0' for x in r[::2])
    return abs(ones - zeros)


for i in range(2, 10000):
    if f(i) == 5:
        print(i)
        break
