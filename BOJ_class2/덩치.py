import sys

n = int(sys.stdin.readline())

properties = []
rank = []

for _ in range(n):
    properties.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    k = 0
    for j in range(n):
        if properties[i][0] < properties[j][0] and properties[i][1] < properties[j][1]:
            k += 1
    rank.append(k+1)

print(*rank, sep=' ')