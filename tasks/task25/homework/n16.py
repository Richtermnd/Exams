def div(x: int) -> list[int]:
    res = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)

    return sorted(res)


def main():
    res = []
    for i in range(125_697, 125_721 + 1):
        divs = div(i)[1:-1]
        
        if len(divs) != 2:
            continue
        
        if divs[0] == divs[1]:
            continue
        
        if len(div(divs[0])) == 2 and len(div(divs[1])) == 2:
            res.append((divs[0], divs[1]))
    res.sort(key=lambda x:x[0] * x[1])
    for line in res:
        print(*line)
        

main()
