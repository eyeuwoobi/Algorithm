import sys

input = sys.stdin.readline

n = int(input())

dp = [0, 1, 2]

while len(dp) < 1001:
    dp.append(dp[-1]+dp[-2])

print(dp[n]%10007)