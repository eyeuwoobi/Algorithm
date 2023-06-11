# +와 -를 번갈아 출력하기 1a

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))

for i in range(n // 2):
    print('+-', end='')

if n % 2 == 1:
    print('+')
else:
    print()
