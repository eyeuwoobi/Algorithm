#원하는 개수(n)만큼 값을 입력받아 마지막 n개를 저장

n = int(input('정수를 몇 개 저장할까요?: '))
a = [None] * n

cnt = 0
while True:
    a[cnt % n] = int(input())
    
    

    
    
    