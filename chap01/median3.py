#세 정수 입력받아 중앙값 구하기

a = int(input('정수 a를 입력하세요.: '))
b = int(input('정수 b를 입력하세요.: '))
c = int(input('정수 c를 입력하세요.: '))

def med3(a, b, c):
    """a, b, c의 중앙값을 구하여 반환"""
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return b
    else:
        return b
