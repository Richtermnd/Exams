import operator
import itertools as it

def check(x, y, z, func):
    return (x == (not y)) or func(not x, z)


op_list = [operator.or_, operator.and_, operator.eq, operator.le]



for op in op_list:
    print(op.__name__)
    print('\tx y z f')
    for args in it.product([0, 1], repeat=3):
        func = lambda args: check(*args, op)
        print(f'\t{" ".join(map(str, args))} {int(func(args))}')


# ответ: 23