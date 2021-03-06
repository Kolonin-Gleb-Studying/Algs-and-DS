# Источник кода
# https://pimiento.github.io/python_graphs.html
# 
'''
Будет использоваться ненаправленный связный граф V=6 E=6.
Существует две популярные методики представления графов: матрица смежности (эффективна с плотными графами)
и список связей (эффективно с разряженными графами).

Плотный граф - граф, имеющий число ребер близкое к максимально возможному с его числом вершин.

Разряженный граф - граф, в котором число ребер далеко от максимального.

Будем использовать второй способ, т.к. наш граф - разряженный
'''

# Граф в виде списков связностей
graph = {
'A': ['B', 'C'],
'B': ['A', 'D', 'E'],
'C': ['A', 'F'],
'D': ['B'],
'E': ['B', 'F'],
'F': ['C', 'E']
}

# Поиск в ширину на деке и множествах
from queue import deque

def bfs(graph, start):
    visited, queue = [], deque([start])
    while queue:
        vertex = queue.pop()
        if vertex not in visited:
            visited.append(vertex)
            queue.extendleft(set(graph[vertex]) - set(visited))
    return visited

print(bfs(graph, 'A'))
# Здесь алгоритм BFS написан с использованием множеств.
# В связи с этим порядок вывода каждый раз разный (множество - неупор. структура данных)
