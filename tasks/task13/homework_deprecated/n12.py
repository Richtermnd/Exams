graph = {
    'А': 'БЖ',
    'Б': 'ВЗ',
    'В': 'Г',
    'Г': 'ЗЖД',
    'Д': 'КЕАЖ',
    'Е': 'ИА',
    'Ж': 'З',
    'З': 'АВ',
    'И': 'А',
    'К': 'Е',
    'Л': '',
    'М': '',
    'Н': ''
}


def func(path, finish):
    if len(path) > 1 and path[-1] == finish:
        return 1
    if len(set(path)) != len(path):
        return 0
    return sum([func(path + c, finish) for c in graph[path[-1]]])
    

print(func('З', 'З'))