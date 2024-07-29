import sys

n = int(sys.stdin.readline())

probs = []

for _ in range(n):
    probs.append(list(map(str, sys.stdin.readline().split())))

probs.sort(key=lambda x : x[1])
print(probs[0][0])