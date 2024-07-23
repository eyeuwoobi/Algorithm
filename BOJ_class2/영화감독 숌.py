import sys

N = int(sys.stdin.readline())

x = 667
evil_numbers = [666]
while True:
    if N == len(evil_numbers):
        break
    if str(x).find('666') >= 0:
        evil_numbers.append(x)

    x += 1

print(evil_numbers[-1])