import sys

T = int(sys.stdin.readline())


for _ in range(T):
    status = []
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    status.append([])
    for i in range(1, n+1):
        status[0].append(i)
    for i in range(1, k+1):
        status.append([])
        for room in range(n):
            status[i].append(sum(status[i-1][0:room+1]))    
    print(status[k][n-1])