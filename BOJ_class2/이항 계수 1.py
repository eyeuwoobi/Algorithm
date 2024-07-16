import sys
import math

N, K = map(int, sys.stdin.readline().split())

combination = math.factorial(N) // (math.factorial(K+1) * math.factorial(K))

print(int(combination))