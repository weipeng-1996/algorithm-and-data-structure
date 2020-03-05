graph, start, end = input().strip().split('|')
print(graph, start, end)
graph = list(map(int, filter(str.isdigit, graph)))
start = list(map(int, filter(str.isdigit, start)))
end = int(end)
# print(type(graph[0]), type(start), type(end))
max = max(graph)
arr = [[0 for _ in range(max+1)] for _ in range(max+1)]
i = 1
l = len(graph)
while i < l:
    arr[graph[i-1]][graph[i]] = graph[i]
    i += 2


def findallpath(graph, start, end, path = []):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node!= 0 and node not in path:
            newpaths = findallpath(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

result = []
for i in start:
    paths = findallpath(arr, i, end)
    if paths:
        for j in paths:
            result.extend(j)
result = set(result)
result = list(result)
result.sort()
print(result)



