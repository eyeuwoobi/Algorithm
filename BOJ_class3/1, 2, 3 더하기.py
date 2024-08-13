import sys

input = sys.stdin.readline

dp = [0, 1, 2, 4]

t = int(input())
m = 4
while m < 11:
    dp.append(dp[m-3]+dp[m-2]+dp[m-1])
    m+=1

for _ in range(t):
    n = int(input())
    print(dp[n])