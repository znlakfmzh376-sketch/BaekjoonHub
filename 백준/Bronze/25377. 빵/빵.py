import sys
input = sys.stdin.readline

N=int(input())
ans =[]
for i in range(N):
    A,B =map(int, input().split())
    if A<=B:
        ans.append(B)

if len(ans)==0:
    print(-1) 
else:
    print(min(ans))      
