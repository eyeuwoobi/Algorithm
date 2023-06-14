# 1000 이하의 소수를 나열하기(알고리즘 개선 2)

counter = 0
primes = [2, 3]

for n in range(5, 1001, 2):
    i = 1
    while primes[i] * primes[i] <= n:
        counter += 2
        if  n % primes[i] == 0:
            break
        i += 1
    else:
        primes.append(n)
        counter += 1

for i in primes:
    print(i)
print(f'나눗셈을 실행한 횟수: {counter}')