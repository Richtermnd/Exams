import itertools as it


alph = '0234567'
res = it.product(alph, repeat=5)
res = map(lambda x: ''.join(x), res)
res = filter(lambda x: x[0] != '0', res)
res = filter(lambda x: len(x) == len(set(x)), res)
res = map(lambda x: (
    x.replace('2', '0')
    .replace('4', '0')
    .replace('6', '0')
    .replace('3', '1')
    .replace('5', '1')
    .replace('7', '1')
    .replace('9', '1')
    ), 
    res)
res = filter(lambda x: '11' not in x and '00' not in x, res)
res = len(list(res))
print(res)