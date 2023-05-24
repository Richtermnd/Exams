import itertools as it


def func(p1, p2, p3, p4):
    return (p3 <= p1) <= (p4 or not p2)


table = [
    {
        (0, 0, 0, 1): 0,
        (0, 0, 1, 1): 0,
    },
    {
        (0, 1, 0, 1): 0,
        (0, 1, 1, 1): 0,
    },
    {
        (1, 1, 0, 0): 0,
        (1, 1, 0, 1): 0,
        (1, 1, 1, 0): 0,
        (1, 1, 1, 1): 0,
    }
]

res_set = set()

for row in table:
    temp_set = set()

    for key, value in row.items():
        temp = dict(zip('xyzw', key))
    
        for key_args in set(it.permutations(temp.keys())):
            args = map(lambda key: temp[key], key_args)

            if func(*args) == value:
                temp_set.add(key_args)
    
    # Если множество не пустое, то пересечение
    if res_set:
        res_set = res_set & temp_set
    # Иначе просто переприсваиваем
    else:
        res_set = temp_set
print(res_set)
