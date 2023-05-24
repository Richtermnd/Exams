import itertools as it


def func(x, y, z ,w):
    return not (not (x <= (not w)) and z) and not (w <= z) and (x <= (not z))


table = [
    # Можно было бы ставить на место пропусков None и как-то рекурсивно заполнять, но легче ручками.
    {
        (1, 0, 0, 0): 1,
        (1, 0, 1, 0): 1
    },
    {
        (1, 0, 0, 0): 0,
        (1, 0, 0, 1): 0,
        (1, 0, 1, 0): 0,
        (1, 0, 1, 1): 0
    },
    {
        (0, 1, 0, 1): 0,
        (0, 1, 1, 1): 0,
        (1, 1, 0, 1): 0,
        (1, 1, 1, 1): 0
    }
]

cnt = 0
for lttrs in it.permutations('xyzw'):
    all_correct = True
    for row in table:
        is_correct = False
        for key, value in row.items():
            kwargs = dict(zip(lttrs, key))
            if func(**kwargs) == value:
                is_correct = True
        if not is_correct:
            all_correct = False

    if all_correct:
        print(lttrs)
        cnt += 1
print(cnt)

# ответ: 8
    
    

        
