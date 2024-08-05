import sys

input = sys.stdin.readline

n, m = map(int, input().split())

d = dict()

for _ in range(n):
    name, password = map(str, input().rstrip().split())
    d[name] = password

for _ in range(m):
    name = str(input().rstrip())
    print(d[name])