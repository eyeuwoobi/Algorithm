import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
network = [[] for i in range(n+1)]


for _ in range(m):
    x, y = map(int, input().rstrip().split())
    network[x].append(y)
    network[y].append(x)

def BFS(graph, start, visited, linked):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        linked.add(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

linked = set()
visited = [False] * (n+1)
if m == 0:
    print(0)
else:
    BFS(network, 1, visited, linked)
    print(len(linked)-1)