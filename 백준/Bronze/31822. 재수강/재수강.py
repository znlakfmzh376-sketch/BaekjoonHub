import sys
input=sys.stdin.readline

s=input().strip()
N=int(input())
count =0
for i in range(N):
    a=input().strip()
    if s[:5]==a[:5]:
        count +=1

print(count)        

