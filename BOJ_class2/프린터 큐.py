import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    documents = list(map(int, sys.stdin.readline().split()))
    target = documents[m]
    tagger = [0] * n
    tagger[m] = 1
    counter = 0
    while True:
        if max(documents) > documents[0]:
            documents.append(documents[0])
            documents[0:1] = []
            tagger.append(tagger[0])
            tagger[0:1] = []
        else:
            counter += 1
            if tagger[0] == 1:
                print(counter)
                break
            else:
                documents.pop(0)
                tagger.pop(0)
    