import sys

N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

max = 0

for a in range(N):
    if cards[a] > M:
        pass
    for b in range(a+1, N):
        for c in range(b+1, N):
            if max <= cards[a] + cards[b] + cards[c] <= M:
                max = cards[a] + cards[b] + cards[c]
print(max)