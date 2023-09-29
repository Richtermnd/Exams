graph = {
    'А': 'БВГД',
    'Б': 'ЕВ',
    'В': 'Ж',
    'Г': 'ВЖ',
    'Д': 'ГЖЗ',
    'Е': 'ЖИ',
    'Ж': 'И',
    'З': 'ЖИ',
    'И': 'КЛ',
    'К': 'М',
    'Л': 'КМ',
    'М': '',
    'Н': ''
}


def func(path, finish):
    if len(path) > 1 and path[-1] == finish:
        return len(path) - 1
    return max([func(path + c, finish) for c in graph[path[-1]]])
    

print(func('А', 'М'))