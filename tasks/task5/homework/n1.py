def solution():
    for i in range(100):
        # 1
        r = bin(i)[2:]
        r += str(sum(int(x) for x in r) % 2)
        r += str(sum(int(x) for x in r) % 2)
        r = int(r, 2)

        if r > 80:
            print(r)
    

solution()