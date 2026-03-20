import sys
input = sys.stdin.readline

arr= [[0]* 100 for i in range(100)]
N=int(input())
result=0

for _ in range(N):
    x,y=map(int, input().split())
    for i in range(x,x+10,1):
        for j in range(y,y+10,1):
            arr[i][j]=1

for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            result += 1

print(result)            
                       
        