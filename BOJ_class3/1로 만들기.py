import sys
from copy import copy

input = sys.stdin.readline

n = int(input())
m = copy(n)
counter_f = 0
counter_s = 0

while n > 1:
    if n % 3 == 0:
        counter_f += 1
        n //= 3
    elif n % 3 == 1:
        counter_f += 1
        n -= 1
    elif n % 2 == 0:
        counter_f += 1
        n //= 2
    else:
        n -= 1
        counter_f += 1

while m > 1:
    if m % 3 == 0:
        counter_s += 1
        m //= 3
    elif m % 2 == 0:
        counter_s += 1
        m //= 2
    elif m % 3 == 1:
        counter_s += 1
        m -= 1
    else:
        m -= 1
        counter_s += 1
    print(m)

print(min(counter_f, counter_s))

# 짝수인데 mod 3 = 1인 경우가 문제임.
# 그럴 때마다 분기점 나눠서 계산하는게 필요한듯.
