# 10진수 정수값을 받아 2~36진수로 변환하여 출력하기

def card_conv(x: int, r:int) -> str:
    """정숫값 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열을 반환"""
    d = ''
    char = '0123456789ABCDEFGHIJKLMNOPQRSTUWXYZ'
    while x // r != 0:
        d += char[x % r]
        x = x // r
    return d[::-1]

if __name__ == '__main__':
    x = int(input('정숫값 x를 입력하세요.: '))
    r = int(input('진수를 입력하세요.: '))
    print(f'{x}는 {r}진수로 {card_conv(x, r)}입니다.')
