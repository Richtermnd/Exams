C
    res = 0
    nums = [0] * 134
    for x in a:
        if x > 134:
            # Число уже больше чем желаемое.
            continue

        for i in range(x + 1, 134 - x + 1):
            res += nums[i]

        # Записываем в статистику.
        nums[x] += 1
    
    print(res)


solution('A')
solution('B')