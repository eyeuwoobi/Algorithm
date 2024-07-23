import sys


counter = 1
while True:
    try:
        i = int(sys.stdin.readline())
        break
    except ValueError:
        counter += 1

i += (4 - counter)

if i % 3 == 0:
    if i % 5 == 0:
        print('FizzBuzz')
    else:
        print('Fizz')
elif i % 3 != 0 and i % 5 == 0:
    print('Buzz')
else:
    print(i)