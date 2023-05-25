"""
НЕ РЕШЕНО

Условие дурацкое.
"""

graph_ = {
    'А': 'БВГ',
    'Б': 'Д',
    'В': 'ДЕ',
    'Г': 'ВЕ',
    'Д': 'К',
    'Е': 'ДЛЖИ',
    'Ж': 'ЛМ',
    'З': '',
    'И': 'МН',
    'К': 'ПМ',
    'Л': 'КМ',
    'М': 'ПСРН',
    'Н': 'Р',
    'П': 'С',
    'Р': 'С',
    'С': '',
}

# Вот тут я осознал, что нужно было делать обратный(?) граф
graph = {}
for key, value in graph_.items():
    for c in value:
        if c not in graph:
            graph[c] = ''
        graph[c] += key
graph['А'] = ''
print(graph)


res = set()


def func(path):
    if len(path) > 1:
        res.add(path)
    [func(path + c) for c in graph[path[-1]]]
    
func('С')
print(*sorted(res), sep='\n')
print(len(res))