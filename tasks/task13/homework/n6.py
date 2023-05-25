graph = {
    'А': 'БВГД',
    'Б': 'Е',
    'В': 'БК',
    'Г': 'ВЗД',
    'Д': 'ЗИ',
    'Е': 'КЖ',
    'Ж': 'К',
    'З': 'КИ',
    'И': 'Ж',
    'К': '',
    'Л': '',
    'М': '',
    'Н': ''
}


def func(path, finish):
    if len(path) > 1 and path[-1] == finish:
        return 'Е' not in path
    return sum([func(path + c, finish) for c in graph[path[-1]]])
    

print(func('А', 'К'))