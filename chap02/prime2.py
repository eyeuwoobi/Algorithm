# 1000 이하의 소수를 나열하기(알고리즘 개선 1)

counter = 0
primes = [2]

for n in range(3, 1001, 2):
    for i in primes:
        counter += 1
        if n % i == 0:
            break
    else:
        primes.append(n)
        print(n)

print(f'나눗셈을 실행한 횟수: {counter}')