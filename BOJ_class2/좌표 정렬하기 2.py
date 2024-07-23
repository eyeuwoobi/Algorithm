import sys

n = int(sys.stdin.readline())
coords = []

for _ in range(n):
    coords.append(list(map(int, sys.stdin.readline().split())))

coords.sort(key=lambda x : (x[1], x[0]))

for i in range(n):
    print(f'{coords[i][0]} {coords[i][1]}')