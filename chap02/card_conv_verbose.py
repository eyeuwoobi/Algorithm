# 10진수 정수값을 받아 2~36진수로 변환하여 출력하기

def card_conv(x: int, r:int) -> str:
    """정숫값 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열을 반환"""
    d = ''
    char = '0123456789ABCDEFGHIJKLMNOPQRSTUWXYZ'

    while x > 0:
        d += char[x % r]
        print(f'{r} | {x}...{x % r}')
        print(' +----')
        x = x // r
    print(f'  0...{x%r}')
    return d[::-1]

if __name__ == '__main__':
    print('10진수를 n진수로 변환합니다.')
    while True:
        while True:
            no = int(input('변환할 값으로 음이 아닌 정수를 입력하세요.: '))
            if no > 0:
                break
            
        while True:
            cd = int(input('어떤 진수로 변환할까요?: '))
            if 2 <= cd <= 36:
                break
        
        print(f'{cd}진수로는 {card_conv(no, cd)}입니다.')

        retry = input('한번 더 변환할까요?(Y ... 예 / N ... 아니요): ')
        if retry in {'N', 'n'}:
            break