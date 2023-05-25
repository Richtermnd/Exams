graph = {
    'А': 'Г',
    'Б': 'А',
    'В': 'БГ',
    'Г': 'ВД',
    'Д': 'АБВ'
}


def func(path, finish):
    if path.count(path[-1]) > 2:
        return 0
    if len(path) > 1 and path[-1] == finish:
        return 1
    return sum([func(path + c, finish) for c in graph[path[-1]]])
    

print(func('А', 'А'))
