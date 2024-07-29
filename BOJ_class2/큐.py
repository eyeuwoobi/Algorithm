import sys

Q = []

n = int(sys.stdin.readline())

def queue(input):
    if len(input) > 5:
        order, x = map(str, input.split())
        x = int(x)
        Q.append(x)
    if input == 'pop':
        if len(Q) == 0:
            return -1
        else:
            return Q.pop(0)
    if input == 'size':
        return len(Q)
    if input == 'empty':
        if len(Q) == 0:
            return 1
        else:
            return 0
    if input == 'front':
        if len(Q) == 0:
            return -1
        else:
            return Q[0]
    if input == 'back':
        if len(Q) == 0:
            return -1
        else:
            return Q[-1]

for _ in range(n):
    input = sys.stdin.readline().rstrip()
    outcome = queue(input)
    if outcome != None:
        print(outcome)