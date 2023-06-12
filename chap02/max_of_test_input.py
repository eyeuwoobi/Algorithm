# 배열 원소의 최댓값을 구해서 출력하기(원솟값을 입력받음)

from max import max_of

print('배열의 최댓값을 구합니다.')
print('주의: "End"를 입력하면 종료합니다.')

nums = list()

while True:
    n = input('입력하세요.: ')
    if n == 'End':
        break
    else:
        n = int(n)
        nums.append(n)

print(f'최댓값은 {max_of(nums)}입니다.')