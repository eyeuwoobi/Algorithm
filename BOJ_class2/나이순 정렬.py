import sys

n = int(sys.stdin.readline())
clients = []

for i in range(n):
    clients.append(list(map(str, sys.stdin.readline().split())))
    clients[i].insert(0, i)

clients.sort(key=lambda x : (x[1], x[0]))

for i in range(n):
    print(f'{clients[i][1]} {clients[i][2]}')