graph = {
    'А': 'БГД',
    'Б': 'ВГ',
    'В': 'ЗКЕ',
    'Г': 'ВЕЖ',
    'Д': 'Г',
    'Е': 'ЖИМК',
    'Ж': 'И',
    'З': 'ЛК',
    'И': 'М',
    'К': 'ЛМН',
    'Л': 'Н',
    'М': 'Н',
    'Н': ''
}


def func(path, finish):
    if len(path) > 1 and path[-1] == finish:
        cond1 = 'Г' in path
        cond2 = 'Е' in path
        return  cond1 ^ cond2
    return sum([func(path + c, finish) for c in graph[path[-1]]])
    

print(func('А', 'Н'))