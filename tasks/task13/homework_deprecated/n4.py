graph = {
    'a': 'bcde',
    'b': 'fg',
    'c': 'bgh',
    'd': 'ch',
    'e': 'dhi',
    'f': 'j',
    'g': 'fjk',
    'h': 'gk',
    'i': 'hkl',
    'j': 'm',
    'k': 'jlm',
    'l': 'm',
    'm': ''
}


def func(path, finish):
    if len(path) > 1 and path[-1] == finish:
        return 1
    return sum([func(path + c, finish) for c in graph[path[-1]]])
    

print(func('a', 'm'))