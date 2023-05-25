graph = {
    'А': 'АБВГД',
    'Б': 'ЕВ',
    'В': 'ЕЖ',
    'Г': 'ВЖ',
    'Д': 'ГЖЗ',
    'Е': 'ЖИ',
    'Ж': 'И',
    'З': 'ЖИ',
    'И': 'КЛМ',
    'К': 'Н',
    'Л': 'КНОПМ',
    'М': 'ПР',
    'Н': 'Я',
    'О': 'НЯ',
    'П': 'ОЯР',
    'Р': 'Я',
    'Я': '',
}


def func(path, finish):
    if len(path) > 1 and path[-1] == finish:
        return (len(path) - 1) % 2
    if path.count(path[-1]) > 1:
        return 0
    return sum([func(path + c, finish) for c in graph[path[-1]]])
    

print(func('А', 'Я'))