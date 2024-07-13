N, X = map(int, input().split())
A = list(map(int, input().split()))

low = []

for _ in A:
    if _ < X:
        low.append(_)

print(*low, sep=' ')