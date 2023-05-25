graph = {
    'А': 'БВ',
    'Б': 'ВГ',
    'В': 'Г',
    'Г': 'ДЕЗЖ',
    'Д': 'ЕИ',
    'Е': 'ИКЗ',
    'Ж': 'ЗЛ',
    'З': 'КЛ',
    'И': 'КМ',
    'К': 'М',
    'Л': 'КМ',
    'М': '',
    'Н': ''
}


def func(path, finish):
    if len(path) > 1 and path[-1] == finish:
        return 'Е' in path
    return sum([func(path + c, finish) for c in graph[path[-1]]])
    

print(func('А', 'М'))