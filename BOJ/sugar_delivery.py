# N키로그램의 설탕을 최소한의 봉지 수로 배달하는 경우

N = int(input())

kg_3 = 0
kg_5 = 0
idx = 0

if N % 5 == 0:
    print(N // 5)

else:
    kg_5 = N // 5
    if (N % 5) % 3 == 0:
        kg_3 = (N % 5) // 3
        print(kg_3 + kg_5)
    
    else:
        for i in range(1, kg_5 + 1):
            if ((N % 5) + i * 5) % 3 == 0:
                kg_5 -= i
                kg_3 = ((N % 5) + i * 5) // 3

                print(kg_3 + kg_5)
                break
    