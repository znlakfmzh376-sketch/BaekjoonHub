import sys
input = sys.stdin.readline

N,M=map(int,input().split())
result=0
for i in range(N):
    count=0
    a=input().strip()
    for i in range(M):
        if a[i]=='O':
            count+=1
        else:
            continue    
    if count>=(M//2+1):
        result +=1
    else:
        continue
print(result)            