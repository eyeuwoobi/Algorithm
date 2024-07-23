import sys

N = int(sys.stdin.readline())

def facto(n):
    if n == 0 or n == 1:
        return 1
    return n * facto(n-1)

fact_n = facto(N)
counter = 0
for i in range(1, len(str(fact_n))):
    if fact_n % (10 ** i) == 0:
        counter += 1
    else:
        break

print(counter)
