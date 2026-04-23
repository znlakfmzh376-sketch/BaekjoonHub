import sys

input = sys.stdin.readline

N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]

# 누적합 배열
S= [[0]*(M+1) for _ in range(N+1)]
# 누적합 계싼
for i in range(1,N+1):
    for j in range(1,M+1):
        S[i][j]=arr[i-1][j-1]+S[i-1][j]+S[i][j-1]-S[i-1][j-1]
K=int(input())

for _ in range(K):
    i,j,x,y=map(int,input().split())
    result = S[x][y]-S[i-1][y]-S[x][j-1]+S[i-1][j-1]
    print(result)

    
        