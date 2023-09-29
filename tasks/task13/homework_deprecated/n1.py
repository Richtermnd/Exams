"""
Аналитически быстрее
"""

graph = {
    'А': '',
    'Б': '',
    'В': '',
    'Г': '',
    'Д': '',
    'Е': '',
    'Ж': '',
    'З': '',
    'И': '',
    'К': '',
    'Л': '',
    'М': '',
    'Н': ''
}


def func(path, finish):
    if len(path) > 1 and path[-1] == finish:
        return 1
    return sum([func(path + c, finish) for c in graph[path[-1]]])
    

print(func('А', 'А'))