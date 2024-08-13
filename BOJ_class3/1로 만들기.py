import sys

input = sys.stdin.readline

n = int(input())

dp = [0, 0, 1, 1, 2, 3]

while len(dp) < n + 1:
    num = len(dp)
    if num % 2 == 0:
        if num % 3 == 0:
            dp.append(min(dp[num//2], dp[num//3], dp[num-1])+1)
        else:
            dp.append(min(dp[num//2], dp[num-1])+1)
    elif num % 3 == 0:
        dp.append(min(dp[num//3], dp[num-1])+1)
    else:
        dp.append(dp[num-1]+1)

print(dp[n])