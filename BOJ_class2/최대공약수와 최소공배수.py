import sys

a, b = map(int, sys.stdin.readline().split())

def Euclidian(a, b):
    while b != 0:
        [a, b] = [b, a%b]
    return a

gcd = Euclidian(a, b)
lcm = abs(a * b) // gcd
print(gcd)
print(lcm)