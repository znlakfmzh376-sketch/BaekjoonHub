import sys
input = sys.stdin.readline

N = int(input())

if N % 2 == 0:
    print("I LOVE CBNU")
else:
    # 1. 첫 번째 줄: N개의 별 출력
    print("*" * N)
    
    # 2. 두 번째 줄: 정중앙 별 1개
    center = N // 2
    print(" " * center + "*")
    
    # 3. 세 번째 줄부터: V자 형태 (중앙 기준 왼쪽/오른쪽 공백 조절)
    for i in range(center):
        # 왼쪽 바깥 공백
        left_space = center - 1 - i
        # 별 사이 공백
        middle_space = 1 + 2 * i
        
        print(" " * left_space + "*" + " " * middle_space + "*")