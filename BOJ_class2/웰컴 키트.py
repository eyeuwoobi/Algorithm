import sys

N = int(sys.stdin.readline())
order_by_size = list(map(int, sys.stdin.readline().split()))
T, P = map(int, sys.stdin.readline().split())

bundles_Tshirts = 0

for orders in order_by_size:
    if orders % T == 0:
        bundles_Tshirts += orders // T
    else:
        bundles_Tshirts += orders // T + 1

print(bundles_Tshirts)
print(N // P, N % P)