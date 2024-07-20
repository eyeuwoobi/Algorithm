import sys
import math

a, b, v = map(int, sys.stdin.readline().split())

climbing_per_day = a - b

print(math.ceil((v - a) / climbing_per_day) + 1)