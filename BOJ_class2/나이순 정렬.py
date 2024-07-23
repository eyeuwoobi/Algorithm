import sys

n = int(sys.stdin.readline())
clients = []

for _ in range(n):
    clients.append(list(map(int, sys.stdin.readline().split())))
