graph = {
    'А': 'БВГ',
    'Б': 'ДГ',
    'В': 'ГИ',
    'Г': 'ДИ',
    'Д': 'ЕЛЖ',
    'Е': 'ЛК',
    'Ж': 'Л',
    'З': '',
    'И': 'ЕК',
    'К': 'Л',
    'Л': '',
    'М': '',
    'Н': ''
}

roads = {
    'АБ': 40,
    'АВ': 60,
    'АГ': 90,
    'БД': 80,
    'БГ': 30,
    'ВГ': 20,
    'ВИ': 80,
    'ГД': 70,
    'ГИ': 50,
    'ДЕ': 80,
    'ДЛ': 120,
    'ДЖ': 100,
    'ЕЛ': 30,
    'ЕК': 40,
    'ЖЛ': 50,
    'ИЕ': 70,
    'ИК': 30,
    'КЛ': 50,
}


def func(path, finish):
    if len(path) == 1:
        return min([func(path + c, finish) for c in graph[path[-1]]])
    
    if path[-1] == finish:
        return roads[path[-2:]]
    
    return min([roads[path[-2:]] + func(path + c, finish) for c in graph[path[-1]]])
    

print(func('А', 'Л'))