import sys
input = sys.stdin.readline

N,M = map(int, input().split())
ans=0
arr=list(map(int,input().split()))
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if arr[i]+arr[j]+arr[k] <= M:
                ans = max(ans, arr[i]+arr[j]+arr[k])
print(ans)  
