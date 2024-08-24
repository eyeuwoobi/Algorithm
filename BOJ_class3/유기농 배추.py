import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

def dfs(x,y):
    if x <= -1 or y <= -1 or x >= m or y >= n:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

        
def bfs(a,b):
    q = deque()
    q.append((a,b))
    while q:
        x, y = q.popleft()
        if graph[y][x] == 1:
            graph[y][x] = 0
            visited[y][x] = True
            for off in [-1, 1]:
                if x+off < 0 or x+off >= m:
                    pass
                elif not visited[y][x+off]:
                    q.append((x+off, y))
                if y+off < 0 or y+off >= n:
                    pass
                elif not visited[y+off][x]:
                    q.append((x, y+off))
    return 1



for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for i in range(m)] for j in range(n)]
    visited = [[False for i in range(m)] for j in range(n)]
    for __ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    result = 0


    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                result += bfs(j, i)
    print(result)

