import sys
input = sys.stdin.readline

N,X =map(int,input().split())
A = list(map(int,input().split()))
temp=sum(A)*X
for i in range(N-1):
    temp1=(A[i]+A[i+1])*X
    if temp1<temp:
        temp=temp1
    else:
        continue
print(temp)        
    

