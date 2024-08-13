import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    d = dict()
    counter = 1
    if n == 0:
        print(0)
        continue
    for __ in range(n):
        name, type = map(str, input().rstrip().split())
        if type not in d:
            d[type] = [name]
        else:
            d[type].append(name)
    for key in d.keys():
        counter *= len(d[key])+1
    counter -= 1
    print(counter)