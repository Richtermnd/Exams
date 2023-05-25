graph = {
    'А': 'БВГД',
    'Б': 'ВЕ',
    'В': 'Ж',
    'Г': 'ВЖ',
    'Д': 'ГЖЗ',
    'Е': 'ЖИ',
    'Ж': 'И',
    'З': 'ЖИ',
    'И': 'КЛМ',
    'К': 'М',
    'Л': 'М',
    'М': '',
    'Н': ''
}


def func(path, finish):
    if len(path) > 1 and path[-1] == finish:
        return 'Ж' in path and 'К' not in path
    return sum([func(path + c, finish) for c in graph[path[-1]]])


print(func('А', 'М'))
