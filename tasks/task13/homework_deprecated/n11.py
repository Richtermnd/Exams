graph = {
    'А': 'БГ',
    'Б': 'ДЕ',
    'В': 'БАГ',
    'Г': 'ЕЖ',
    'Д': 'ЕЛИ',
    'Е': 'ВЛ',
    'Ж': 'Е',
    'З': '',
    'И': 'Л',
    'К': 'Ж',
    'Л': 'ЖК',
    'М': '',
    'Н': ''
}


def func(path, finish):   
    if len(path) > 1 and path[-1] == finish:
        return len(set(path)) == len(path) - 1
    return sum([func(path + c, finish) for c in graph[path[-1]]])
    

print(func('Е', 'Е'))