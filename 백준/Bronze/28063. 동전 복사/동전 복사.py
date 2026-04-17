import sys
input = sys.stdin.readline

N = int(input())
x, y = map(int, input().split())

if N == 1:
    print(0)
elif (x == 1 and y == 1) or (x == 1 and y == N) or (x == N and y == 1) or (x == N and y == N):
    print(2)  # 모서리
elif x == 1 or x == N or y == 1 or y == N:
    print(3)  # 변위
else:
    print(4)  # 내부