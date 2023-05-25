graph = {
    'А': 'Б',
    'Б': 'Д',
    'В': 'А',
    'Г': 'БВЕ',
    'Д': 'Ж',
    'Е': 'ВК',
    'Ж': 'Г',
    'З': 'ДЖ',
    'К': 'З'
}


def func(path: str):
    if path.count(path[-1]) == 2:
        return 1
    return sum([func(path + c) for c in graph[path[-1]]])
    

print(func('Е'))