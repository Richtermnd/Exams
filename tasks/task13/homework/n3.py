graph = {
    'А': 'БГДЕ',
    'Б': 'В',
    'В': 'ИЖ',
    'Г': 'БВЖД',
    'Д': 'ЖЗ',
    'Е': 'ДЗК',
    'Ж': 'Л',
    'З': 'ЖЛ',
    'И': 'ЖЛ',
    'К': 'ЗЛМ',
    'Л': '',
    'М': 'Л',
    'Н': ''
}


def func(path, finish):
    if len(path) > 1 and path[-1] == finish:
        return 'Ж' in path and 'З' not in path
    
    return sum([func(path + c, finish) for c in graph[path[-1]]])
    

print(func('А', 'Л'))