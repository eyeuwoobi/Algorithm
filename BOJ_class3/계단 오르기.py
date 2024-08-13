import sys

input = sys.stdin.readline

n = int(input())
stairs = [0 for i in range(n+1)]
dp = [0 for i in range(n+1)]

for i in range(1, n+1):
    stairs[i] = int(input())

if n == 1:
    print(stairs[1])
    exit()
elif n == 2:
    print(sum(stairs))
    exit()

dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i])

print(dp[-1])