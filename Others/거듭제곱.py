import sys
import math

input = sys.stdin.readline

n = int(input())

bin_n = bin(n)

bin_n = bin_n[::-1]


sum = 0
x = 0
for i in bin_n[:-2]:
    sum += int(i) * (3**x)
    x+=1

print(sum)