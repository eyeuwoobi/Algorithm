#리스트 연습

x = ['John', 'George', 'Paul', 'Ringo']

for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')

for i, name in enumerate(x):
    print(f'x[{i}] = {name}')

for i, name in enumerate(x, 1):
    print(f'{i}번째 = {name}')

for i in x:
    print(i)
