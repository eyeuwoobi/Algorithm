import sys

N = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))

scores.sort()

M = scores[-1]

sum = sum(scores)
sum_rivisited = (sum / M) * 100

print(sum_rivisited / N)