import sys

N = int(sys.stdin.readline())

sum = 0
generator = [0]

for a in range(N // (10**6) + 1):
    for b in range(10):
        if a*(10**6+1) + b*(10**5+1) > N:
            break
        for c in range(10):
            if a*(10**6+1) + b*(10**5+1) + c*(10**4+1)> N:
                break
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        for g in range(10):
                            if a*(10**6+1)+ b*(10**5+1) + c*(10**4+1) + d*(10**3+1) + e*(10**2+1) + f*11 + g*2 == N:
                                generator.append(a*(10**6)+b*(10**5)+c*(10**4)+d*(10**3)+e*(10**2)+f*10+g)


generator.sort()

if len(generator) == 1:
    print(generator[0])
else:
    print(generator[1])