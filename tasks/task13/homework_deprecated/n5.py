graph = {
    'a': 'bcd',
    'b': 'ef',
    'c': 'bfghid',
    'd': 'i',
    'e': 'lg',
    'f': 'eg',
    'g': 'lmkj',
    'h': 'g',
    'i': 'hgj',
    'j': 'k',
    'k': 'm',
    'l': 'm',
    'm': ''
}


def func(path, finish):
    if len(path) > 1 and path[-1] == finish:
        return 'e' in path
    return sum([func(path + c, finish) for c in graph[path[-1]]])
    

print(func('a', 'm'))