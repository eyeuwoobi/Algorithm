import sys

input = sys.stdin.readline

t = int(input())



for _ in range(t):
    n = int(input())
    P = [0, 1, 1, 1, 2, 2]
    if n <= 5:
        print(P[n])
    else:
        while len(P) < n + 1:
            P.append(P[-1]+P[-5])
        print(P[-1])