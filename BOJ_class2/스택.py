import sys


tack = []

def stack(input):
    if len(input) > 5:
        order, x = map(str, input.split())
        x = int(x)
        tack.append(x)
        return 
    if input == 'pop':
        if len(tack) == 0:
            return -1
        else:
            return tack.pop()
    if input == 'size':
        return len(tack)
    if input == 'empty':
        if len(tack) == 0:
            return 1
        else:
            return 0
    if input == 'top':
        if len(tack) == 0:
            return -1
        else:
            return tack[-1]
    
n = int(sys.stdin.readline())

for _ in range(n):
    input = sys.stdin.readline().rstrip()
    output = stack(input)
    if output != None:
        print(output)