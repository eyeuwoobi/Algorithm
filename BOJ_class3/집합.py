import sys

m = int(sys.stdin.readline())
s = set()

for _  in range(m):
    orders = list(map(str, sys.stdin.readline().split()))
    if len(orders) > 1:
        order = orders[0]
        value = int(orders[1])
        if order == 'add':
            s.add(value)
        elif order == 'remove':
            s.discard(value)
        elif order == 'check':
            if value in s:
                print(1)
            else:
                print(0)
        elif order == 'toggle':
            if value in s:
                s.remove(value)
            else:
                s.add(value)
    else:
        order = orders[0]
        if order == 'all':
            s = set([i for i in range(1, 21)])
        elif order == 'empty':
            s = set()