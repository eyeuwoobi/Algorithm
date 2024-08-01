import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    documents = deque(list(map(int, sys.stdin.readline().split())))
    target = documents[m]
    tagger = deque([0] * n)
    tagger[m] = 1
    counter = 0
    while True:
        if max(documents) > documents[0]:
            documents.append(documents[0])
            documents = documents[1:]
            
    